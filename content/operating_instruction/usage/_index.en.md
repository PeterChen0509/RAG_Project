---
title: "Usage Screen"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 10
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  [
    "Document status",
    "Number of models",
    "Data storage capacity",
    "Training run time",
    "Trained",
    "In training",
    "Upper limit",
  ]
---

Clicking the "Usage" button takes you to this screen.

![](../img_en/t_slide73.png)

{{% div_method_area "Check the number of models and their limits" %}}
{{% step_n2 1 "Check the "Number of Models"." %}}
Creating a model increases the number of models by one. Models are counted separately for personal and shared use (which can be shared to the same tenant's account). You cannot create more than the maximum number of models. If the limit is about to be exceeded, delete the unused models.

{{% div_method_area "Check the data storage capacity and its limit" %}}
{{% step_n2 1 "Check the "Data Storage Capacity"." %}}
The total amount of uploaded files is counted. Personal and shared (can be shared to the same tenant's account) are counted separately. If the total file size exceeds the limit, you will not be able to upload or share files.

{{% div_method_area "Check the execution time and its limit" %}}
{{% step_n2 1 "Check the "Execution Time"." %}}
The calculation time accumulates as the model is created. It is reset to zero when the month changes. In the free trial, the calculation time is counted without being reset even if the month changes. If the limit is exceeded, the model cannot be created.

{{% div_method_area "Check which models are being trained" %}}
{{% step_n2 1 "Click the "Training" tab on the right side of the screen to display a list of unconfirmed models that are currently being trained or have completed training." %}}
{{% step_n2 2 "Click a model to go to the model details." %}}

{{% div_method_area "Check which models are API created" %}}
{{% step_n2 1 "Click the "Create API" tab on the right side of the screen to display a list of API created models." %}}
{{% step_n2 2 "Click a model to go to its API Creation Screen." %}}

