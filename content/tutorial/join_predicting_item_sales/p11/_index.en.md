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

![](../img_en/t_slide19.png)

Select the prediction dataset on this screen. Let's review the prediction data used in this tutorial.
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide20.png)
![](../img_en/t_slide21.png)

Using the prediction model that you created, you predict the sales amount for the products (about 100 types) for which the arrival number is not decided.<br/>
In this tutorial, you will use sample data that has been prepared for prediction.
Unlike the data for creating a prediction model (training), the variable for the sales amount is not used.

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/SalesManagement_Product_Sales_Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide22.png)

Specify the prediction data `3_売上情報（予測用）.csv` here.<br/>
{{% desktop_only %}}
You can import data by dragging and dropping it into the window or by [Select a File].<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
Click "Select from Uploaded Data" and select the sample data from the data list on the "Samples" tab.
{{% /cloud_only %}}

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/SalesManagement_Product_Sales_Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide23.png)

Then specify the related data.

The related data for this tutorial also includes related information about the products and sales channel you are predicting,
Select [Reuse Data Used to Create Models]<br/>
Related data has been added and associated with the prediction data.

![](../img_en/t_slide24.png)

Click "Next".

{{% /div_slide %}}

{{% div_slide "Step 5" normal %}}
![](../img_en/t_slide25.png)

Displays a preview of the combined prediction data.

Predict "Sales Amount (target)" displayed as "?"  from information such as "Sales Channel ID".

{{% desktop_only %}}
Click [Result Preview].
{{% /desktop_only %}}
{{% cloud_only %}}
Click "Run Prediction". Wait a while until the preview screen of the prediction result is displayed.
{{% /cloud_only %}}
{{% /div_slide %}}

{{% div_slide "Step 6" normal %}}
![](../img_en/t_slide26.png)

{{% desktop_only %}}
Please specify "Sales ID" in [Add the following variables to the first column].

Click [Predict and Save].
Make a prediction for each row and save the results.

After clicking [Predict and Save], the Save As dialog appears.
Specify a file name and save the prediction result.
{{% /desktop_only %}}
{{% cloud_only %}}
Please specify "Sales ID" in [Add the following variables to the first column].
Click "Save Prediction Results", enter "File name" and click "Save".
{{% /cloud_only %}}
{{% /div_slide %}}

{{% div_slide "Step 7" normal %}}
When the prediction is complete, the following screen is displayed and the prediction results are saved in the specified file.

![](../img_en/t_slide27.png)

Predicted results are output in the following format (this format may vary depending on the option settings).
The predicted sales amount by sales channel is calculated for each product.

![](../img_en/t_slide28.png)
{{% /div_slide %}}