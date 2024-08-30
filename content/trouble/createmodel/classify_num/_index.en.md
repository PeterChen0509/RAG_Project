---
title: "How do I set up to categorize numeric data?"
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
keywords: ["Classification", "Numeric values", "Settings"]
---

To treat multiple numeric values such as 1, 2, and 3 as a classification problem instead of regression, set them as follows:

{{% step_n 1 "Load the target dataset." %}}
{{% step_n 2 "Please check [Advanced Settings] on the prediction model creation screen." %}}
![](../../img_en/t_slide5.png)

{{% step_n 3 "Change Prediction Type to \"multiclass classification\" or \"binary classification.\"" %}}
![](../../img_en/t_slide6.png)

{{% step_n 4 "Click [Create Model]" %}}
