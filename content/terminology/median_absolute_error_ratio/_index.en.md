---
title: "Median Absolute Error Ratio"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2500
draft: false
# metaタグのパラメータ
meta:
  description: "Median Absolute Error Ratio is the median of the absolute error ratio of the prediction for each piece of data included in the evaluation data."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
---

**Median Absolute Error Ratio** is the median of the absolute error ratio of the prediction for each piece of data included in the evaluation data.
In this context, median refers to the value in the middle of a sequence of numbers in ascending order.
In addition, the error ratio is the value obtained by dividing the error in numerical data by the correct value, and indicates the percentage of error with respect to the correct value.

It can be interpreted that approximately half of the data included in the evaluation data could be predicted with an error smaller than the median absolute error ratio.

Median values are aggregate values that are not easily affected by extreme values, so if you are interested in whether there are cases where the error is extremely large, you should also consider the mean absolute error and RMSE values.

{{% div_relitem contents-bottom %}}

- {{% a_in "../median_absolute_error/" "Median Absolute Error" %}}
- {{% a_in "../mean_absolute_error/" "Mean Absolute Error" %}}
- {{% a_in "../rmse/" "RMSE" %}}
- {{% a_in "../../tips/result/eval_reg/" "How to read prediction accuracy (regression)" %}}
- {{% a_in "../../trouble/createmodel/error_ratio/" "Question "Mean and median absolute error ratio may not be calculated"" %}}
  {{% /div_relitem %}}
