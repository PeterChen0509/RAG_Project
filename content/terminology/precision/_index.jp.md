---
title: "精度（Precision）"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 3400
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["精度", "Precision", "適合率"]
---

二値分類のユースケースによっては、分類したい２つの値の一方の値の検出に興味がある場合があります。 たとえば、機器の故障を事前に予測して故障を防ぎたい場合では、 故障しないことの予測よりも、故障することをいかに予測して防げるかが重要になります。 一方の検出に重点をおいた精度評価値が、Precision、再現率（Recall）、F 値です。

「故障」か「正常」かの二値分類をする場合において、予測値として「故障」という値を指定したとします。
予測モデルが「故障」と予測したデータの内、実際に「故障」が正解だった割合を<b>精度（Precision）</b>と呼びます。
適合率とも呼ばれます。

{{% a_in "../recall/" "再現率 (Recall) " %}}のページも合わせて参照してください。

{{% div_relitem contents-bottom %}}

- {{% a_in "../recall/" "再現率 (Recall) " %}}
- {{% a_in "../binary_classification/" "二値分類" %}}
- {{% a_in "../multiclass_classification/" "多値分類" %}}
- {{% a_in "../../tips/result/eval_bin/" "予測精度の概要（二値分類）" %}}
  {{% /div_relitem %}}
