---
title: "How do I specify more future time periods in a time series prediction?"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Time series", "Time", "Long", "Prediction period"]
---

The prediction periods that can be specified in the time series prediction mode are determined according to the time range included in the time information variables of the variable to be predicted in the prediction model creation (training) data.
If the time data contained in the time information variables of the variable you want to predict in the prediction model creation (training) data is limited to a short period of time, the time range you can predict is also limited.
Therefore, in order to predict more future periods, the prediction model creation (training) data must contain longer periods of data.
However, in general, the more you try to predict a longer time, the less predictable the prediction model will be.
