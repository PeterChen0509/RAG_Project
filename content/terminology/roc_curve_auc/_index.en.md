---
title: "ROC curve and AUC"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["ROC", "AUC", "ROCAUC", "Sensitivity", "Curve", "Receiver operating characteristic"]
---

**ROC curve** (Receiver Operating Characteristic curve) is a curve drawn using the prediction probability given by the prediction model for binary classification. A solid yellow line in the graph indicates an ROC curve.

If the prediction model is making random predictions, the ROC curve will overlap the diagonal from lower left to upper right (dashed line on graph). The more the ROC curve swells to the upper left, the better the prediction model. It is difficult to understand the shape of the curve in detail, so it is a good idea to judge the quality of the model based on the size of the AUC.

![](../img_en/t_slide35_tmp_roc.png)

**AUC** (Area Under the Curve) is one of the metrics indices for binary classification. Refers to the area under the ROC curve (yellow areas). The bigger, the better, at best 100%. The AUC value is 50% when the prediction model predicts randomly, and approaches 100% when the model predicts very accurately.

Unlike Accuracy, Recall, Precision, and F-score, AUC is not affected by the threshold value for obtaining the prediction result from the prediction probability, so it is often used as an evaluation value for the prediction accuracy of binary classification.

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/result/eval_bin/" "How to read prediction accuracy (binary classification)"%}}
  {{% /div_relitem %}}
