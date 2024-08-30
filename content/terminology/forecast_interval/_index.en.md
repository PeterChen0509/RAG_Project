---
title: "Prediction Interval"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8500
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Interval Section"]
---

**Prediction Interval** refers to the period from when to when you want to predict in the time series prediction model.

Suppose you want to predict the number of shipments for each product between January and March 2019.
Prepare data for the number of shipments of product A, product B, and product C for each month until December 2018 as the prediction model creation (training) data, and input it into Prediction One.

![](../img_en/t_slide9.png)

The <u>January to March 2019 period for which you want to predict the number of shipments is 1 to 3 months ahead of December 2018, the last month included in the data for prediction model creation (training)</u>. In such cases, specify "from a month to three months from now" as the prediction interval.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../trouble/message/e5/" "Message [Could not learn in the specified prediction interval]" %}}
  {{% /div_relitem %}}
