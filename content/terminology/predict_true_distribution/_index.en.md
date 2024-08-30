---
title: "Distribution of Prediction"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8500
draft: false
# metaタグのパラメータ
meta:
  description: "Distribution of Prediction is a visualization of the actual prediction. Each set of (predicted values, actual values) in the evaluation data is plotted as a point."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Scatter plot"]
---

Distribution of Prediction is a visualization of the actual prediction. Each set of (predicted values, actual values) in the evaluation data is plotted as a point. You can see the prediction intuitively.

![](../img_en/t_slide3.png)

The closer the point is to the diagonal of the graph, the more accurate the prediction. (the predicted value equals the actual value) By looking at the deviation from the diagonal, you can grasp situations such as not being able to predict well when the actual value is large.

![](../img_en/t_slide4.png)

When points are gathered around the diagonal line of the graph, there are many points of data where the actual value is close to the predicted value and the prediction accuracy is high. In such cases, you can expect this model to be a useful predictive model.
