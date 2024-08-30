---
title: "Vertical Join"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["Data Join", "join"]
---

{{% cloud_only_info %}}
Data Join is available for the {{% a_in "../desktop /" "desktop version"%}} only.
{{% /cloud_only_info %}}

In a data join, **Vertical Join** refers to a data join method that joins training data to related data in a row.

Prediction One performs a vertical join if the related data variable names match the training data variable names exactly.
Vertical joins increase the number of rows of training data.

See also {{% a_in "../../tips/join_dataset/" "Model creation method using data join"%}} for a description of data joins.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/join_dataset/" "Model creation method using data join" %}}
- {{% a_in "../../terminology/join_additional_column/" "Additional Variables (Data Join)" %}}
- {{% a_in "../../terminology/join_column/" "Horizontal Join" %}}
  {{% /div_relitem %}}
