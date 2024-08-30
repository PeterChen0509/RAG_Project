---
title: "Missing Value"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2400
draft: false
# metaタグのパラメータ
meta:
  description: "For example, when there is an unanswered item in a survey, the actual value is unknown or not recorded, and is called [Missing]."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Missing Value", "Missing", "Null character", "missing value", "Blank space"]
---

**Missing** refers to situations in which the actual value is unknown, such as when there are unanswered items in a survey.

**Missing value** refers to the value used to indicate missing status.

### Handling of missing values in Prediction One

#### When items used for learning are missing

Prediction One creates a prediction model by giving the missing data a "missing" status.
So, for example, sales data for a product <u>is treated differently</u> if sales are recorded as "`0円`" than if sales are not known and "" (it is blank because the value is unknown).
In general, a better prediction model can be created if there is less information missing for items related to the item you want to predict.

#### When the item you want to predict is missing

If some of the items you want to predict are missing, Prediction One removes the missing data and learns and evaluates the prediction model.
Keep in mind that if the item you want to predict contains too many missing values, you may not be able to create a prediction model.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../trouble/message/e16/" "Messages [Too much missing data for the item you want to predict]" %}}
- {{% a_in "../../tips/specification/dataset_format/" "More detailed specifications of the dataset" %}}
  {{% /div_relitem %}}
