---
title: "Failed to generate join data."
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
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["generation failure"]
---

{{% h4_error_cause %}}
This message appears if the data join fails for any reason.

{{% h4_error_avoid %}}
There are several possible causes.
Check for the following problems:

- There are a lot of missing values in the variable you want to predict.
- Too many unique values in the variables to predict (Has a unique number greater than or equal to 3 for binary classification and greater than {{% t_mul_max_class%}} for multiclass classification)
- The variable specified as the join relation (the join key) is not specified correctly.
