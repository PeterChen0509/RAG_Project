---
title: "再現率（Recall）"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 3100
draft: false
# metaタグのパラメータ
meta:
  description: "再現率（Recall）は、予測モデルで予測して見つけたいデータのうち、実際に予測を当てることができた割合を示しています。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
---

二値分類のユースケースによっては、分類したい２つの値の一方の値の検出に興味がある場合があります。
たとえば、機器の故障を事前に予測して故障を防ぎたい場合では、
故障しないことの予測よりも、故障することをいかに予測して防げるかが重要になります。
一方の検出に重点をおいた精度評価値が、Precision、再現率（Recall）、F 値です。

**再現率（Recall）** は、予測モデルで予測して見つけたいデータのうち、実際に予測を当てることができた割合を示しています。

![](../img/t_slide24.png)

たとえば、この図の混同行列では「購入あり」である 20+10 のデータのうち 20 個を予測して当てることができています。
この場合、再現率（Recall）は (20/(20+10)) = 0.66 となります。

{{% div_relitem contents-bottom %}}

- {{% a_in "../precision/" "精度 (Precision) " %}}
- {{% a_in "../binary_classification/" "二値分類" %}}
- {{% a_in "../multiclass_classification/" "多値分類" %}}
- {{% a_in "../../tips/result/eval_bin/" "予測精度の概要（二値分類）" %}}
  {{% /div_relitem %}}
