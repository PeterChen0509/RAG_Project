---
title: "予測値 (二値分類) "
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
keywords: ["予測値", "ポジティブ"]
---

Prediction One では二値分類において、予測したい方の値のことを「**予測値**」と呼びます。

たとえば、「(a)退会」「(b)継続」のどちらになるかを予測したい時に<u>「(a)退会」を予測値として設定すると</u>、結果として得られる混同行列は以下のようになります。

{{% div_confmat twoclass %}}

|         | (a)退会 | (b)継続 |
| :------ | :-----: | :-----: |
| (a)退会 |    4    |    5    |
| (b)継続 |    6    |    7    |

{{% /div_confmat %}}

反対に、<u>「(b)継続」を予測値として設定すると</u>、結果として得られる混同行列は以下のようになります。

{{% div_confmat twoclass %}}

|         | (b)継続 | (a)退会 |
| :------ | :-----: | :-----: |
| (b)継続 |    7    |    6    |
| (a)退会 |    5    |    4    |

{{% /div_confmat %}}

予測値をどちらするかによって混同行列が変わるため、混同行列から計算される、

- <a href="../precision/index.html">Precision</a>
- <a href="../recall/index.html">Recall</a>
- <a href="../f_value/index.html">F 値</a>

の結果も変化します。
