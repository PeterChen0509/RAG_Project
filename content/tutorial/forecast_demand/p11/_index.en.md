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

{{% div_slide "Step 1" normal first-page%}}

![](../img_en/t_slide18.png)

By clicking [Next], you can output the predicted shipments for 2020/01 to 2020/12.

If you create a prediction model from "Year and month (time information)", "Product name (series)", "Number of shipments (target)", alone, as in this case, you do not need to specify the prediction data.
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide19.png)

The prediction is ready. Click [Predict].
{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide20.png)

{{% desktop_only %}}
Click [Save] to save the prediction results.
{{% /desktop_only %}}
{{% cloud_only %}}
Click [Save], enter "File name", and click [Save].
{{% /cloud_only %}}

---

When the prediction is complete, the following screen is displayed and the prediction results are saved in the specified file.

![](../img_en/t_slide21.png)
{{% /div_slide %}}

{{% div_slide "Step 4" normal %}}

Predicted results are output in the following format:
The predicted number of shipments is written for each year and month.

![](../img_en/t_slide22.png)
{{% /div_slide %}}
