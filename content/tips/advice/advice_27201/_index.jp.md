---
title: "精度が改善しきらなくても業務に活用する方法をご紹介します (二値分類)"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4
draft: false
# metaタグのパラメータ
meta:
  description: "予測分析ツールPrediction Oneが提案する精度改善のための改善ヒントについて説明するページです。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  ["ヒント","改善ヒント","tips","精度改善","寄与度"]
toc: true
---

### 説明

予測精度が悪い場合でも、一部の予測については活用できる場合があります。<br/>
例えば、予測確率が高い順に並び替えたとき上位10%程度であれば、精度良く予測できている可能性があります。

以下の画像は{{% a_in "./../../../tutorial/targeting_based_on_predictive_customer_behavior/" "顧客行動予測に基づいたターゲティング" %}}での予測結果です。
このうち購入ありの確率が高い順番に並び替えて、上位のみをビジネスアクションに繋げると、全体の精度が悪かったとしてもビジネスアクションに繋げた顧客については精度が良い可能性があります。

![](../img/t_slide22.png)

### 関連資料

- {{% a_in "./../../../tutorial/targeting_based_on_predictive_customer_behavior/p13/" "顧客リストの作成" %}}

