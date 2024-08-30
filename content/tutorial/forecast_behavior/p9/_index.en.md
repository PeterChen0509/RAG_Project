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

After training with the prediction model, it automatically evaluates the prediction accuracy. This screen provides a summary of the model evaluation.

The prediction accuracy is calculated by comparing the actual results with the predicted results of the prediction model that is created.
We found that we can predict the vacation acquisition achievement with good accuracy from the number of stars at the prediction accuracy level!
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide12.png)

Select "Evaluation" to see a more detailed evaluation.
Evaluated values of prediction accuracy from various perspectives and tables and graphs of prediction accuracy are generated. You can scroll down to browse.
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide13.png)

We found that the prediction accuracy is high. So why is the prediction accuracy high?
Click [Understanding].
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide14.png)

In the vacation acquisition prediction,
"Number of vacations taken in the last 3 months" is valid, and from the information on the right side,
it is easy to achieve if the acquisition number is large.

You can check if it matches your intuition.
They may also discover unexpected relationships (length of service was more related to the achievement of vacation than expected, etc.).

Then click [Predict].
{{% /div_slide %}}
