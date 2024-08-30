---
title: "Upturn/Downturn Prediction"
date: 2023-06-08T18:00:00+06:00
lastmod: 2023-06-08T18:00:00+06:00
weight: 1600
draft: false
# metaタグのパラメータ
meta:
  description: "Upturn/downturn prediction is a feature that predicts not only a single point corresponding to each instant in time when performing a time series prediction, but also a range of possible upturns and downturns."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Upturn/Downturn Prediction"]
---

Upturn/downturn prediction is a feature that predicts not only a single point corresponding to each instant in time when performing a time series prediction, but also a range of possible upturns and downturns. The "upturns and downturns" are what is known in statistical terms as the "prediction interval." Inside the model, the values themselves corresponding to each time and the standard deviations of the values are predicted. For how to use the upturn/downturn prediction feature, see Tips "{{% a_in "../../tips/new_features/prediction_interval/" "upturn/downturn prediction" %}}".

For coverage rate, an evaluation metric for upturn/downturn prediction, see the terminology description "{{% a_in "../coverage/" "Coverage rate" %}}".
