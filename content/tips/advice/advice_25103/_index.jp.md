---
title: "特定の条件でデータを絞ってから予測モデルを再作成しましょう"
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
  ["ヒント","改善ヒント","tips","精度改善"]
toc: true
---

### 説明

データ全体では予測精度が低くても、ある特定の条件で絞ったデータでは予測精度が高い場合、特定の条件でデータを絞ってから予測モデルを作成することで、精度が改善する可能性があります。<br/>
例えば、売上予測を行う際に、地域が日本とアメリカの両方を含んでいる場合、日本の予測だけでも精度が高ければ、日本のデータに絞って予測モデルを作成しましょう。

