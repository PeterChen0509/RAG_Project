---
title: "Learning Screen"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 5
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
---

Clicking the [Create Model] button, 
takes you to this screen.

![](../../img_en/t_slide23.png)

{{% div_method_area "Check the remaining time" %}}
{{% step_n_area2 1 "Check the remaining time and progress bar." %}}
The estimated time remaining is displayed. There is a possibility that the estimate will be wrong.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% cloud_only %}}
{{% div_method_area "Run learning in the background" %}}
{{% step_n_area2 1 "Click the [Close] button." %}}
The Learning screen closes, but the modeling process is still running in the background. The Model List displays the model you are creating.
{{% /step_n_area2 %}}
{{% step_n_area2 2 "You can check details or predict by clicking on the created model in the model list." %}}
You can also use the "Usage" screen to check which models are learning or have completed learning.
{{% /step_n_area2 %}}
{{% /div_method_area %}}
{{% /cloud_only %}}

{{% div_method_area "Stop Learning" %}}
{{% step_n2 1 "Click the [Cancel] button." %}}
{{% step_n_area2 2 "Click [Discard]." %}}
![](../../img_en/t_slide40.png)
If you click [Cancel], the prediction model continues to learn.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Complete learning and evaluation" %}}
{{% step_n2 1 "When the learning and evaluation process is complete, click the [Completed] button." %}}
{{% /div_method_area %}}

{{% div_method_area "Review learning and evaluation progress" %}}
{{% step_n_area2 1 "Watch the learning and evaluation phase." %}}

During the learning and evaluation phase, you can see what processes are currently being performed.

- Data Import: Imports data from a file and prepares prediction model creation (training) data and evaluation data. It also estimates the processing time.
- Data Preprocessing: Calculates the required statistics for a dataset.
- Model Learning: Learn prediction models from training datasets. Prediction One uses neural networks and gradient boosting decision trees as models to automatically select the best model settings for each.
- Accuracy Evaluation: The evaluation dataset is used to calculate the prediction accuracy of the prediction model created.
- Predictive Contribution Analysis: Analyze the predictive contribution of the prediction model you have created. Not performed when using the time series prediction mode.

The learning and evaluation message displays the details of the process.
{{% /step_n_area2 %}}
{{% /div_method_area %}}
