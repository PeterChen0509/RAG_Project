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
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: [""]
tutorial_page:
  is_next_exists: true
---

{{% div_slide "Step 1" normal first-page %}}
![](../img_en/t_slide6.png)
You can create a new model for the model you want to update by clicking the [Update model] button.
Here, we'll update the model we created for the {{% a_in "../../classification_of_fault_information/" "classification of failure information" %}}.
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide7.png)

After clicking [Update model],
select `最新データ_故障情報_2018年以降.csv` in the following folder on the data-entry screen.
{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/Information management_Automatic classification of the latest failure information" %}}
Also select "Latest data does not include old data".
When you select this option, you can use joined data—the data from the last training process together with the latest data that you are entering now—as the data for creating a prediction model (training).

{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide8.png)

On the model settings screen, you can see the settings for the variables that you want to predict from the previous model and the variables for the current model.
Click the [Next] button to proceed to the next screen.

{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide9.png)

Next, specify the evaluation data. Here, the evaluation will use the prediction accuracy for failure information since 2019 as the correct answer.<br/>

First, select "Use the following criteria to extract evaluation data from the data for creating a prediction model (training)". This lets you split the data into two groups—data for creating a prediction model (training) and evaluation data—based on
the specified criteria. The objective here is to ensure that the latest data is evaluated correctly.
{{% /div_slide %}}

{{% div_slide "Step 5" normal %}}
![](../img_en/t_slide10.png)

Specify the range of values for the evaluation data. Here, our evaluation range will be data where the repair date is January 1, 2019, or later.<br/>

This makes it possible to use data through 2018 as days for creating a prediction model (training) and data since 2019 as evaluation days.
By taking these steps to incorporate the time axis into your prediction, you can perform training and evaluation under problem settings that align well with actual conditions.
{{% /div_slide %}}

{{% div_slide "Step 6" normal %}}
![](../img_en/t_slide18.png)
Finally, you can create your prediction model by clicking the [Create prediction model] button.
{{% /div_slide %}}
