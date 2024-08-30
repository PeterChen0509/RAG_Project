---
title: "Failed to build model for series X."
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
# weight: カテゴリごとにまとめる
weight: 1000
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["Series"]
---

{{% h4_error_cause %}}
The variable you want to predict for a particular series is missing. If time information for a particular series is missing, this message will be displayed during learning.

{{% h4_error_avoid %}}
Make sure that there is no missing data in the data for the failed series.
