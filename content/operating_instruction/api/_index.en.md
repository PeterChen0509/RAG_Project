---
title: "API Specifications"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1
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
    "API",
    "REST API",
  ]
---

### API List

| No.  | Category    |  API Name     | Function Overview              |
| :--- | :--------- | :--------- | :------------------  |
|1 | Learning | {{% a_in "../train_api/api_key/" "Get API Key"%}} | Retrieve the API key|
|2 | Learning | {{% a_in "../train_api/train_data_upload/" "Train Data Upload"%}} | Upload the data set for training|
|3 | Learning | {{% a_in "../train_api/train/" "Train"%}} |Create a prediction model|
|4 | Learning | {{% a_in "../train_api/train_status_check/" "Train Status Check"%}} | Retrieve the status of training|
|5 | Retraining | {{% a_in "../re_train_api/re_train_data_upload/" "Retrain Data Upload"%}} | Execute retraining for a created model|
|6 | Retraining | {{% a_in "../re_train_api/re_train_status_check/" "Retrain Status Check"%}} | Retrieve the status of retraining|
|7 | Retraining | {{% a_in "../re_train_api/switch_model/" "Retrain Model Switch"%}} | Switch the API created model|
|8 | Prediction | {{% a_in "../model_api/inference/" "Inference"%}}  | Perform prediction on prediction data with created model|

For information on the relationship between each API, see the figure below.

![](../img_en/t_slide109.png)


