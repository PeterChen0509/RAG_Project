---
title: "Coverage Rate"
date: 2023-06-08T18:00:00+06:00
lastmod: 2023-06-08T18:00:00+06:00
weight: 2200
draft: false
# metaタグのパラメータ
meta:
  description: "Coverage rate is the probability that the correct value will be between the upturn and downturn in an upturn/downturn prediction. The target value for coverage rate is set to 90%."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Upturn/Downturn Prediction", "Coverage Rate"]
---

Coverage rate is the probability that the actual value will be between the upturn and downturn in an upturn/downturn prediction. Because Prediction One trains models to have a coverage rate near 90%, the closer the number is to 90%, the better the model is training.

![](../img_en/t_slide39.png)

This is the formula for calculating the score.

![](../img_en/t_slide40.png)

Since there is no way to observe actual upturn/downturn values, you cannot calculate the coefficient of determination, median absolute error, or other metrics used in time series prediction. In addition, a coverage rate of 90% does not necessarily guarantee upturn/downturn accuracy. Use coverage rate as a basic gauge for determining whether upturn/downturn predictions seem reasonable.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/new_features/prediction_interval/" "Upturn/Downturn Prediction" %}}

{{% /div_relitem %}}
