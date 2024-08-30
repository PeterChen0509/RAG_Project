---
title: "Software Update History (Cloud version)"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1000 # 一番下に表示する
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  [
    "Update Contents",
    "Difference",
    "Last time",
    "Last version",
    "Version",
    "Compared to before",
    "New Features",
    "Add",
    "update",
  ]
---

This is the update history of the manual and software of the previous version.
### version 1.9
- Added the {{% a_in "../../tips/new_features/data_connector/" "Data Connector feature" %}}.
- Added the {{% a_in "../../operating_instruction/train_api/" "Training API" %}}.
- Added {{% a_in "../../tips/new_features/prediction_interval/" "Upturn/Downturn Prediction" %}} to time series prediction.
- Expanded the maximum number of series that can be trained simultaneously in a time series prediction from 20 to 200.
- Added a function for specifying evaluation data according to variable conditions.

### version 1.8
- Added the {{% a_in "../../tips/new_features/quick_guide/" "Quick Guide" %}}.
- You can now specify how you want to use {{% a_in "../../tips/new_features/timeseries_features/" "variables other than the variable to be predicted in a time series prediction" %}}.
- {{% a_in "../../tips/new_features/score/" "Relevance score" %}} is now displayed on the prediction model creation screen.
- You can now open the manual from an error message screen.
- Added the following processing methods to the {{% a_in "../../tips/specification/custom/" "Data Preparation feature" %}}.
  - Converting data for time series prediction: Convert files in certain formats to formats that can be used in time series predictions
  - Splitting numerical data into bins: Split numerical data into a specified number of sections
  - Deleting low-correlation variables: Delete variables based on correlation coefficients

### version 1.7
- Added the {{% a_in "../../tips/new_features/dataprep_custom/" "Data Preparation feature" %}}.
- Added the {{% a_in "../../tips/new_features/help/" "In-app Help feature" %}} and {{% a_in "../../tips/new_features/advice/" "Accuracy-Improvement Hint feature" %}}.

### version 1.6
- Added the following features: Specifying the number of divisions for cross-validation, setting thresholds for prediction probability when evaluating/predicting binary classification, exporting evaluation data, changing the maximum number of classifications for multiclass classification to 200, displaying contributions in time series prediction mode.

### version 1.5
- Added the Model Monitoring feature.
- Updated the designs of the API management tab and usage dialogs.

### version 1.4
- Added the Retraining API for API created models.
- Added the feature for importing models from the desktop version.

### version 1.3
- Added the Prediction API and Create API features.

### version 1.2 (2021/05)

- First release.
