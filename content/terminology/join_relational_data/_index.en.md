---
title: "Related Data"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["data join" , "Relational"]
---

{{% cloud_only_info %}}
Data Join is available for the {{% a_in "../desktop /" "desktop version"%}} only.
{{% /cloud_only_info %}}

In a data join, **Related Data** refers to data that has information relevant to the training data.

### Handling of Related Data in Prediction One

Prediction One allows you to join related data by {{% a_in "../../terminology/join_column/" "horizontal join"%}} and {{% a_in "../../terminology/join_row/" "vertical join"%}}.
The related data must be directly joined with the training data.
You cannot join related data.

Please refer to {{% a_in "../../tips/join_dataset/" "Model creation method using data join"%}} for a description of data joins.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/join_dataset/" "Model creation method using data join" %}}
- {{% a_in "../../terminology/join_column/" "horizontal join" %}}
- {{% a_in "../../terminology/join_row/" "vertical join" %}}
  {{% /div_relitem %}}
