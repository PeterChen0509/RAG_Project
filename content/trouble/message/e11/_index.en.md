---
title: "Cannot auto-generate prediction data for time series prediction mode."
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
keywords: ["Time series mode", "Auto-generation", "Target"]
---

{{% h4_error_cause %}}
To automatically generate prediction data, 

- Variable to be predicted
- Time information variable of the variable to be predicted

must be the only two columns used to create the model during training.

{{% h4_error_avoid %}}
Automatic generation is possible if the files used for learning have only two columns: "Variable to be predicted" and "Time information variable of the variable to be predicted".

However, the more information that is relevant to the variable you want to predict, the more accurate the prediction model will be.
If you add information other than "Variable to be predicted" and "Time information variable of the variable to be predicted" to your learning, you will need to include that data in your predictions.
See also {{% a_in "../../../tips/specification/dataset_for_timeseries/" "Sample Dataset for regression (time series prediction mode)" "timeseries-no-feature"%}}.
