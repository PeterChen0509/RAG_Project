---
title: "Time series prediction setting screen"
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

If the time series prediction mode is specified, this screen is displayed.
Use this screen to specify how far ahead the prediction model can predict
and whether prediction interval data is available for variables other than that you wish to predict. 

![](../../img_en/t_slide21.png)

{{% cloud_only %}}
In the cloud version, you can also specify whether to enable upturn/downturn prediction.
![](../../img_en/t_slide126.png)
{{% /cloud_only %}}

{{% div_method_area "Specifying Prediction Start and End Time Periods" %}}
{{% step_n_area2 1 "Select a time period from the prediction From/To pull-down." %}}
You can only predict after learning for the period you specify here.
You can also enter a value directly by checking [Direct input].
Prediction End Time must be greater than or equal to the Prediction Start Time.
If the prediction period is too long for the length of the prediction model creation (training) data,
the prediction period may not be specified or the learning and evaluation process may fail.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Specify the variables that identify a series" %}}
{{% step_n2 1 "Select a variable from the drop-down list to identify the series." %}}
{{% /div_method_area %}}

{{% div_method_area "Set variables other than that you want to predict" %}}
{{% step_n_area2 1 "If obtaining variables other than the one that you want to predict for the time set in the prediction interval (i.e., for the future), set them here." %}}

![](../../img_en/t_slide100.png)

Used for cases where additional information other than time information variables or variables to be predicted have been added as data for training (model creation).<br/>
If prediction interval values are not available for the information you have added, select "Set Automatically".<br/>
If prediction interval values are available for the information you have added, choose from "Set Individually".<br/>
If there is no information added, only "Set Automatically" can be selected.<br/>
For details see {{% a_in "../../../tips/new_features/timeseries_features/" "Variables other than that you want to predict" %}}.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% cloud_only %}}
{{% div_method_area "Set upturn/downturn prediction" %}}
{{% step_n_area2 1 "Click the "Enable" radio button to enable upturn/downturn prediction." %}}
For details on the upturn/downturn prediction feature, see the "{{% a_in "../../../tips/new_features/prediction_interval" "upturn/downturn prediction" %}}" page.
{{% /step_n_area2 %}}
{{% /div_method_area %}}
{{% /cloud_only %}}

{{% div_method_area "Carry out learning and evaluation" %}}
{{% step_n2 1 "Click the [Create Model] button." %}}
{{% /div_method_area %}}
