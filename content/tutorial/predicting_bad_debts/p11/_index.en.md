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

The loan default probability is predicted for each borrower (application for pre-assessment) using the created prediction model.
In this tutorial, you will use sample data that has been prepared for prediction.

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/RiskManagement_Bad_Debts_Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide17.png)

Specify the prediction data `2_貸し倒れ（予測用）.csv` here.<br/>
{{% desktop_only %}}
You can import data by dragging and dropping it into the window or by [Select a File].<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
Click "Select from Uploaded Data" and select the sample data from the data list on the "Samples" tab.
{{% /cloud_only %}}

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/RiskManagement_Bad_Debts_Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide21.png)

The prediction dataset preview is displayed.
Predict "bad debt (prediction target)" displayed as "?"  from information such as "Preferred Loan Type", and "Business Profile".

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
For each borrower, a prediction probability of loan default is calculated. This probability can be used in preliminary loan screening.

![](../img_en/t_slide19.png)
{{% /div_slide %}}