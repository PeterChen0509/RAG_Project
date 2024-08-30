---
title: "Other Specifications"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1000
draft: false
# metaタグのパラメータ
meta:
  description: "This section describes the data formats that can be used with Prediction One and how to handle missing values."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  ["Dataset", "Timestamp", "Format", "yymmdd", "Size", "Upper limit"]
toc: true
---

### Notes on creating datasets for binary and multiclass classification

Prediction One reads the first {{% t_read_row_num%}} rows of the file to determine how many values for the variables you want to predict (in the above example, there are two types, "Continuation" and "Withdrawal"). If the variable to be predicted is a character string, binary or multiclass classification is determined according to the determined unique number.
If you want to perform binary classification, make sure that the <u>first {{% t_read_row_num%}} row contains two values for the variable you want to predict</u>. If you want to perform multiclass classification, sort the first {{% t_read_row_num%}} row so that there are at least three possible values for the variable you want to predict. Also, note that <u>you cannot use more than {{% t_mul_max_class%}}</u>.

### Handling of missing values

Missing values are <u>unrecorded data</u>.
Use an empty string if there is a missing value.

### Size of prediction model creation (training) data

Prepare prediction model creation (training) data with 100 to 1 million rows and 2 to 200 columns. For Time Series Prediction Mode, prepare prediction model creation (training) data with 20 to 10,000 rows and 2 to 200 columns. When using data join, prepare the prediction model creation (training) data so that the total number of columns of the prediction model creation (training) data and the related data does not exceed 200 columns.

As the number of rows and columns increases, the learning time and memory usage increases. If the memory usage exceeds the capacity of your PC, the software may terminate.

{{% a_id "timestamp-format" %}}
