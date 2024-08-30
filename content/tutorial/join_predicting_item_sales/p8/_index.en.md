---
title: "Creating a Prediction Model 2 : Import related data"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8
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

![](../img_en/t_slide11.png)

Click the [Data Join] button to launch the animation window for the data join. Click the [Go to Data Join] button.
Moves to the data join screen.

![](../img_en/t_slide12.png)

Specify the related data `2_関連_チャネル情報.csv` and `2_関連_商品情報.csv`.<br/>
You can drag and drop them into the window or import them from the "Add Data" button.<br/>

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/SalesManagement_Product_Sales_Prediction" %}}
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide13.png)

When the data import is complete, two related pieces of data are added to the screen.
The Join Key variables that map the prediction model creation (training) data to the related data are also displayed.<br/>
Make sure that the Join Key variables are selected correctly and click the "Create Predictive Model" button.<br/>
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide14.png)

Please wait until the learning begins. Four processes are executed: Preprocessing → Prediction Model Learning → Accuracy Evaluation → Predictive Contribution Analysis.<br/>
The estimated wait time is displayed at the top. The more data you have, the longer it takes.<br/>
When you have completed your learning, click the [Completed] button.<br/>
{{% /div_slide %}}
