---
title: "How do I specify my own evaluation data?"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Evaluation data", "Valid", "Test", "Myself"]
---

When no evaluation data is specified, Prediction One randomly selects samples contained in the prediction model creation (training) data (a single piece of data is called a sample. For example, in customer data, it refers to customers), to create the evaluation data.
If you are creating your own evaluation data, please follow the steps below to import your prediction model creation (training) data.

{{% step_n_area 1 %}}
Load prediction model creation (training) data.
{{% /step_n_area %}}

{{% step_n_area 2 %}}
Please check "Advanced Settings" on the prediction model creation screen.

![](../../img_en/t_slide5.png)
{{% /step_n_area %}}

{{% step_n_area 3 %}}
Move to the lower left of the screen and click "Select a File" in "Set another file".

![](../../img_en/t_slide7.png)
{{% /step_n_area %}}

{{% step_n_area 4 %}}
Specify the file you want to use as evaluation data in the "Specify a File" window.
{{% /step_n_area %}}
