---
title: "F-score"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: "F-score is a scale to check whether Recall and Precision are well balanced."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["F-score", "F-score", "fvalue"]
---

**F-score** is a scale to check whether {{% a_in "../recall/" "Recall"%}} and {{% a_in "../precision/" "Precision"%}} are well balanced. The bigger, the better, at best 100%. It is expressed by the following formula:

- F-value = (2 x Precision x Recall) / (Precision + Recall)

For example, if "(a) Withdrawal" is set as the prediction value, and the following confusion matrix is obtained,

{{% div_confmat twoclass %}}

|         | (a) Withdrawal | (b) Continuation |
| :------ | :-----: | :-----: |
| (a) Withdrawal |    4    |    5    |
| (b) Continuation |    6    |    7    |

{{% /div_confmat %}}

Recall and Precision are calculated as

- Recall = 4/(4+6)= 40%
- Precision = 4/(4+5) = 44.4%

  From this result, the F-score is

- F-value = (2 x Precision x Recall)/(Precision + Recall) = approximately 0.421

and 42.1% is displayed.

{{% div_relitem contents-bottom %}}

- {{% a_in "../recall/" "Recall" %}}
- {{% a_in "../precision/" "Precision" %}}
- {{% a_in "../confusion_matrix/" "Confusion Matrix" %}}

{{% /div_relitem %}}
