---
title: "Prediction Accuracy Level"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8500
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Level", "Prediction Accuracy Level"]
---

Prediction One provides a **Model Level** as a reference for how good a prediction model created from prediction model creation (training) data is.

![](../img_en/t_slide1.png)

The model level is expressed as 1 to 5 stars, and the higher the number of stars, the better the prediction model.

The model level is calculated based on the evaluation metrics that are presented together on the model summary screen. The accuracy evaluation from which the calculation is made depends on the problem as follows:

- For binary classification：{{% a_in "../roc_curve_auc/" "AUC" %}}
- For multiclass classification: {{% a_in "../accuracy/" " percentage of correct answers (Accuracy) " %}}
- numerical prediction: {{% a_in "../r2/" "Coefficient of Determination" %}}
- For time series predictions: {{% a_in "../median_absolute_error_ratio/" "Median Absolute Error Ratio" %}}

In general, the higher the model level, the more accurate your prediction model will be.
However, each use case must determine whether the model is actually a useful model.
