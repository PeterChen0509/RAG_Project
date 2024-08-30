---
title: "Prediction Value (binary classification) "
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
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Prediction Value", "Positive"]
---

In Prediction One, the value you want to predict is called **Prediction Value** in binary classification.

For example, if you wanted to predict which would be "(a) Withdrawal" or "(b) Continuation" and <u>you set "(a) Withdrawal" as the prediction value</u>, the resulting confusion matrix would be:

{{% div_confmat twoclass %}}

|         | (a) Withdrawal | (b) Continuation |
| :------ | :-----: | :-----: |
| (a) Withdrawal |    4    |    5    |
| (b) Continuation |    6    |    7    |

{{% /div_confmat %}}

Conversely, <u>if you set "(b) Continuation" as a prediction value</u>, the resulting confusion matrix is:

{{% div_confmat twoclass %}}

|         | (b) Continuation | (a) Withdrawal |
| :------ | :-----: | :-----: |
| (b) Continuation |    7    |    6    |
| (a) Withdrawal |    5    |    4    |

{{% /div_confmat %}}

Since the confusion matrix changes depending on which prediction value is used, it is calculated from the confusion matrix.

- <a href="../precision/index.html">Precision</a>
- <a href="../recall/index.html">Recall</a>
- <a href="../f_value/index.html">F-value</a>

also changes the result.
