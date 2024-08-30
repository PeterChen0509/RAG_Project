---
title: "The number of unique values contained in the variable to be predicted exceeds the number of values that can be handled by the specified prediction type."
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
keywords: ["Unique values", "Specified prediction type", "200", "Target"]
---

{{% h4_error_cause %}}
When you perform binary or multiclass classification on a variable that you want to predict, the prediction model will fail if it contains values that exceed the criteria.

{{% h4_error_avoid %}}

#### For binary classification

Make sure that the column for the variable you want to predict does not contain more than two types of values, and then modify the prediction model creation (training) data so that it contains only two types.  
If there are more than {{% t_read_row_num%}} rows in the file, sort the data so that all types of data appear before the {{% t_read_row_num%}} row.

#### For multiclass classification

When using multiclass classification as the prediction type, Prediction One allows for a maximum {{% t_mul_max_class%}} types of classification.  
Make sure that the column for the variable you want to predict does not contain more than {{% t_mul_max_class%}} types, and correct the prediction model creation (training) data to only contain {{% t_mul_max_class%}} types.  
