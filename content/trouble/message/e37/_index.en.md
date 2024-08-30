---
title: "This join is likely to be mismatched. Please check the variable."
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
keywords:
  [
    "Click Create Prediction Model to join the selected variables.",
    "check variables",
  ]
---

{{% h4_error_cause %}}
This message is displayed when there is a high possibility that data cannot be joined on the data join screen.

Data joining is the process of joining rows that contain identical values (Refer to {{% a_in "../../../tips/new_features/join_dataset/" ""Data Joining"" %}}).
Therefore, this message is displayed when the same value cannot be found at all or contains a large amount of notation.

{{% h4_error_avoid %}}
Make sure that the files to be joined contain common variables and values.
