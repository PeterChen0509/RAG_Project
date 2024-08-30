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

![](../img_en/t_slide7.png)

The main screen appears, no prediction model has been created, so it is empty. Click [Create New Prediction Model].
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide8.png)

{{% desktop_only %}}
Specify `1_来店数.csv`, the data for creating a prediction model (training).<br/>
You can import data by dragging and dropping it into the window or by [Select a File].<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
Specify `v1.8/1_来店数.csv`, the data for creating a prediction model (training).<br/>
Click "Select from Uploaded Data" and select the sample data from the data list on the "Samples" tab.
{{% /cloud_only %}}

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/StoreManagement_Store_Visits_Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide9.png)

This screen is displayed when data loading is completed.<br/>
Please select one variable to predict.
For this tutorial, select the variable "Number of store visits (Prediction target)".
After selecting, click the "Next" button.<br/>
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide10.png)

For this tutorial, we'll use our store traffic records up to 2019/09/15 to predict how many store visits we expect.

Click "Use the time series prediction mode" and then click "Next".{{% /div_slide %}}

{{% div_slide "Step 5" normal %}}
![](../img_en/t_slide11.png)

Set whether you want to predict "number of store visits" or "when".

Suppose you have data up to 2019/09/15, and you want to predict store visits between the following day (9/16) and two weeks in the future (9/29).**Specify the prediction interval as "One day ahead" through "14 days from now".**

You can check the period that you will be creating a model to predict for.**Confirm that the period is September 16, 2019, to September 29, 2019**.

<hr/>

![](../img_en/t_slide29.png)
![](../img_en/t_slide30.png)

Also configure the variables other than the variable to be predicted.

This time, let's assume that the temperature, weather, and vacation flag information for the period September 16, 2019, to September 29, 2019 is obtained from weather reports and calendar information.
Let's also assume that website access count data for September 16, 2019, to September 29, 2019 will not be obtained until that time.<br/>
In cases like this where related information for a prediction time in the future can be obtained, **select the check boxes of the individual settings for the temperature, weather, and vacation flags**.
**Do not select the check box for the website access count**, as it will not be obtained.

For details on the settings, see {{% a_in "../../../tips/new_features/timeseries_features/" "Variables other than the variable to be predicted" %}}.

When you have finished selecting the check boxes, click [Create prediction model].


{{% /div_slide %}}

{{% div_slide "Step 6" normal %}}
![](../img_en/t_slide12.png)

Please wait until the learning begins. The processes for Preprocessing → Prediction Model Training → Accuracy Evaluation are executed.<br/>
The estimated wait time is displayed at the top. The more data you have, the longer it takes.<br/>
When you have completed your learning, click the [Completed] button.<br/>
{{% /div_slide %}}
