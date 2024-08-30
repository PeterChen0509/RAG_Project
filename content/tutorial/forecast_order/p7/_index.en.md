---
title: "Creating a Prediction Model"
date: 2023-06-15T11:02:05+06:00
lastmod: 2023-06-15T10:42:26+06:00
weight: 7
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
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

Specify `1_注文数.csv`, the data for creating a prediction model (training).<br/>
{{% desktop_only %}}
You can import data by dragging and dropping it into the window or by [Select a File].<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
Click [Select from Uploaded Data] and select the sample data from the data list on the "Samples" tab.
{{% /cloud_only %}}
{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/Production Control_Prevent Overstocking and Shortages through Order Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide6.png)

This screen is displayed when data loading is completed.<br/>
Please select one variable to predict.
For this tutorial, select the variable "Number of orders (Prediction target)".
After selecting, click the [Next] button.<br/>
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide7.png)

In this tutorial, we'll use the number of orders per month through March 2019 and Nikkei Stock Average values to predict future order volume and also the corresponding upturn and downturn.
Click [Use the time series prediction mode] and then click [Next].
{{% /div_slide %}}

{{% div_slide "Step 5" normal %}}
![](../img_en/t_slide8.png)

On this screen, set the period for which you want to predict the "number of orders".

Suppose you have data up to 2019/3, and you want to predict the number of orders from 2019/4 to 2020/3. Specify that you want to predict from "1 month from now" to "12 months from now" in the prediction period.

The figure shows the period that you will be creating a model to predict for: April 1, 2019, to March 1, 2020.

![](../img_en/t_slide9.png)

You could also configure variables other than the variable to be predicted, but we'll go with "Set Automatically" here.

{{< notice note >}}
For details on the settings, see {{% a_in "../../../tips/new_features/timeseries_features/" "Variables other than the variable to be predicted" %}}.<br/>
The tutorial for setting variables individually can be found {{% a_in "../../forecast_the_number_of_visitors/" "here" %}}.
{{</ notice >}}

![](../img_en/t_slide10.png)
You can also enable or disable the feature for "Upturn/downturn prediction". If you disable it, the prediction will follow the process for normal time series prediction mode, which does not generate upturn/downturn prediction results. Since we want to predict upturn and downturn in this case, though, select "Enable". If a horizontal range is visible in the prediction period graph, upturn/downturn prediction is enabled.

Once you completed these setup steps, click [Create Prediction Model].

{{% /div_slide %}}

{{% div_slide "Step 6" normal %}}
![](../img_en/t_slide11.png)

Please wait until the training begins. The processes for Preprocessing → Prediction Model Training → Accuracy Evaluation are executed.<br/>
The estimated wait time is displayed at the top. The more data you have, the longer it takes.<br/>
When you have completed your training, click the [Completed] button.<br/>
{{% /div_slide %}}
