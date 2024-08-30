---
title: "The selected prediction file cannot be used for data joining."
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
keywords: ["join failure"]
---

{{% h4_error_cause %}}
This message appears when you specify a file that cannot be used for data joining.

{{% h4_error_avoid %}}
The file used for predicting must contain the exact same variable names as the training data.
Make sure that the list of variables displayed in Model Settings matches the variables contained in the file you are entering.
