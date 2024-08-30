---
title: "Data cannot be loaded because it contains data for time intervals that are not supported."
date: 2018-12-29T11:02:05+06:00
lastmod: 2024-05-31T15:09:54+09:00
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
keywords: ["time series mode", "time interval", "format"]
---

{{% h4_error_cause %}}
Prediction One does not allow time series predicting for time intervals of less than minutes.

{{% h4_error_avoid %}}
Prepare data with equal time intervals in units of minutes or more.  
Prediction One can create a prediction model with the last day of the month aligned if all the time information variables for the variable you want to predict are on the last day of the month. If you have the time information variables of the variable you want to predict on the last day of the month, please check if there is any data not on the last day of the month.  
  
Please refer to the {{% a_in "../../../tips/specification/dataset_for_timeseries/" "Supported time interval in the dataset for regression (time series prediction mode)" "time-interval"%}}.
