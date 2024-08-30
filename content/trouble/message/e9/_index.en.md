---
title: "The data cannot be read because there is a date and time that are not within the supported time period."
date: 2018-12-29T11:02:05+06:00
lastmod: 2024-05-31T15:26:01+09:00
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
keywords: ["time series mode", "supported period"]
---

{{% h4_error_cause %}}
Prediction One cannot treat data, prior to 1970/01/01 or on and after 4000/01/01, as a time variable for the variable you want to predict.

{{% h4_error_avoid %}}
Only use data from 1970/01/01 to 4000/01/01 for prediction model creation (training).
