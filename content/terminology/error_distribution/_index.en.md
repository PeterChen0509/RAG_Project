---
title: "Distribution of Prediction Errors"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8500
draft: false
# metaタグのパラメータ
meta:
  description: "Distribution of Prediction Errors is a graphical representation of how much percent of the data contained in the evaluation data is wrong (= Error) when the prediction model is evaluated using the evaluation data."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
---

**Distribution of Prediction Errors** is a graphical representation of how much percent of the data contained in the evaluation data is wrong (= Error) when the prediction model is evaluated using the evaluation data.

Distribution of prediction errors shows the overall picture of prediction errors.
The bar chart shows the percentage of the total prediction error between 0 and 5, the percentage of the total prediction error between 5 and 10, and so on.
You can see what kind of error the prediction is likely to have.

![](../img_en/t_slide7.png)

In the figure above, approximately 11.4% of the data in the evaluation data was predicted with an error within 0 to 100.
Also, no data with an error of 700 to 800 existed.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/result/eval_reg/" "How to read prediction accuracy (regression)" %}}

{{% /div_relitem %}}
