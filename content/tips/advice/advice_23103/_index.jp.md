---
title: "項目のデータタイプが数値で適切か確認しましょう"
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


データタイプが数値の場合は、数字の大小関係が予測モデル作成時に考慮されます。一方、IDなど大小関係に意味がない数字の場合は、文字列に変更することで少しでも数字が異なると全く別のものとして扱われます。
文字列の方が適切であれば、データタイプを文字列に変更して予測モデルを再作成すると、精度が改善する場合があります。


![](../img/t_slide.png)

