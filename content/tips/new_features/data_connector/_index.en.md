---
title: "Data Connector Feature"
date: 2023-06-15T11:00:00+06:00
lastmod: 2023-06-15T11:00:00+06:00
weight: 22
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Data connector", "External data"]
---

{{% div_slide "What is the data connector feature?" normal first-page %}}
The ability to transfer specified files to Prediction One via Amazon S3 provided by Amazon Web Services (AWS) has been added.
Previously, models were created by manually downloading csv files from Amazon S3 and uploading the data to Prediction One.
The addition of this data connector feature will eliminate the time and effort previously required for this task, thereby improving work efficiency. Plans are in place to gradually expand connectivity to the public cloud in the future.

{{% /div_slide %}}

{{% div_slide "What is the data connector feature?" normal %}}
Input the connection information.
If temporary credentials are used, also enter the "Access Token".
![](img_en/t_slide1.png)
A list of files is now displayed.
Click the Transfer button.
![](img_en/t_slide2.png)
{{% /div_slide %}}

{{% div_slide "Summary" summary %}}
This document has given an overview of the data transfer method of the data connector feature.
Here are the key points:

- The data connector feature allows transfer of datasets stored in external services.

{{% /div_slide %}}
