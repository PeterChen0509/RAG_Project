---
title: "Cannot perform data joining because of differences between training and evaluation data variables."
date: 2018-12-29T11:02:05+06:00
lastmod: 2024-05-30T11:42:19+09:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
  # hide_on_dist_type: ["SNC", "RDC"]
# 検索でヒットする文字列の指定
keywords: ["join failure"]
---

{{% h4_error_cause %}}
This message appears if the joined learning data and evaluation data contain different variables.

Prediction models use data in the same format as the training data to evaluate how accurate predictions can be.
Therefore, the variables in the joined learning data and evaluation data must match.

{{% h4_error_avoid %}}
Ensure that the variables in the joined learning data and evaluation data match exactly.
