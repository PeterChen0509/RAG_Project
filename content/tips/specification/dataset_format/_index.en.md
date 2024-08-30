---
title: "Dataset"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1
draft: false
# metaタグのパラメータ
meta:
  description: "Describes the dataset formats available in Prediction One and the corresponding problem settings. You can easily create classification, regression and time series models."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  ["Dataset", "Timestamp", "Format", "Data type", "Type"]
toc: true
---

### Dataset Formats

The data format is tabular data, and the file formats are CSV (comma-separated) and TSV (tab-separated).

Each row corresponds to one sample (a single piece of data is called a sample. For example, in customer data, it refers to customers), and each column (variable) corresponds to an attribute of the sample (e.g., age, gender, etc.). The first row of the data file contains column names (variable names), and the second and subsequent rows contain sample information. Each row must have the same number of variables.

The variable to be predicted (for example, continue or withdraw) is one of the variables in the file. For an example of a dataset, see the figure below. The variable to be predicted is "Continuation and withdrawal". Please refer to the enclosed sample data as an example.

![](../img_en/t_slide4.png)

### Variable Data Types

The following data types are available: You can only specify text or numeric values for binary or multiclass classification, and numeric values for regression.

| Data type | Description                                               |
| :----------: | :------------------------------------------------- |
|    String    | Categorical value (e.g., the "gender" variable above)             |
|   Text   | Text (Text written in Japanese or English)         |
|     Numeric value     | Integer, decimal, or other number (e.g., the "past purchases" variable above) |
|     Date/time     | Date and time (e.g., the "registration date" variable above)               |

### Date and Time Format

The date and time data included between 0:0 on January 1, 1970 and 23:59 on December 31, 3999 can be read and used as datetime data. To read datetime data, the format of the datetime data must be consistent. For example, the following data can be read as datetime data.

| Date/time data description | Example                                                        |
| :--------------: | :------------------------------------------------------------ |
|   Year data   | "2019"                                                      |
|   Month data   | "2019-6" "201906"                                          |
|   Day data   | "2019/6/12" "2019-6-12" "20190612" "2019/06/12 00:00:00" |
| Hour/minute data | "2019/06/12 03:00:00" "2019-06-12 21:30:00"                |


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
