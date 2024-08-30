---
title: "Viewing Evaluation Results"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 9
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

{{% div_slide "Step 1" normal first-page %}}

![](../img_en/t_slide11.png)

After learning the prediction model, it automatically evaluates the prediction accuracy. This screen provides a summary of the model evaluation.

The prediction accuracy is calculated by comparing the actual results with the predicted results of the prediction model that is created.
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide12.png)

Select "Evaluation" to see a more detailed evaluation.
Evaluated values of prediction accuracy from various perspectives and tables and graphs of prediction accuracy are generated. You can scroll down to browse.
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide13.png)

We found that the prediction accuracy value. Click [Understanding].
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide14.png)

In the prediction model created this time, "Systolic blood pressure (mmHg)" is regarded as an effective variable, and further from the content on the right
High levels of systolic blood pressure (mmHg) shows that the model tends to predict a higher morbidity.
Then click "Predict".
{{% /div_slide %}}