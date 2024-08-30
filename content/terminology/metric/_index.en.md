---
title: "Accuracy Evaluation"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2500
draft: false
# metaタグのパラメータ
meta:
  description: "Accuracy Evaluation is an evaluation of the performance of predictive models created from the prediction model creation (training) data."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Evaluation value", "Accuracy Evaluation", "Evaluation metric", "Prediction accuracy"]
---

**Accuracy Evaluation** is an evaluation of the performance of prediction models created from prediction model creation (training) data.
Prediction One randomly extracts a portion of the prediction model creation (training) data, creates a prediction model using the remaining data, and makes a prediction on the data extracted earlier.
By comparing the prediction with the correct answer, we evaluate how much we can predict the data that we have never seen before.

You can also specify the data to use for accuracy evaluation by specifying the file from "Specify Data for Evaluation".

Accuracy evaluation metrics depends on the problem setting. See the links below for more information on each metric.

### Evaluation Metrics for Binary Classification

- {{% a_in "../../tips/result/eval_bin/" "Tips [How to read prediction accuracy (binary classification)]" %}}
- {{% a_in "../roc_curve_auc/" "AUC" %}}
- {{% a_in "../accuracy/" "Accuracy" %}}
- {{% a_in "../precision/" "Precision" %}}
- {{% a_in "../recall/" "Recall" %}}
- {{% a_in "../f_value/" "F-score" %}}

### Evaluation Metrics for Multiclass Classification

- {{% a_in "../../tips/result/eval_mul/" "Tips [How to read prediction accuracy (multiclass classification)]" %}}
- {{% a_in "../accuracy/" "Accuracy" %}}
- {{% a_in "../precision/" "Precision" %}}
- {{% a_in "../recall/" "Recall" %}}
- {{% a_in "../f_value/" "F-score" %}}

### Evaluation Metrics for Regression

- {{% a_in "../../tips/result/eval_reg/" "Tips [How to read prediction accuracy (regression)]" %}}
- {{% a_in "../mean_absolute_error/" "Mean Absolute Error" %}}
- {{% a_in "../rmse/" "RMSE" %}}
- {{% a_in "../median_absolute_error/" "Median Absolute Error" %}}
- {{% a_in "../median_absolute_error_ratio/" "Median Absolute Error Ratio" %}}
- {{% a_in "../r2/" "Coefficient of Determination" %}}
