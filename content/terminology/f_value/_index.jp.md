---
title: "F値"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: "F 値は再現率(Recall)と精度(Precision)がバランスよく良い値になっているかを確認するための尺度です。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["エフチ", "えふち", "fvalue"]
---

**F 値**は{{% a_in "../recall/" "再現率(Recall)" %}}と{{% a_in "../precision/" "精度(Precision)" %}}がバランスよく良い値になっているかを確認するための尺度です。大きければ大きいほど良く、最良で 100%になります。下式で表されます。

- F 値 = (2 x Precision x Recall) / (Precision + Recall)

たとえば、「(a)退会」を予測値と設定した状態で下のような混同行列が得られた場合、

{{% div_confmat twoclass %}}

|         | (a)退会 | (b)継続 |
| :------ | :-----: | :-----: |
| (a)退会 |    4    |    5    |
| (b)継続 |    6    |    7    |

{{% /div_confmat %}}

再現率(Recall)と精度(Precision)は

- 再現率(Recall) = 4/(4+6)= 40%
- 精度(Precision) = 4/(4+5) = 44.4%

と求まります。ここから

- F 値 = (2 x Precision x Recall) / (Precision + Recall) = 約 0.421

となり、42.1%と表示されます。

{{% div_relitem contents-bottom %}}

- {{% a_in "../recall/" "再現率(Recall)" %}}
- {{% a_in "../precision/" "精度(Precision)" %}}
- {{% a_in "../confusion_matrix/" "混同行列" %}}

{{% /div_relitem %}}
