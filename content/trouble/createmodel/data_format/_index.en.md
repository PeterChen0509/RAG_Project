---
title: "What is the format of the dataset?"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Format", "tsv", "csv", "xlsx", "DB"]
---

The data format supports tabular data, and the file formats support CSV (Comma Separated) and TSV (Tab Separated).

Each row corresponds to one sample (a single piece of data is called a sample. For example, in customer data, it refers to customers),  and each column (variable) corresponds to an attribute of the sample (e.g., age, gender, etc.). The first row of the data file contains column names (Variable name), and the second and subsequent rows contain sample information. Each row must have the same number of variables. Use an empty string if there is a missing value. There are four data types available: string, text, numeric, and datetime. However, you can only specify text or numeric values for binary or multiclass classification, and numeric values for regression.

Prediction One reads the first {{% t_read_row_num%}} row of the file to determine how many values for the variable you want to predict. If the variable to be predicted is a character string, binary or multiclass classification is determined according to the determined unique number. If you want to perform binary classification, make sure that the first {{% t_read_row_num%}} row contains two values for the variable you want to predict. If you want to perform multiclass classification, sort the first {{% t_read_row_num%}} row so that there are at least three possible values for the variable you want to predict. In addition, please note that the above categories {{% t_mul_max_class%}} are not supported. For a specific example, see {{% a_in "../../../tips/specification/dataset_format/" "Detailed specifications" %}}.
