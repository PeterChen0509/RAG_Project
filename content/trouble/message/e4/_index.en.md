---
title: "Data cannot be read because the time interval is not constant for many data items."
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["time series mode", "interval", "constant interval"]
---

{{% h4_error_cause %}}
When the time stamps included in the time information variables of the variable to be predicted specified in the time series prediction mode are arranged along time, time series prediction cannot be performed if there are many places where the time interval between data is not constant.

{{% h4_error_avoid %}}
Make sure that the time stamp interval in the time information variables of the variable to be predicted specified in the time series prediction mode is constant.
