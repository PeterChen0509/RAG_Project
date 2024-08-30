---
title: "Creating a Prediction Model1:  Input data for creating a prediction model (learning)"
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

Specify `1_売上情報.csv`, the data for creating a prediction model (training).<br/>
{{% desktop_only %}}
You can import the prediction model creation (training) data by dragging and dropping it into the window or by [Select a File].<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
Click "Select from Uploaded Data" and select the sample data from the data list on the "Samples" tab.
{{% /cloud_only %}}

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/SalesManagement_Product_Sales_Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide9.png)

This screen is displayed when data loading is completed.<br/>
Please select one variable to predict. For this tutorial, select the variable "Sales amount (Prediction target)"<br/>
After making your selection, click the checkbox for **Advanced settings** in the upper right to enter Advanced mode.<br/>

![](../img_en/t_slide10.png)
Click the **Data Join button** at the bottom right of the advanced setting mode screen.

{{% /div_slide %}}
