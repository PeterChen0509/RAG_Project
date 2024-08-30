---
title: "Precision"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 3400
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Precision", "Precision", "Precision rate"]
---

In some use cases of binary classification, you may be interested in finding one of the two values you wish to classify. For example, if you want to prevent equipment failure by predicting in advance, it is more important to predict and prevent failure than to predict normal. Precision, Recall, and F-score are measures focused on detection.

In the binary classification of "failure" or "normal", the value of "failure" is specified as the prediction value.
The percentage of the data predicted by the prediction model as "failure" for which "failure" was actually correct is called <b>Precision</b>.
This is also called "precision rate."

See also the {{% a_in "../recall/" "Recall rate (Recall) " %}} page.

{{% div_relitem contents-bottom %}}

- {{% a_in "../recall/" "Recall" %}}
- {{% a_in "../binary_classification/" "Binary Classification" %}}
- {{% a_in "../multiclass_classification/" "multiclass classification" %}}
- {{% a_in "../../tips/result/eval_bin/" "How to read prediction accuracy (binary classification)"%}}
  {{% /div_relitem %}}
