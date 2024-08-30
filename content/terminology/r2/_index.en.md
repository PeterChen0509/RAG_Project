---
title: "Coefficient of Determination"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2400
draft: false
# metaタグのパラメータ
meta:
  description: "Coefficient of Determination is a metric that measures the performance of a numerical prediction model. In general, the higher the value, the better, and in the best case, at 1. It is used to check the correlation between the correct values in the evaluation data and the values predicted by the prediction model."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Coefficient of Determination", "R2"]
---

**Coefficient of Determination** is a metric that measures the performance of a numerical prediction model. In general, the higher the value, the better, and in the best case, at 1. It is used to check the correlation between the correct values in the evaluation data and the values predicted by the prediction model.

![](../img_en/t_slide16.png)

When the coefficient of determination is close to 1, there tends to be a correlation between the correct value and the predicted value.
At this point, the distribution of predictions is more diagonal and dotted. The figure below shows an example where the coefficient of determination is approximately 0.98.

![](../img_en/t_slide32.png)

On the other hand, the coefficient of determination is small if the prediction is close to being independent of the correct value.
In such cases, the distribution of predictions is likely to have points that are off the diagonal. The figure below shows an example where the coefficient of determination is approximately 0.20.

![](../img_en/t_slide33.png)

{{% div_relitem contents-bottom %}}

- {{% a_in "../regression/" "Regression" %}}
- {{% a_in "../../tips/result/eval_reg/" "How to read prediction accuracy (regression)" %}}

{{% /div_relitem %}}
