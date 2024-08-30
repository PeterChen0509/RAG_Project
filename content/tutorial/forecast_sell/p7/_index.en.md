---
title: "Creating a Prediction Model"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 7
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

![](../img_en/t_slide4.png)

The main screen appears, no prediction model has been created, so it is empty. Click [Create New Prediction Model].
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide5.png)

Specify `1_販売台数.csv`, the data for creating a prediction model (training).<br/>
{{% desktop_only %}}
You can import data by dragging and dropping it into the window or by [Select a File].<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
Click "Select from Uploaded Data" and select the sample data from the data list on the "Samples" tab.
{{% /cloud_only %}}
{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/Production Control_Improve manufacturing planning through sales volume prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide6.png)

This screen is displayed when data loading is completed.<br/>
Please select one variable to predict.
For this tutorial, select the variable "Sales Volume (Prediction Target)".
After selecting, click the "Next" button.<br/>
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide7.png)

In this tutorial, we will look at the monthly sales volume and Nikkei Stock Average through March 2019 and predict how much we expect to sell in the future.
Click "Use the time series prediction mode" and then click "Next".
{{% /div_slide %}}

{{% div_slide "Step 5" normal %}}
![](../img_en/t_slide8.png)

On this screen, set the period for which you want to predict the sales volume.

Suppose you have data up to 2019/03, and you want to predict the sales volume from 2019/04 to 2020/03. Specify that you want to predict from "a month from now" to "12 months from now" in the prediction interval.

The figure shows the period that you will be creating a model to predict for. Once you have made sure that the period is set to "2019/04/01" to "2020/03/01," click [Create Prediction Model].

![](../img_en/t_slide22.png)

You could also configure variables other than the variable to be predicted, but we'll go with "Set Automatically" here.

{{< notice note >}}
For details on the settings, see {{% a_in "../../../tips/new_features/timeseries_features/" "Variables other than the variable to be predicted" %}}.<br/>
The tutorial for setting variables individually can be found {{% a_in "../../forecast_the_number_of_visitors/" "here" %}}.
{{</ notice >}}

{{% /div_slide %}}

{{% div_slide "Step 6" normal %}}
![](../img_en/t_slide9.png)

Please wait until the learning begins. The processes for Preprocessing → Prediction Model Training → Accuracy Evaluation are executed.<br/>
The estimated wait time is displayed at the top. The more data you have, the longer it takes.<br/>
When you have completed your learning, click the [Completed] button.<br/>
{{% /div_slide %}}
