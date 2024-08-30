---
title: "Valid variable selection"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8500
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["データ結合", "項目選択", "過学習", "特徴選択"]
---

{{% cloud_only_info %}}
Data Join is available for the {{% a_in "../desktop /" "desktop version"%}} only.
{{% /cloud_only_info %}}

**Valid variable selection** refers to the selection of variables from the set of input variables in the prediction model that are valid for the prediction target.

Because the number of variables in the data is larger than the number of rows and this can degrade the accuracy of the prediction model, eliminate variables that are unnecessary for the prediction, select variables that are likely to be relevant to the prediction target, and then create a prediction model.

### Handling of a valid variable selection in Prediction One

Prediction One automatically display a message regarding the automatic selection of additional variables that are valid for prediction when the number of variables in the joined data greatly exceeds the number of rows in a data join.

The variables to be selected are limited to those added or created from the related data. Variables originally included in the training data are not subject to deletion.

Automatic selection of variables that are valid for predicting is done by creating a simple prediction model to evaluate the validity of each variable. Therefore, it is not always more accurate than using all the additional variables.

See also {{% a_in "../../tips/join_dataset/" "Model creation method using data join"%}} for a description of data joins.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/join_dataset/" "Model creation method using data join" %}}
- {{% a_in "../../terminology/join_column/" "Horizontal Join" %}}
  {{% /div_relitem %}}
