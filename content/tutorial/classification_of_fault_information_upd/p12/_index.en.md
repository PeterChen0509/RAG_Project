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
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: [""]
tutorial_page:
  is_next_exists: true
---

{{% div_slide "Using Predicted Results to Automate Type Classification" normal first-page %}}

By classifying the failure type with the highest probability from the predicted probability for all failure information, the failure type can be classified automatically.
A particular feature of the current model is that it has performed prediction based on the information of failures that have occurred recently.

![](../img_en/t_slide32.png)

Now we can perform prediction reflecting the latest data!
The cause of failure is expected to change as time goes by. When operating a prediction model, it is recommended that you review how accurate the predictions are
and update the model as required.
{{% /div_slide %}}
