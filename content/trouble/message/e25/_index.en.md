---
title: "Data cannot be imported because there are multiple variables with the same name."
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
keywords: ["Same name", "Duplicate"]
---

{{% h4_error_cause %}}
All variables in the prediction model creation (training) data must have different names.

{{% h4_error_avoid %}}
Edit the variables in the prediction model creation (training) data and evaluation data so that there is no overlap.
This error also appears if there are multiple columns with blank variable names. In this case, give each blank column a different name, or remove the blank column.
