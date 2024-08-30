---
title: "There is too little data in the evaluation data that contains the correct value available for the variable you want to predict."
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
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["too little", "cannot train"]
---

{{% h4_error_cause %}}
When performing binary classification or multiclass classification, if there is a bias in the values included in the variables to be predicted in the data for prediction model creation (training) and the data for evaluation,
This message appears and the learning process may fail.

For example, to create a binary classification of whether a customer "exits" or "stays"
If you prepare the data including 1 customer who "withdrew" and 100 customers who "stayed" as prediction model creation (training) data,
this message may be displayed.

{{% h4_error_avoid %}}
Prepare the prediction model creation (training) data so that the bias of the variables you want to predict is reduced.
Alternatively, specify evaluation data that can exist for all types of correct values.
