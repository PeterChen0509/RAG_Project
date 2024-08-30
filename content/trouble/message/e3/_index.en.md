---
title: "Unable to read data due to a long period of no data."
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
keywords: ["Cannot be read", "Cannot read", "Time series mode"]
---

{{% h4_error_cause %}}
When performing a time series prediction in "time series prediction mode", the time interval of the time included in the time information variable of the specified variable to be predicted must be kept as constant as possible.  
This message is displayed if the timestamp in the time information variable of the variable you want to predict is re-ordered over time and long periods of missing data is detected.

{{% h4_error_avoid %}}
Check the data contained in the time information variable of the variable you want to predict, collect the data of the place where the time interval is blank, and add it to the prediction model creation (training) data. Or, remove the previous data from the prediction model creation (training) data where the time interval is blank.
For information on how to create training and prediction data for use in the time-series prediction mode, see also "{{% a_in "../../../tips/specification/dataset_for_timeseries/" "Dataset for regression (time series prediction mode)" %}}".
