---
title: "Data cannot be read because it contains duplicate times."
date: 2018-12-29T11:02:05+06:00
lastmod: 2024-05-31T15:29:34+09:00
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
keywords: ["Time series mode", "Cannot be read", "Cannot read", "Duplicate"]
---

{{% h4_error_cause %}}
If the time information variable of the variable to be predicted specified in the time series prediction mode contains duplicate time stamps, a model for time series prediction cannot be created. This error can occur if more than 200 series exist in the prediction series.

{{% h4_error_avoid %}}
Check for duplicates in the time information variable of the variable you want to predict in the prediction model creation (training) data, and delete the duplicate data. If you get this error when predicting multiple series, make sure that there are no more than 200 series.
