---
title: "Horizontal Join"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8500
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["data join" , "coupling" , "joins"]
---

{{% cloud_only_info %}}
Data Join is available for the {{% a_in "../desktop /" "desktop version"%}} only.
{{% /cloud_only_info %}}

In a data join, **horizontal join** is a data join method that increases the number of variables (increases the column direction of the file).

In Prediction One, if the join key variable values in the related data do not overlap (are unique), a horizontal join is performed by matching each row with the join key value and copying the variables.

Join key for related data. If there is a duplicate variable value, summarize the related data information by various aggregation methods, such as average or unique number of variable values.
For more information about the different summary functions, refer to {{% a_in "../../terminology/join_additional_column/" "Additional Variables (Data Join)"%}}.

See also {{% a_in "../../tips/join_dataset/" "Model creation method using data join"%}} for a description of data joins.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/join_dataset/" "Model creation method using data join" %}}
- {{% a_in "../../terminology/join_additional_column/" "Additional Variables (Data Join)" %}}
- {{% a_in "../../terminology/join_row/" "Vertical Join" %}}
  {{% /div_relitem %}}
