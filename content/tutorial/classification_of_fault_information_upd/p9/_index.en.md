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
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: [""]
tutorial_page:
  is_next_exists: true
---

{{% div_slide "Step 1" normal first-page %}}


![](../img_en/t_slide11.png)

After training with the prediction model, it automatically evaluates the prediction accuracy. This screen provides a summary of the model evaluation.
The comparison summary shows the accuracy of the current prediction in comparison to the accuracy of the most recent prediction.
Looking at the change in the Accuracy values, you can see that the current prediction model can predict failure types more accurately!
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide12.png)

A look at the comparison of evaluation values gives you an even more detailed picture of the two sets of evaluation results.
You can also see the difference in prediction accuracy for each metric between the current and previous predictions.
As the numbers show, the results for the current model are better across all the metrics.
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide13.png)

The page at the bottom of the [Model Comparison] tab provides a comparison of degrees of contribution.
The predictive contribution for the current model is on the left, and the predictive contribution for the previous model is on the right.

The details indicate that "Pointed Failure" is the most effective for both the current and the previous model.
The information for the other variables also suggests that the current and previous models used similar variables, for the most part.
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}

![](../img_en/t_slide14.png)

Since you now know that the current model generates better results, let's use it to do a failure type classification prediction
on the actual data that you want to predict. The [Predict] button in the upper right allows you to make a prediction.
{{% /div_slide %}}
