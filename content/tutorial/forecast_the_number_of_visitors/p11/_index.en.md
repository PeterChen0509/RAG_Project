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
![](../img_en/t_slide21.png)

Using the prediction model created, we predict store visits over the next two weeks (2019/09/16 to 09/29).
In this tutorial, you will use sample data that has been prepared for prediction.

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/StoreManagement_Store_Visits_Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 2" normal%}}
![](../img_en/t_slide18.png)

Let's make a prediction with this prediction model.

{{% desktop_only %}}
Specify the prediction data `2_来店数（予測用）.csv` here.<br/>
You can import data by dragging and dropping it into the window or by [Select a File].<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
Specify the prediction data `v1.8/2_来店数（予測用）.csv` here.<br/>
Click "Select from Uploaded Data" and select the sample data from the data list on the "Samples" tab.
{{% /cloud_only %}}
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide19.png)

{{% desktop_only %}}
Previewing imported prediction data  `2_来店数（予測用）.csv`.
{{% /desktop_only %}}
{{% cloud_only %}}
Previewing imported prediction data  `v1.8/2_来店数（予測用）.csv`.
{{% /cloud_only %}}
From now,  we predict the number of store visits (prediction target) displayed as "?".

{{% desktop_only %}}
Click [Result Preview].
{{% /desktop_only %}}
{{% cloud_only %}}
Click "Run Prediction". Wait a while until the preview screen of the prediction result is displayed.
{{% /cloud_only %}}
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide20.png)

{{% desktop_only %}}
It is ready to predict. Click [Predict and Save] to run the prediction.
Specify a file name to save the predicted results, and then run the prediction.
{{% /desktop_only %}}
{{% cloud_only %}}
Click "Save Prediction Results", enter "File name" and click "Save".
{{% /cloud_only %}}
{{% /div_slide %}}


{{% div_slide "Step 5" normal %}}
When the prediction is complete, the following screen is displayed and the prediction results are saved in the specified file.

![](../img_en/t_slide22.png)
{{% /div_slide %}}

{{% div_slide "Step 6" normal %}}

Predicted results are output in the following format (this format may vary depending on the option settings).
The predicted number of visitors is written for each date.

![](../img_en/t_slide23.png)
{{% /div_slide %}}
