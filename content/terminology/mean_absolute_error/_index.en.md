---
title: "Mean Absolute Error"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2500
draft: false
# metaタグのパラメータ
meta:
  description: "Mean Absolute Error is the average of the absolute values of the errors in the predictions for each piece of data included in the evaluation data."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
---

**Mean Absolute Error** is the average of the absolute values of the errors in the predictions for each piece of data included in the evaluation data."

Mean Absolute Error is easily affected by abnormal data. For example, when the evaluation data contains a sample with a very large error (a single piece of data is called a sample. For example, in customer data, it refers to a customer), the mean absolute error tends to take a large value compared to the median absolute error. It is a good idea to evaluate it together with the median absolute error rate and the distribution graph of the prediction.

![](../img_en/t_slide15.png)

{{% div_relitem contents-bottom %}}

- {{% a_in "../median_absolute_error/" "Median Absolute Error" %}}
- {{% a_in "../rmse/" "RMSE" %}}
- {{% a_in "../../tips/result/eval_reg/" "How to read prediction accuracy (regression)" %}}
  {{% /div_relitem %}}
