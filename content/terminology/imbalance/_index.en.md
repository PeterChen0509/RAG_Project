---
title: "Imbalanced Data"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4400
draft: false
# metaタグのパラメータ
meta:
  description: "Imbalanced Data is a condition in which there is a significant bias in the frequency of appearance of each variable in the column that you want to predict when you perform classification."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["imbalance", "Imbalanced Data", "Balance", "Balance between classes"]
---

**Imbalanced** means a state where there is a large bias in the frequency of appearance of each variable contained in the column to be predicted when classification is performed.

For example, the "{{% a_in "../../tutorial/crm_predict_unsubscribe/" "Churn prediction" %}}" tutorial involves binary classification of whether customers fall into "(a) Withdrawal" or "(b) Continuation", and if there are 10 customers who fall under "(a) Withdrawal" and 1000 customers who fall under "(b) Continuation", then there is a bias in the variable to be predicted.
If data with bias in the column to be predicted is used for learning, it is possible to create a prediction model in which "(a) Withdrawal" is difficult to predict.

If there is a bias in the column you want to predict and you want to predict a variable with a particularly low frequency of occurrence, checking "Correct imbalance in the column you want to predict" in the advanced setting screen makes it easier to predict values with a low frequency of occurrence.
However, this option may reduce the classification accuracy. Also, this option may not improve prediction accuracy for data with fewer occurrences.

{{% div_relitem contents-bottom %}}

- {{% a_in "../classification/" "Classification" %}}
- {{% a_in "../recall/" "Recall" %}}
- {{% a_in "../precision/" "Precision" %}}
- {{% a_in "../confusion_matrix/" "Confusion Matrix" %}}
- {{% a_in "../../operating_instruction/create_model/select_target_detail/" "Model Settings Screen (Details)" %}}

{{% /div_relitem %}}
