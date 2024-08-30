---
title: "The data cannot be imported because there are too many variables."
date: 2018-12-29T11:02:05+06:00
lastmod: 2024-05-30T14:48:14+09:00
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
keywords: ["Upper limit"]
---

{{% h4_error_cause %}}
Prediction One cannot read more than 1,000 csv columns.
You cannot import csv data that exceeds 200 columns in the time series prediction mode.

{{% h4_error_avoid %}}
Create prediction model creation (training) data with less than 1,000 columns. In time series prediction mode, the data should be less than 200 columns.

When you delete columns, you should first delete columns that do not appear to be relevant to the variable you want to predict.
