---
title: "Data cannot be imported because there are rows with a different number of variables."
date: 2018-12-29T11:02:05+06:00
lastmod: 2024-05-30T14:48:14+09:00
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
keywords: ["Number of variables", "Cannot read", "Cannot read"]
---

{{% h4_error_cause %}}
You may get this message if the file specified for prediction model creation (training) data/prediction data contains rows with a different number of variables.

{{% h4_error_avoid %}}
Make sure that the number of variables in all rows of the prediction model creation (training) data is equal to the number of variables in the first row of the prediction model creation (training) data.
