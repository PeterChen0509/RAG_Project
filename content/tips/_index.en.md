---
title: "Tips/Specifications"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
description: "This section summarizes tips on how to create data sets and how to read prediction accuracy, as well as the specifications of each feature."
type: "docs"
weight: 3
---

The "Tips" section provides a collection of useful information and pointers for using Prediction One.

## How to Create Datasets
Methods of creating datasets.
{{% a_in "./how_to_create_dataset/" "How to create datasets" %}}

## Information on New Features
About features added in the new version.

- {{% a_in "./new_features/contribution_csv/" "Output predictive contribution in csv format" %}}
- {{% a_in "./new_features/timeseries/" "Time series prediction" %}}
 - {{% a_in "./new_features/timeseries_features/" "Time series prediction mode: Variables other than the variable to be predicted" %}}
- {{% a_in "./new_features/join_dataset/" "Data join" %}}
- {{% a_in "./new_features/model_update/" "Update model" %}}
- {{% a_in "./new_features/model_monitor/" "Monitor model" %}}
- {{% a_in "./new_features/dataprep_custom/" "Data preparation feature" %}}
- {{% a_in "./new_features/score/" "Relevance score" %}}
- {{% a_in "./new_features/advice/"  "Accuracy improvement hint feature" %}}
- {{% a_in "./new_features/help/" "In-app help feature" %}}
- {{% a_in "./new_features/quick_guide/" "Quick guide" %}}
- {{% a_in "./new_features/prediction_interval/" "Upturn/downturn prediction" %}}
- {{% a_in "./new_features/data_connector/" "Data connector feature" %}}


## How to Read Prediction Accuracy and Utilize Results
For details on how to read prediction accuracy and contribution:

- {{% a_in "./result/contribution/" "How to read the predictive contribution" %}}
- {{% a_in "./result/eval_bin/" "How to read prediction accuracy (binary classification)" %}}
- {{% a_in "./result/eval_mul/" "How to read prediction accuracy (multiclass classification)" %}}
- {{% a_in "./result/eval_reg/" "How to read prediction accuracy (regression)" %}}
- {{% a_in "./result/improve_model/" "To improve prediction accuracy" %}}
- {{% a_in "./result/use_result/" "How to utilize prediction results" %}}

## Using Accuracy-Improvement Hints
How to use the hints for improving accuracy.

- {{% a_in "./advice/" "List of hints for improving accuracy" %}}

## Specification Details
About the specifications for each feature of Prediction One.

- {{% a_in "./specification/dataset_format/" "Dataset formats" %}}
- {{% a_in "./specification/dataset_for_timeseries/" "Datasets for time series prediction mode" %}}
- {{% a_in "./specification/custom/" "Processing methods for each data preparation feature" %}}
