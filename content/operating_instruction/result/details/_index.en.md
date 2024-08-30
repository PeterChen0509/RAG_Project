---
title: "Accuracy Detail Screen"
date: 2018-12-29T11:02:05+06:00
lastmod: 2023-06-10T10:42:26+06:00
weight: 2
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Predictions and Results", "Graph", "Figure", "Plot"]
---

Click the Accuracy Details tab to go to this screen.

![](../../img_en/t_slide26.png)

{{% div_method_area "Check the description of the evaluation value of prediction accuracy" %}}
{{% step_n_area2 1 "Place the cursor on the name of the evaluation value for prediction accuracy." %}}
![](../../img_en/t_slide41.png)

Displays a description of each evaluation value.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "View graphs and tables of prediction accuracy" %}}
{{% step_n_area2 1 "Check each graph in the area below the evaluation value." %}}
![](../../img_en/t_slide42.png)

The type of graph displayed depends on the prediction type.
For example, for binary classification, a graph of a confusion matrix or distribution of predicted probabilities is displayed.

The type of graph displayed depends on the prediction type. See also Tips on how to check prediction accuracy.
{{% div_relitem %}}

- {{% a_in "../../../tips/eval_bin/" "Summary of the prediction accuracy (binary classification)"%}}
- {{% a_in "../../../tips/eval_mul/" "Summary of the prediction accuracy (multiclass classification)"%}}
- {{% a_in "../../../tips/eval_reg/" "Summary of the prediction accuracy (regression)"%}}
- {{% a_in "../../../tips/timeseries/" "Time Series Prediction"%}}
  {{% /div_relitem %}}
  {{% /step_n_area2 %}}
  {{% /div_method_area %}}

{{% div_method_area "Viewing Predicted and Actual Values Graphs (Time Series Mode Only)" %}}
{{% step_n_area2 1 "Check each graph in the area below the evaluation value." %}}
![](../../img_en/t_slide57.png)

If you are using the time series mode, a graph is displayed that compares the actual and predicted values for the future predicted values from a point in time.
For example, the figure above compares the actual values and predicted values for a 1 to 3 month prediction from 2019/04 (April 2019).

![](../../img_en/t_slide58.png)

The "Predicted and Actual Values" graph shows how stable the future prediction is.
For example, the figure above compares what the prediction would look like if one month ahead and two months ahead were repeated.

For information on viewing each graph, see the "{{% a_in "../../../tips/new_features/timeseries/" "Time series forecast"%}}" page in the tips.

{{% cloud_only %}}
![](../../img_en/t_slide127.png)

When upturn/downturn prediction is enabled, upturn/downturn prediction values are also rendered in the graph, in addition to the comparison of predictions and results.
{{% /cloud_only %}}

{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Saving the displayed content as an image" %}}
{{% step_n2 1 "Click the Save Image button. " %}}
{{% step_n2 2 "Specify the name of the folder in which to save the images. The displayed content is saved as an image (png). " %}}
{{% /div_method_area %}}

{{% desktop_only %}}
{{% div_method_area "Save in CSV format" %}}
![](../../img_en/t_slide76.png)
{{% step_n2 1 "Click Save in CSV format " %}}
{{% step_n2 2 "Specify the location to save the CSV file. The confusion matrix is saved as a CSV file." %}}
{{% /div_method_area %}}
{{% /desktop_only %}}
