---
title: "Evaluation Result Screen"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Evaluation Summary", "Sort"]
---

This screen allows you to check evaluation results, such as the prediction accuracy of the learned prediction models.
The evaluation performs a prediction on the learned prediction model for data not used for learning.
Evaluates prediction accuracy by comparing predicted results with correct answers.
For each prediction type (Binary classification, multiclass classification, and regression), information is displayed.
You can toggle the display by clicking Model Summary, Accuracy Details, Contribution Details, and Model Settings.

![](../../img_en/t_slide24.png)

{{% div_method_area "Understand an overview of prediction accuracy" %}}
{{% step_n_area2 1 "See prediction accuracy summary." %}}
Displays the key accuracy metrics for each prediction type, along with the levels of prediction accuracy and their descriptions.
The more stars, the better the prediction accuracy level.
If it is judged that the accuracy is improved by increasing the amount of data, that fact is displayed as text.

If the accuracy is good, a link to the utilization method of this model will be displayed. 
If there are points that need improvement, a button will be displayed to the "Hints" tab where you can check the improvement methods.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Understand the overview of contributions" %}}
{{% step_n_area2 1 "See the contribution summary." %}}
For each input variable, it shows how important the learned prediction model is and whether it is effective for prediction.
The longer the bar graph, the greater the importance and effectiveness.
The most important and effective variables have a significant impact on the prediction results.
The two colors indicate the importance and effectiveness of each value in the case of binary classification.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Saving the displayed content as an image" %}}
{{% step_n2 1 "Click the Save Image button. " %}}
{{% step_n2 2 "Specify the name of the folder in which to save the images. The displayed content is saved as an image (png). " %}}
{{% /div_method_area %}}

{{% div_method_area "View details of the contribution" %}}
{{% step_n_area2 1 "Click the [Contribution details] button." %}}
![](../../img_en/t_slide25.png)
{{% /step_n_area2 %}}
{{% /div_method_area %}}
