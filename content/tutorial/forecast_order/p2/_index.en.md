---
title: "Story: Order prediction based on data"
date: 2023-06-13T11:02:05+06:00
lastmod: 2023-06-13T10:42:26+06:00
weight: 2
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
tutorial_page:
  is_next_exists: true
---

#### Situations and Challenges: Using accurate order predictions to prevent shortages and overstocking

You are in charge of production control at a site that manufactures parts for home electronics.
To maintain optimal inventory levels, you predict the number of orders in advance and use the results to determine the corresponding manufacturing volume.
Prediction One's time series prediction mode has enabled you to predict the number of orders at a higher degree of accuracy compared to when you did your forecasts through a manual, trial-and-error approach. While that makes it possible to automate adjustments to manufacturing volume, you also run into overstocking issues and shortages when there are sizable gaps between the prediction values and the actual values.

#### Using Predictive Analytics: Predicting the number of orders based on data and predicting upturn/downturn

- Prepare historical data of orders (you will use sample datasets in the tutorial)
- Use Prediction One to predict the number of orders for future months and predicting upturn/downturn
- Plan production based on order predictions

#### Expected Effect: Reducing overstocking and preventing shortages to secure sales opportunities

As you develop your manufacturing plans based on the prediction results you obtain from normal time series prediction mode, you can now refer to upturn and downturn—upturn prediction values on the order side when you want some extra inventory, downturn prediction values when you want to trim surplus inventory—to streamline your plans in an efficient, flexible manner.

**Now let's actually predict the number of orders with Prediction One!**
