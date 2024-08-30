---
title: "Additional Variables (Data Join)"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4300
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["data join" , "Additional variables" , "Aggregation" , "Consolidation"]
---

{{% cloud_only_info %}}
Data Join is available for the {{% a_in "../desktop /" "desktop version"%}} only.
{{% /cloud_only_info %}}

**Additional Variables** in a data join are variables that are newly created using related data when data is {{% a_in "../../terminology/join_column/" "horizontally joined"%}}.

If the join key variable values in the related data overlap, Prediction One combines the related data information into the join data by various aggregation methods, such as average or unique number of variable values, for rows with duplicate join keys.
The number of aggregation methods is automatically determined by Prediction One so that the number of variables in the joined data does not significantly exceed the number of rows.

### Handling additional variables in Prediction One

Prediction One automatically selects some of the following aggregation methods so that the number of variables in the joined data does not exceed the number of rows.

- Candidate for aggregation method for overlapping horizontal joins

If there is a duplicate join key variable value in the related data, Prediction One selects some of the possible aggregation methods set by the data type of the related data variable.

| Type of the related data variable | Candidate for aggregation method |
| --------------------------------- | -------------------------------- |
|              Numeric              |  Count, Average, Max, Min        |
|              String               |  Unique number, Mode             |
|              Datetime             |  Maximum, average time interval  |
|              Text                 |  Average number of characters    |

※ Count refers to the number of rows of related data that correspond to join key variable values with data for creating model data.

- Candidate for aggregation method for overlapping horizontal joins (using date type variables)

If there is a duplicate join key variable value in the related data and the related data has a variable whose data type is Date and Time, an additional aggregation method using time information is added.

| Type of the related data variable | Candidate for aggregation method  |
| --------------------------------- | --------------------------------  |
|               Numeric             |  Oldest value, newest value       |
|               String              |  Oldest value, newest value       |
|               Datetime            |  None                             |
|               Text                |  Oldest value, newest value       |

Variables created by the aggregation method using variables whose data type is date and time are named according to the format of <br> [Aggregation method name] in [Related data variable name] ([date and time variable name])<br>.

Please refer to {{% a_in "../../tips/join_dataset/" "Model creation method using data join"%}} for a description of data joins.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/join_dataset/" "Model creation method using data join" %}}
- {{% a_in "../../terminology/join_column/" "Horizontal Join" %}}
  {{% /div_relitem %}}
