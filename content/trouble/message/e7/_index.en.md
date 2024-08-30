---
title: "The number of series is not 200 or fewer, so the data cannot be imported."
date: 2018-12-29T11:02:05+06:00
lastmod: 2024-05-31T09:59:22+09:00
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
keywords: ["time series mode", "number of series", "upper limit", "multiple series"]
---

{{% h4_error_cause %}}
In time series prediction mode, you can create a prediction model for up to 200 series simultaneously.
If the specified series contains more than 200 types of variables, you cannot create a prediction model.

{{% h4_error_avoid %}}
Divide the prediction model creation (training) data so that it contains no more than 200 series.
