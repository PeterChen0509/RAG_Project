---
title: "Software Update History (Desktop version)"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1000 # 一番下に表示する
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
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

{{% notice tip "../../operating_instruction/setting/feedback/index.html" "About sending feedback" %}}
If you have any likes or dislikes or suggestions for improvement regarding Prediction One functions, please send a message from the send feedback screen. We will use it for future product development.
{{% /notice %}}

### version 3.2 (2023/01)

- Added the {{% a_in "../../tips/new_features/help/" "in-app help feature" %}}.
- Added the {{% a_in "../../tips/new_features/advice/" "accuracy-improvement hint feature" %}}.

### version 3.1 (2022/10)

- Added the Favorites feature.
  - Clicking the "Add to Favorites" button for a model on the {{% a_in "../../operating_instruction/result/model_list/" "Model List Screen" %}} pins the corresponding model to the top of the list.
- You can now {{% a_in "../../operating_instruction/result/importance/" "output contribution to a CSV file" %}}.
- Added processing methods to the {{% a_in "../../tips/specification/custom/" "Data Preparation feature" %}}.
  - Adding "Other" to strings: Replace strings that occur infrequently
  - Replacing portions of strings: Replace only a portion of a given string
  - Unifying similar strings: Unify strings with similar notation
  - Splitting strings: Split strings by a specified symbol or character
  - Combining variables: Combine two variables into one
  - Deleting low-correlation variables: Delete variables based on correlation coefficients
  - Deleting rows that satisfy certain conditions: Delete rows meeting specified conditions
  - Deleting rows containing missing data: Delete rows containing missing data
  - Deleting duplicate rows: Delete all duplicate rows except one
- {{% a_in "../../tips/new_features/score/" "Relevance score" %}} is now displayed on the Prediction Model Creation Screen.
- You can now specify how you want to use {{% a_in "../../tips/new_features/timeseries_features/" "variables other than the variable to be predicted in a time series prediction" %}}.
- You can now open the manual from an error message screen.
- UI and usability improvements.

### version 3.0 (2022/05)

- Added the Data Preparation feature. With the {{% a_in "../../tips/new_features/dataprep_custom/" "Data Preparation feature" %}}, users can combine methods for processing data as they choose.
- UI and usability improvements.

### version 2.3 (2021/11)

- You can now {{% a_in "../..//operating_instruction/result/model_list/" "export/import" %}} prediction models.
- You can now use the {{% a_in "../../tips/new_features/model_update/" "Model Update" %}} feature to update models with the latest data and compare them with the current models.
- Added a feature for specifying evaluation data based on variable conditions (splitting data for creating [training] prediction models and evaluation data based on specified numeric or date/time values ranges).
- You can now perform classifications of up to 200 classes in multiclass classification (as opposed to the original 20 classes).
- You can now {{% a_in "../..//operating_instruction/result/details/" "save confusion matrices in multiclass classifications in CSV format" %}} via the details for multiclass classification evaluation results.
- Reduced memory usage.
- UI and usability improvements.

### version 2.2 (2021/03)

- You can now create prediction models by {{% a_in "../../tips/new_features/join_dataset/" "combining data" %}} from multiple files.
- You can now {{% a_in "../..//operating_instruction/create_model/select_target_detail/" "correct bias in the variables you want to predict" "imbalanced-data" %}}.
- You can now display contribution in time series mode.
- UI and usability improvements.

### version 2.1 (2020/11)

- You can now specify the number of divisions for cross-validation.
- You can now {{% a_in "../../operating_instruction/result/model_list/" "output prediction results for evaluation data" "output-result" %}} to see which data was used for the evaluation.

### version 2.0 (2020/08)

- Redesigned to improve UI and usability.
- You can now create prediction models more easily.
- Improved the way you specify output in the prediction screen.
- Project list view has been changed to model folder list view.

### version 1.4 (2020/04)

- Improved time series prediction mode (multiple series support, addition of evaluation result graph).
- Improved time remaining display during training/predicting.
- For regression, improvements have been made to speed up the creation of prediction models.
- UI and usability improvements.

### version 1.3 (2020/01)

- Added time series forecasting mode to regression.
- Support for more timestamp formats.You can check the supported formats from {{% a_in "../../tips/specification/dataset_format/" "More detailed specifications of the dataset" "timestamp-format" %}}.
- Improvements have been made to improve the performance of regression, binary classification and multiclass classification.
- UI and usability improvements.

### version 1.2 (2019/09)

- Added the function to save the display content as an image.
- Added tutorials/tips to the project list screen.
- Added configuration/reasoned prediction of multiclass classification contribution.
- Improved handling of Japanese and English texts.
- UI and usability improvements.

### version 1.1 (2019/06)

- First release.
