---
title: "Accuracy"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 3400
draft: false
# metaタグのパラメータ
meta:
  description: "Accuracy is a measure of the percentage of all samples (a single piece of data is called a sample. For example, in customer data, it refers to customers) in the evaluation data that can be correctly identified."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Accuracy", "Accuracy", "Accuracy"]
---

Accuracy is a measure of the percentage of all samples (a single piece of data is called a sample. For example, in customer data, it refers to customers) in the evaluation data that can be correctly identified.

For example, if "(a) Withdrawal" is set as the prediction value, and the following confusion matrix is obtained,

{{% div_confmat twoclass %}}

|         | (a) Withdrawal | (b) Continuation |
| :------ | :-----: | :-----: |
| (a) Withdrawal |    4    |    5    |
| (b) Continuation |    6    |    7    |

{{% /div_confmat %}}

Out of the total number of samples (4 + 5 + 6 + 7 = 22), the number that correctly predicted "(a) Withdrawal;" "(b) Continuation" is 4 + 7 = 11.
In this case, Accuracy is **50%**, because 11/22 = 0.5.
