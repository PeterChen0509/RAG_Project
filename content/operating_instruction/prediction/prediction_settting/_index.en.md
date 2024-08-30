---
title: "Prediction Setting Screen"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4
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

![](../../img_en/t_slide31.png)

{{% div_method_area "Run a prediction and save the prediction results" %}}
{{% step_n2 1 "In the preview of the prediction result, check the content of the prediction result to be output." %}}
{{% step_n2 2 "Click the [Predict and Save] button." %}}
{{% step_n_area2 3 "Specify a file or enter a file name to save the prediction results." %}}
After the file is specified, the prediction is performed on all data contained in the prediction data.
Prediction reasons are also calculated after you click the [Predict and Save] button.

If your prediction data contains a lot of data, this process can take a long time.
In this case, the time remaining to complete the prediction is displayed.
![](../../img_en/t_slide32.png)
Please wait while the prediction completes without closing the prediction window.

{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Add classification results when using binary classification or multiclass classification" %}}
{{% step_n_area2 1 "Please check [Add classification results] in the prediction setting." %}}
When predicting a classification, the prediction model outputs a probability of the prediction value for each prediction value.

If [Add classification results] is checked, the predicted value with the highest probability is selected by comparing the output probabilities, and the predicted value is added to the prediction results.

![](../../img_en/t_slide44.png)
![](../../img_en/t_slide45.png)
For example, in the above figure, the result of comparing the probability of "Purchased" and "No purchase" (in the red frame) is added to the prediction result.
{{% /step_n_area2 %}}
{{% step_n2 2 "Make sure that the classification result is added to the preview of the prediction results." %}}
{{% /div_method_area %}}

{{% div_method_area "Adding Prediction Reasons to the Prediction Results File" %}}
{{% step_n2 1 "Please check [Add a prediction reason] in the prediction setting." %}}
{{% step_n2 2 "Make sure that the prediction reason is added to the preview of the prediction results." %}}
{{% /div_method_area %}}

{{% div_method_area "Add specific variables of prediction data to the file of prediction results" %}}
{{% step_n2 1 "In prediction settings, select one of the variables you want to add from the [Add the following variables to the first column] pull-down." %}}
{{% step_n2 2 "Make sure that the specified variable is added to the preview of the prediction results." %}}
{{% /div_method_area %}}

{{% div_method_area "Add the contents of prediction data to the prediction results file" %}}
{{% step_n2 1 "Check [Add prediction data to the output] in the prediction setting." %}}
{{% step_n2 2 "Make sure that the prediction data is added to the preview of the prediction results." %}}
{{% /div_method_area %}}
