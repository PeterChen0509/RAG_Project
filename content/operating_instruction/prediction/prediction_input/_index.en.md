---
title: "Prediction Data Input Screen"
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
keywords: [""]
---

Click the [Predict] button to go to this screen.
On this screen, you can input the data you want to predict to the prediction model.

![](../../img_en/t_slide29.png)

{{% div_method_area "Make a new prediction" %}}
{{% step_n_area2 1 "Please prepare the prediction data." %}}
To make predictions, you need prediction data.
Create prediction data with reference to How to Make Data.

The file formats are CSV (comma separated values) and TSV (tab separated values).
The prediction data items must match the prediction model creation (training) data when the selected prediction model was created,
except for the items that you want to predict.
{{% /step_n_area2 %}}
{{% step_n2 2 "Drag and drop the prediction data to this screen, or specify a file to enter it." %}}
{{% /div_method_area %}}

{{% div_method_area "Automatically generate prediction data and run the prediction" %}}

<u>Only when learning is performed with the time series prediction mode and [Automatic configuration] set</u>,
the prediction data can be automatically created to perform prediction without entering prediction data manually.
For example, you need to prepare prediction data if you used <u>items other than time information items and the items you want to predict such as a record of weather forecasts when creating the prediction model and configured a record of weather forecasts with [Manual configuration]</u>.

{{% step_n_area2 1 "Select [Automatically generate prediction data] in the prediction data specification method radio button" %}}
![](../../img_en/t_slide54.png)
{{% /step_n_area2 %}}
{{% step_n2 2 "Click [Next]" %}}
{{% step_n_area2 3 "In the preview, check the time for the prediction and click [Predict]." %}}
![](../../img_en/t_slide55.png)
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Close prediction window" %}}
{{% step_n2 1 "Click the [Back] or [Close] button." %}}
{{% /div_method_area %}}
