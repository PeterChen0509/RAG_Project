---
title: "Creating a Customer List"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 13
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
tutorial_page:
  is_next_exists: true
---

{{% div_slide "Labeling Complaint Types" normal  first-page %}}

From the prediction results file, the complaint type with the highest probability of prediction for each review statement is the complaint type for that review statement.

![](../img_en/t_slide20.png)

Actually, the prediction accuracy is not 100%, so it may be mistaken. If the highest probability value is not high, the confidence in the prediction is low, so it may be better for a human to check such cases.
{{% /div_slide %}}
