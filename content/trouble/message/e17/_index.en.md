---
title: "Data cannot be imported because the character encoding is not supported."
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Encoding"]
---

{{% h4_error_cause %}}
This message appears if you import a file that uses character encoding that is not supported by Prediction One.

{{% h4_error_avoid %}}
To the file's character code

- UTF-8 (with BOM)
- Shift_JIS

You can then import the file by changing it.
