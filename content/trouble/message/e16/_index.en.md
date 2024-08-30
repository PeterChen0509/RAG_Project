---
title: "Too much missing data for the variable you want to predict."
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
# weight: カテゴリごとにまとめる
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Missing data"]
---

{{% h4_error_cause %}}
Prediction One automatically removes rows from the prediction model creation (training) data that are missing (empty) for the variable to be predicted.
If a sufficient amount of data is not obtained as a result of removal, it may not be possible to proceed with learning.

{{% h4_error_avoid %}}
For rows where the variable you want to predict is missing (empty), enter the value of the variable you want to predict.
Alternatively, add data that does not have missing values for the variable to be predicted to the prediction model creation (training) data.
