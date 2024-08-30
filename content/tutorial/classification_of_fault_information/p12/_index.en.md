---
title: "Failure Type Classification"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 12
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

{{% div_slide "Using Predicted Results to Automate Type Classification" normal first-page %}}

By classifying the failure type with the highest probability from the predicted probability for all failure information, the failure type can be classified automatically.

![](../img_en/t_slide20.png)

Actually, the prediction accuracy is not 100%, so it may be mistaken. If the highest probability value is not high, the confidence in the prediction is low, so it may be better for a human to check such cases.
{{% /div_slide %}}
