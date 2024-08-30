---
title: "Prediction Reason / Predictive Contribution"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8500
draft: false
# metaタグのパラメータ
meta:
  description: "Contribution is a numerical expression of how much each variable and value of the data affect the prediction result."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Importance", "importance"]
---

**Contribution** is a numerical expression of how much each item and value of the data affects the prediction result.
For example, suppose you create a prediction model that predicts the closing price of real estate and you get the following results:

![](../img_en/t_slide2.png)

In this case, it can be read that real estate properties whose "Address" is "Tokyo 23 wards" are likely to have an increase in "contract price".
For further details on reading the contribution, see "{{% a_in "../../tips/result/contribution/" "How to read the predictive contribution"%}}".

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/result/contribution/" "How to read the predictive contribution" %}}
  {{% /div_relitem %}}
