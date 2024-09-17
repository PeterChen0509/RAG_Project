import os
import re
import glob
import yaml
from typing import List
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

def find_jp_md_files(root_dir):
    # find all jp.md files in the root_dir
    jp_md_files = []
    for dir_path, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.jp.md'):
                full_path = os.path.join(dir_path, file)
                jp_md_files.append(full_path)
    return jp_md_files

def extract_path(file):
    # content directory
    parts = file.split("content/")
    if len(parts)>1:
        relevant_path = parts[1]
        relevant_path = os.path.dirname(relevant_path)
        return relevant_path

def process_md_files(jp_md_files: List[str]) -> List[Document]:
    # Read all jp.md files and extract metadata, content
    all_chunks = []
    for file_path in jp_md_files:
        with open(file_path, 'r') as f:
            md_content = f.read()
        parts = md_content.split('---', 2)
        if len(parts) < 3:
            print(f"Error: {file_path} has missing info")
            continue
        try:
            metadata = yaml.safe_load(parts[1].strip("\n"))
        except yaml.YAMLError:
            print(f"Error: Unable to parse YAML in {file_path}")
            continue
        content = parts[2].strip("\n")
        source_path = extract_path(file_path)
        doc = Document(
            page_content = content,
            metadata = { 
                "title": metadata.get("title", "").strip(""),
                "description": metadata.get("meta", {}).get("description", "").strip(""),
                "keywords": metadata.get("keywords", []),
                "source_path": source_path,
            }
        )
        all_chunks.append(doc)
    return all_chunks
            
def clean_html(text: str) -> str:
    # clean html tags, markdown tags, and other special characters
    text = re.sub(r'{{[<%]?\s*/?dist_type_exclude\s*(?:"[^"]*")?\s*[%>]?}}', ' ', text)
    text = re.sub(r'{{% /desktop_only %}}', ' ', text)
    text = re.sub(r'{{<\s*ref\s+"([^"]+)"\s*>}}([^)]+)', r'\1\2', text)
    text = re.sub(r'{{% a_in\s+"([^"]+)"\s+"([^"]+)"(?:\s+"[^"]*")?\s+%}}', r' [\2](\1)', text)
    text = re.sub(r'{{% step_n\s+\d+\s+"([^"]+)"\s+%}}', r'\1', text)
    text = re.sub(r'<a[^>]*>(.*?)', r'\1', text)
    text = re.sub(r'<img[^>]*src="([^"]*)"[^>]*>', r'![](\1)', text)
    text = re.sub(r'{{% dist_type_only\s+"[^"]+"\s+%}}', ' ', text)
    text = re.sub(r'{{% /dist_type_only %}}', ' ', text)
    text = re.sub(r'{{% notice\s+tip\s+"([^"]+)"\s+"([^"]+)"\s+%}}', r'[Tip: \2](\1)', text)
    text = re.sub(r'{{% /notice %}}', ' ', text)
    text = re.sub(r'{{% desktop_only %}}(.*?){{% /desktop_only %}}', r'[Desktop Only] \1', text, flags=re.DOTALL)
    text = re.sub(r'{{% cloud_only %}}(.*?){{% /cloud_only %}}', r'[Cloud Only] \1', text, flags=re.DOTALL)

    tags_to_remove = [
        r'<tr[^>]*>', r'</tr>',
        r'<td[^>]*>', r'</td>',  
        r'<p[^>]*>', r'</p>',
        r'</a>', r'<a[^>]*>',
        r'<table[^>]*>', r'</table>',
        r'<b[^>]*>', r'</b>',
        r'<br\s*/?>', 
        r'<style[^>]*>.*?</style>',
        r'<details[^>]*>', r'</details>',
        r'<div[^>]*>', r'</div>',
    ]
    for tag in tags_to_remove:
        text = re.sub(tag, ' ', text, flags=re.DOTALL)
    
    patterns = [
        r'{{[<%]?\s*/?dist_type_exclude\s*(?:"[^"]*")?\s*[%>]?}}',
        r'{{<\s*youtube\s+[^>]*>}}', 
        r'{{[<%][^}]*[%>]}}',  
    ]
    for pattern in patterns:
        text = re.sub(pattern, ' ', text)
    
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'^-\s*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def chunk_md_files(all_chunks: List[Document]) -> List[Document]:
    # Split the content into chunks
    new_chunks = []
    for doc in all_chunks:
        headers_to_split = [
            ("#", "Subtitle"),
            ("##", "Subtitle"),
            ("###", "Subtitle"),
            ("####", "Subtitle"),
            ("#####", "Subtitle"),
            ("######", "Subtitle"),
        ]
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split)
        splits = markdown_splitter.split_text(doc.page_content)
        chunk_id = 0
        for split in splits:
            new_chunk = Document(
                metadata = {**doc.metadata, **split.metadata, "chunk_id": chunk_id},
                page_content = clean_html(split.page_content),
            )
            new_chunks.append(new_chunk)
            chunk_id += 1
    return new_chunks


