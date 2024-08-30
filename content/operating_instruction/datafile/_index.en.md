---
title: "Data List Screen"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 5
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  [
    "Data",
    "Upload",
    "File",
    "Dataset",
    "Shared",
    "Sample data",
  ]
---

Clicking the "Data" button takes you to this screen.

![](../img_en/t_slide68.png)

{{% div_method_area "Check file attributes" %}}

You can check the attribute information of each uploaded file in the "File List".

- Filename: File name of the data.
- Date and Time: The date and time the file was uploaded.
- Size: The size of the file. There is an upper limit on the total size of files that can be uploaded.
- Rows: The number of rows of data.
- Columns: The number of columns (variables) in the data.
- Uploaded by: The user who uploaded the file. If there is a nickname setting, the nickname is displayed. If there is no setting, the account ID is displayed.
{{% /div_method_area %}}

{{% div_method_area "Preview a file" %}}
{{% step_n2 1 "In the "File List", click the "Details" button." %}}
{{% step_n2 2 "Displays the top 10 rows of the file." %}}
{{% /div_method_area %}}

{{% div_method_area "Check the storage capacity" %}}

There is a fixed limit to the total amount of data that can be uploaded. You can check the limit and the current amount used by looking at "Storage capacity". Files cannot be uploaded if they exceed the limit. The upper limit is decided for each plan. Personal and shared capacity counts separately.

{{% div_method_area "Switch between tabs of data" %}}

The following three data list screens can be switched by the tabs.

- Personal: This screen lists personal data. Data that only you can access.
- Shared: A screen that lists data for sharing. Data that can be shared between accounts belonging to the same tenant (group). The free trial version doesn't offer data sharing, so you won't see a sharing tab.
- Sample: Sample data for use in the tutorial.
{{% /div_method_area %}}

{{% div_method_area "Upload a file" %}}
{{% step_n2 1 "Click the "Upload" button." %}}
{{% step_n2 2 "In the window that appears, drag and drop the file you want to upload." %}}
You can also specify a file from the "Select Local File" button.
You can upload files in either the csv (comma-delimited) or tsv (tab-delimited) format.
{{% /div_method_area %}}

{{% div_method_area "Delete an uploaded file" %}}
{{% step_n_area2 1 "In "File List", click the check button for the file you want to delete." %}}
You can select multiple files.
{{% /step_n_area2   %}}
{{% step_n2 2 "Click the "Delete" button" %}}
{{% step_n_area2 3 "Click [Delete] in the dialog box that appears after clicking" %}}
Alternatively, you can select "Delete" from the three-point reader at the right end of each file line in the "File List".
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Transfer data from an external service" %}}
{{% step_n_area2 1 "Click [Data connector]." %}}
{{% /step_n_area2   %}}
{{% step_n_area2 2 "In the window that appears, enter the required information for accessing the external service." %}}
{{% /step_n_area2   %}}
{{% step_n_area2 3 "Click "Transfer" from the list of files displayed." %}}
{{% /step_n_area2   %}}
{{% step_n_area2 4 "In the window that appears, enter the filename to save as and click "Transfer"." %}}
You can transfer files in either the csv (comma-delimited) or tsv (tab-delimited) format.
{{% /step_n_area2   %}}
{{% /div_method_area %}}

{{% div_method_area "Copy uploaded Personal files to Shared" %}}
{{% step_n_area2 1 "Select "Copy" from the three-point reader at the right end of the file you want to share in the "File list"." %}}
You cannot upload files directly to Shared. Please copy the Personal upload for Shared.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Download an uploaded file" %}}
{{% step_n2 1 "In the "File list", select "Download" from the three-point reader at the right end of the file you want to download." %}}
{{% step_n2 2 "It is downloaded in the manner specified by the browser." %}}
{{% /div_method_area %}}

{{% div_method_area "Rename a file" %}}
{{% step_n2 1 "Click [Rename] from the three-point reader at the right end of each file line in the "File List"." %}}
{{% step_n2 2 "In the window that appears, enter the name of the file you want to change and click "Rename"." %}}
{{% /div_method_area %}}

{{% div_method_area "Creating Models from Uploaded Files" %}}
{{% step_n2 1 "In the "File List", select "Create Model" from the three-point reader at the right end of the target file." %}}
{{% step_n2 2 "Proceed to model creation from the displayed model setup screen as usual." %}}
{{% /div_method_area %}}