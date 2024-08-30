---
title: "Median Absolute Error"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2500
draft: false
# metaタグのパラメータ
meta:
  description: "Median Absolute Error is the median of the absolute error values when predicting for each data included in the evaluation data."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
---

**Median Absolute Error** is the median of the absolute error values when predicting for each data included in the evaluation data.
In this context, median refers to the value in the middle of a sequence of numbers in ascending order.

It can be interpreted that approximately half of the data included in the evaluation data could be predicted with an error smaller than the median error.

The median is an aggregate value that is not sensitive to extreme values, so if you are interested in whether there are cases where the error is extremely large, you may want to refer to mean absolute error, RMSE values, and distribution graphs of the prediction.

{{% div_relitem contents-bottom %}}

- {{% a_in "../mean_absolute_error/" "Mean Absolute Error" %}}
- {{% a_in "../rmse/" "RMSE" %}}
- {{% a_in "../../tips/result/eval_reg/" "How to read prediction accuracy (regression)" %}}
  {{% /div_relitem %}}
