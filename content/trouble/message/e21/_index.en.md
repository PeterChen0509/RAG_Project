---
title: "The training process cannot be performed due to insufficient data."
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
keywords: ["Amount of data", "Small amount", "Insufficient data", "Training process"]
---

{{% h4_error_cause %}}
If there is not enough data to create a prediction model, the training process cannot proceed.

{{% h4_error_avoid %}}
Import prediction model creation (training) data that contains at least 11 rows.
Some prediction types require more data.
Also, if the data count included in the prediction model creation (training) data is too low, the performance of the prediction model may not improve.

{{% notice tip "../../../tips/how_to_create_dataset/index.html" "How to create datasets" %}}
For the relation between the amount of data and predictive performance, see Tips How to Create a Dataset.
{{% /notice %}}
