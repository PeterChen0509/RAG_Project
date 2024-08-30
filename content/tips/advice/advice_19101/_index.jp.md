---
title: "データに時系列性がある場合は評価用データを手動で指定しましょう"
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

データに時系列性がある場合、評価用データは手動で指定すると評価結果の信頼性が高くなります。

Prediction Oneでは、評価用データが指定されておらず、かつ、予測モデル作成用データが501行以上の場合、予測モデル作成用データからランダムで10%が評価用データとして自動的に抽出されます。
ただし、データに時系列性がある場合、ランダムで10%抽出してしまうと、未来の情報を用いて過去を予測することになり、評価結果の信頼性は低くなります。
予測モデル作成前の詳細設定画面で、「評価用データを指定」することで、手動で評価データを指定することができます。

![](../img/t_slide.png)


