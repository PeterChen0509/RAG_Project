---
title: "Detailed Dataset Specifications"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2
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
---

### Notes on creating datasets for binary and multiclass classification

Prediction One reads the first {{% t_read_row_num%}} rows of the file to determine how many values for the variables you want to predict (in the above example, there are two types, "Continuation" and "Withdrawal"). If the variable to be predicted is a character string, binary or multiclass classification is determined according to the determined unique number.
If you want to perform binary classification, make sure that the <u>first {{% t_read_row_num%}} row contains two values for the variable you want to predict</u>. If you want to perform multiclass classification, sort the first {{% t_read_row_num%}} row so that there are at least three possible values for the variable you want to predict. Also, note that <u>you cannot use more than {{% t_mul_max_class%}}</u>.

### Handling of missing values

Missing values are <u>unrecorded data</u>.
Use an empty string if there is a missing value.

### Size of the training data

Prepare training data with 100 to 1 million rows and 2 to 999 columns. For Time Series Prediction Mode, prepare training data with 20 to 10,000 rows and 2 to 200 columns. When using data join, prepare the training data so that the total number of columns of the training data and the related data does not exceed 200 columns.

As the number of rows and columns increases, the learning time and memory usage increases. If the memory usage exceeds the capacity of your PC, the software may terminate.

{{% a_id "timestamp-format" %}}

### Date and Time Format

Variables whose data type is date and time must be prepared in the following format: The dates and times that can be used are from 0:0 on January 1, 1970 to 23:59 on December 31, 3999. Seconds data may be present, but it is not used by Prediction One. (y = year, M = month, d = day, H = hour, m = minute, s = second)

- `yyyy-MM-dd HH:mm:ss`
- `yyyy-MM-dd HH:mm`
- `yyyy-MM-dd H:mm:ss`
- `yyyy-MM-dd H:mm`
- `yyyy-MM-dd`
- `yyyy-MM-d HH:mm:ss`
- `yyyy-MM-d HH:mm`
- `yyyy-MM-d H:mm:ss`
- `yyyy-MM-d H:mm`
- `yyyy-MM-d`
- `yyyy-M-dd HH:mm:ss`
- `yyyy-M-dd HH:mm`
- `yyyy-M-dd H:mm:ss`
- `yyyy-M-dd H:mm`
- `yyyy-M-dd`
- `yyyy-M-d HH:mm:ss`
- `yyyy-M-d HH:mm`
- `yyyy-M-d H:mm:ss`
- `yyyy-M-d H:mm`
- `yyyy-M-d yyyy/MM/dd HH:mm:ss`
- `yyyy/MM/dd HH:mm`
- `yyyy/MM/dd H:mm:ss`
- `yyyy/MM/dd H:mm`
- `yyyy/MM/dd`
- `yyyy/MM/d HH:mm:ss`
- `yyyy/MM/d HH:mm`
- `yyyy/MM/d H:mm:ss`
- `yyyy/MM/d H:mm`
- `yyyy/MM/d`
- `yyyy/M/dd HH:mm:ss`
- `yyyy/M/dd HH:mm`
- `yyyy/M/dd H:mm:ss`
- `yyyy/M/dd H:mm`
- `yyyy/M/dd`
- `yyyy/M/d HH:mm:ss`
- `yyyy/M/d HH:mm`
- `yyyy/M/d H:mm:ss`
- `yyyy/M/d H:mm`
- `yyyy/M/d`
- `yyyy-MM`
- `yyyy-M`
- `yyyyMMdd`
- `yyyyMM`
- `dd-MM-yyyy`
- `dd-M-yyyy`
- `d-MM-yyyy`
- `d-M-yyyy`
- `yyyy`
- `mmm-yy` (`mmm` is the English abbreviation for the month name. For example, `Jan-21` represents `2021年1月`. In this format, when the current year and month are `yyyy年mm月`, only data within `(yyyy-80)年(mm+1)月～(yyyy+20)年(mm)月` and within `1970年1月～3999年12月` can be used).
