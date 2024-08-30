---
title: "Could not train over the specified prediction period."
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
keywords: ["time series mode", "prediction period"]
---

{{% h4_error_cause %}}
Prediction periods that can be specified in the time series prediction mode are determined according to the time range included in the time information variables of the variable to be predicted in the prediction model creation (training) data.
If the time data contained in the time information variables of the variable you want to predict in the prediction model creation (training) data is limited to a short period of time, the time range you can predict is also limited.

{{% h4_error_avoid %}}
When predicting "X days in advance", use data that is twice as long as X.

For example, if you predict 100 days in the future, you should have more than 200 days of prediction model creation (training) data.
The number of days ahead that can be predicted depends on a variety of conditions, such as the type of time and interval included in the data. If you want to predict more time ahead, you need to prepare more data for prediction model creation (training).
