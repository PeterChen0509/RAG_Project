---
title: "When creating a dataset, if there are values that cannot be retrieved (in the presence of a missing value), how should I record the data?"
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
keywords: ["Missing value"]
---

The missing part should be blank (please write an empty string). This is true for all data types.

Also, if a variable you want to predict is missing, the data in that row is not used to train or evaluate the prediction model.
