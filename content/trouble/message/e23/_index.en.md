---
title: "Cannot import data because there is only one variable."
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
# weight: カテゴリごとにまとめる
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
keywords: ["Item", "Cannot read", "One"]
---

{{% h4_error_cause %}}
If there is only one column in the prediction model creation (training) data, that data cannot be read and analyzed.
If you are not using time series prediction mode, the prediction model creation (training) data must contain a column containing the variable to be predicted <u>and at least one</u> column containing information related to the variable to be predicted.
When using time series prediction mode, the prediction model creation (training) data must contain a column for the variable to be predicted and <u> a column for the time information variable of the variable to be predicted</u>.

{{% h4_error_avoid %}}
The data that you want Prediction One to perform predictive analytics on must contain at least two columns, one for the variable to be predicted and one for the variable containing information related to it.
{{% a_in "../../../tips/how_to_create_dataset/" "Tips "How to create datasets"" %}}
