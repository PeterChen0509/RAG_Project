---
title: "Join Key Variable"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2400
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["data join" , "join key"]
---

{{% cloud_only_info %}}
Data Join is available for the {{% a_in "../desktop /" "desktop version"%}} only.
{{% /cloud_only_info %}}

In a data join, **join key variable** are variables with common values that represent the correspondence between the training data and the related data.
When you {{% a_in "../../terminology/join_column/" "horizontal join"%}} the related data, the join process is performed by looking for a match in the values of the join key variable.

### Handling a Join Key Variable in Prediction One

![](../../operating_instruction/img_en/t_slide61.png)

When related data is added in the data join screen, Prediction One automatically judges the join key variable of the training data and related data, and displays the join relation.
In automatic judgment, a judgment is made based on the matching degree of the variable name, data type, and value, and the variable with the highest matching degree is judged as the join key variable.

If a different join key is selected than expected, you can change the join key variable from the Change Join Key Variable pull-down.

Refer to {{% a_in "../../tips/join_dataset/" "Model creation method using data join"%}} for a description of data joins.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/join_dataset/" "Model creation method using data join" %}}
- {{% a_in "../../terminology/join_column/" "Horizontal Join" %}}
  {{% /div_relitem %}}
