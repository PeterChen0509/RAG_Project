---
title: "評価結果の信頼性を高めるために「交差検証」の設定を試しましょう"
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
  ["ヒント","改善ヒント","tips",]
toc: true
---

### 説明

学習用データが少ない場合、評価用データに含まれる値により予測しやすさが変わり、評価結果が不安定になることがあります。
この場合、「交差検証」の設定をすることで、予測モデルの作成時間が長くなりますが、評価結果の信頼性を高めることができます。

![](../img/t_slide.png)

### 関連資料

- {{% a_in "./../../../terminology/cross_validation/" "交差検証" %}}

