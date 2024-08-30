---
title: "Training API Specifications"
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

| No.  |  API Name     | Function Overview              |
| :--- | :--------- | :------------------  |
|1 | Get API Key| Retrieve the API key.|
|2 | Train Data Upload| Upload the data set for training.|
|3 | Train| Create a prediction model.|
|4 | Train Status Check| Retrieve the status of training.|

For information on the method for retrieving a secret key, see the "{{% a_in "secret_key/" "Retrieving a Secret Key"%}}" page.

For information on the relationship between each API, see the figure below.

![](../img_en/t_slide109.png)


