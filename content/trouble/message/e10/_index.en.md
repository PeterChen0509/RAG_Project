---
title: "Prediction data does not contain any predictable time data."
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
keywords: ["Time series mode"]
---

{{% h4_error_cause %}}
You cannot predict for data outside the prediction periods specified in time series prediction mode.
For example, a prediction model that predicts data for periods between `2020/1/1`–`2020/1/31` cannot predict data `2020/2/1` or later.

{{% h4_error_avoid %}}
Make sure that the time information column of the variable you want to predict in the prediction data contains the time information included in the prediction period.
Set the prediction periods to include the times you want to predict and learn the prediction models.
