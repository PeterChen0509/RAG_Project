---
title: "It is unavailable prediction types for the prediction target because of the data type and unique label counts."
date: 2018-12-29T11:02:05+06:00
lastmod: 2024-05-31T10:44:30+09:00
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
keywords: ["binary classfication", "multi classification", "cannot train"]
---

{{% h4_error_cause %}}
It may detect that it can not create the prediction model with the selected prediction type, in the training process for 'binary-classfication model' or 'multi-classification model'.  

{{% h4_error_avoid %}}
For the item you wish to predict, prepare the data so that all classification patterns appear in the first 1000 rows of data.  
If you use automatically extractiton mode for the evaluation data, changing the order of the data may solve this problem.  
