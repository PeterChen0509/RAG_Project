---
title: "Parameter Search"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 5100
draft: false
# metaタグのパラメータ
meta:
  description: "Parameter Search refers to the adjustment of predictive model settings (usually called a hyperparameter) to improve predictive model performance."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Parameter", "Tuning", "Hyperparameter Search", "Adjustment"]
---

**Parameter Search** refers to the adjustment of predictive model settings (usually called a hyperparameter) to improve predictive model performance.
In general, to create a high performance prediction model, it is necessary to use trial and error to create and evaluate a prediction model with various settings.

### Parameter search in Prediction One

Prediction One automatically searches for all parameters.
Also, when the amount of data is small, cross-validation is automatically performed, and a prediction model with high possibility of good performance is created.

{{% div_relitem contents-bottom %}}

- <a href="../cross_validation/index.html">Cross-validation</a>

{{% /div_relitem %}}
