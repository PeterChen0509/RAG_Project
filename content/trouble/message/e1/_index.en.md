---
title: "Prediction period [after XX] is not available and has been changed to [after XX]."
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
keywords: ["Time series mode", "Cannot specify"]
---

{{% h4_error_cause %}}
The prediction periods that you can specify in the time series prediction mode depend on the time range that is included in the time information variables for the variable you want to predict.
If the time data contained in the time information variable of the variable you want to predict is limited to a short period of time, the time range that can be specified as the prediction period is also reduced.

{{% h4_error_avoid %}}
In addition, if you want to specify future time as a prediction period, make sure that the prediction model creation (training) data includes more time in the past.
Predictable prediction periods vary depending on missing values for the variable to be predicted and the order of time in the prediction model creation (training) data.
