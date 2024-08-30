---
title: "Join Data Input Screen"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2
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
---

When you create a learning model using the data join feature,
click the [Predict] button to go to this screen.
Use this screen to specify additional related data for the data you want to predict.

![](../../img_en/t_slide67.png)

{{% div_method_area "Add related data for predicting" %}}
{{% step_n_area2 1 "Input related data for the prediction." %}}
To make predictions in a model that uses the data join feature, you must also specify the related data during the prediction.
Refer to What is Data Join? to create prediction data.
The file formats are CSV (comma separated values) and TSV (tab separated values).
The prediction data variables must match the related data when the selected prediction model was created.

{{% /step_n_area2 %}}
{{% step_n2 2 "Drag and drop prediction related data to this screen, or specify a file to enter it." %}}
{{% /div_method_area %}}

{{% div_method_area "Add the same related data that you used to create the model" %}}
You can also use the related data that you used to create the model for the prediction.
{{% step_n_area2 1 "Select [Reuse Data Used to Create Models]" %}}
The file used during learning is embedded in the related data display.
Of the files that were added when the prediction model was created, only the data of the horizontal join is taken over. Vertical join data is not taken over.

{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Preview prediction data" %}}
{{% step_n_area2 1 "Click [Next]" %}}
The display changes to the preview screen.
The Next button is not enabled if no related data is specified.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Specify the prediction data again" %}}
{{% step_n2 1 "Click the Back button." %}}
{{% /div_method_area %}}

{{% div_method_area "Close prediction window" %}}
{{% step_n2 1 "Click the [Close] button. " %}}
{{% /div_method_area %}}
