---
title: "Recall"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 3100
draft: false
# metaタグのパラメータ
meta:
  description: "Recall is the percentage of the actual positive that was predicted to be positive."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
---

In some use cases of binary classification, you may be interested in finding one of the two values you wish to classify.
For example, if you want to prevent equipment failure by predicting in advance, 
it is more important to predict and prevent failure than to predict normal.
Precision, Recall, and F-score are measures focused on detection.

**Recall** is the percentage of the actual positive that was predicted to be positive.

![](../img_en/t_slide24.png)

For example, the confusion matrix in this figure predicts and guesses 20 pieces of data in "Purchased" of 20 + 10.
In this case, the Recall is (20/(20 + 10)) = 0.66.

{{% div_relitem contents-bottom %}}

- {{% a_in "../precision/" "Precision " %}}
- {{% a_in "../binary_classification/" "Binary Classification" %}}
- {{% a_in "../multiclass_classification/" "multiclass classification" %}}
- {{% a_in "../../tips/result/eval_bin/" "How to read prediction accuracy (binary classification)"%}}
  {{% /div_relitem %}}
