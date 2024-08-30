---
title: "The variables in the training data and evaluation data must match exactly / The variables in the training data and prediction data must match exactly"
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
keywords: ["Exact match", "Do not match"]
---

{{% h4_error_cause %}}
The prediction model is created to calculate the prediction value for the variable to be predicted using the variables included in the prediction model creation (training) data.
Therefore, if the evaluation data does not include the variables used in the prediction model creation (training) data, the prediction cannot be calculated and a prediction model cannot be created.

In addition, the prediction model performs predictions based on rules learned from the model creation data, etc.
As such, all variables in the model creation data and the prediction data must match.

{{% h4_error_avoid %}}
Match the variables in the prediction model creation (training) data and evaluation data (the names of the variables on the first line of the data file).

<br/>
<br/>
<br/>

#### Examples
To predict customer withdrawal, assume the following data:

- Date of last login to the service
- Customer's contract plan
- Flag if the customer has withdrawn

 
If you want to create a predictive model that predicts the "flag if the customer has withdrawn" based on the "date of last login to the service" and the "customer's contract plan", you need to prepare the following data.

- Training data: "Date of last login to the service", "customer's contract plan", "flag if the customer has withdrawn"
- Evaluation data: "Date of last login to the service", "customer's contract plan", "flag if the customer has withdrawn"
- Prediction data: "Date of last login to the service", "customer's contract plan"

