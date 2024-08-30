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

Specify the data for creating a prediction model (training) `1_Customer feedback.csv` here.<br/>
{{% desktop_only %}}
You can import data by dragging and dropping it into the window or by [Select a File].<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
Click [Select from Uploaded Data] and select the sample data from the data list on the [Samples] tab.
{{% /cloud_only %}}
{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/CRM_Review_Classification" %}}
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide9.png)

This screen is displayed when data loading is completed.<br/>
Please select one variable to predict. After selecting (for this tutorial, select the item "Complaint Type (Target)"), click the [Create Prediction Model] button.<br/>
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide10.png)

Please wait until the training begins. Four processes are executed: Preprocessing → Prediction Model Training → Accuracy Evaluation → Predictive Contribution Analysis.<br/>
The estimated wait time is displayed at the top. The more data you have, the longer it takes.<br/>
When you have completed your training, click the [Completed] button.<br/>
{{% /div_slide %}}
