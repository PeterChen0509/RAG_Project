---
title: "I cannot click \"Create Prediction Model\" after selecting the variable I want to predict"
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
keywords: ["Create Prediction Model"]
---

{{% h4_error_cause %}}

If there is no variable checked for "Use for model" other than the variable you want to predict, you cannot create a prediction model.
When you click [Create Model], Prediction One creates a prediction model that predicts the value of the variable you want to predict based on a variety of information other than the variable you want to predict.
Therefore, a prediction model cannot be created when there is no information available other than the variables to be predicted.

You can click [Create Model] by following the steps below.

{{% step_n 1 "Go to the advanced settings screen" %}}

![](../../img_en/t_slide1.png)

{{% step_n 2 "Check "Use for model"." %}}

![](../../img_en/t_slide2.png)

{{% step_n 3 "Make sure that [Create Model] can be clicked." %}}

![](../../img_en/t_slide3.png)
