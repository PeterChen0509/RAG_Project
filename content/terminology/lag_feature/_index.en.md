---
title: "Past Value of the Variable to be Predicted"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Lag features", "Time difference", "Past value", ""]
---

The past value of a variable that you want to predict is a variable that was created by referring to the past value in order to predict the value in the future rather than at a certain point in time.

For example, in {{% a_in "../../tutorial/forecast_demand/" "Product shipment forecast tutorial" %}}, we are trying to forecast the number of shipments for the next 12 months.
At this time, in order to make a prediction 3 months or 4 months ahead of a certain point in time, we make a prediction by referring to information such as the number of shipments 12 months or 24 months prior.
The Prediction One time series model automatically determines when values are referenced.
In this way, the variables created based on the past information are displayed as the past values of the variables that you want to predict.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/new_features/timeseries/" "Time series prediction" %}}
  {{% /div_relitem %}}
