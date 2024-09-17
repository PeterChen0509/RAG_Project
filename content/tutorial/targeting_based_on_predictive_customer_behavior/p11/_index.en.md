---
title: "Prediction"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 11
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

![](../img_en/t_slide15.png)

Select the prediction dataset on this screen. Let's review the prediction data used in this tutorial.
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide16.png)

The prediction model is used to predict the purchase probability for customers who have not purchased premium services (Approximately 1,600 rows).
In this tutorial, you will use sample data that has been prepared for prediction.
Unlike the prediction model creation (training) data, variables with or without premium service purchase are not used.

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/Marketing_Service_Purchase_Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide17.png)

Specify the prediction data `2_プレミアムサービス購入（予測用）.csv` here.<br/>
{{% desktop_only %}}
You can import data by dragging and dropping it into the window or by [Select a File].<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
Click "Select from Uploaded Data" and select the sample data from the data list on the "Samples" tab.
{{% /cloud_only %}}

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/Marketing_Service_Purchase_Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide21.png)

The prediction dataset preview is displayed.
Predict "Premium Service (target)" displayed as "?"  from information such as "Registration Date" and "Age".

{{% desktop_only %}}
Click [Result Preview].
{{% /desktop_only %}}
{{% cloud_only %}}
Click "Run Prediction". Wait a while until the preview screen of the prediction result is displayed.
{{% /cloud_only %}}
{{% /div_slide %}}

{{% div_slide "Step 5" normal %}}
![](../img_en/t_slide22.png)

{{% desktop_only %}}
Please specify "Customer ID" in [Add the following variables to the first column].

Click [Predict and Save].
Make a prediction for each row and save the results.

After clicking [Predict and Save], the Save As dialog appears.
Specify a file name and save the prediction result.
{{% /desktop_only %}}
{{% cloud_only %}}
Please specify "Customer ID" in [Add the following variables to the first column].
Click "Save Prediction Results", enter "File name" and click "Save".
{{% /cloud_only %}}
{{% /div_slide %}}

{{% div_slide "Step 6" normal %}}
When the prediction is complete, the following screen is displayed and the prediction results are saved in the specified file.

![](../img_en/t_slide23.png)

Predicted results are output in the following format (this format may vary depending on the option settings).
For each customer, a prediction probability of premium service purchase is calculated.

![](../img_en/t_slide19.png)
{{% /div_slide %}}
