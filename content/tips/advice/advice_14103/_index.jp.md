---
title: "寄与度が非常に小さい項目を除外しましょう"
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
  ["ヒント","改善ヒント","tips",精度改善","寄与度"]
toc: true
---

### 説明

項目数が多いと予測には十分ですが、寄与度が非常に小さい項目があると、予測精度は低下してしまう可能性があります。
この場合は、寄与度が非常に小さい項目を除外して予測モデルを再作成し、精度が改善するか確認しましょう。

![](../img/t_slide11.png)

### 関連資料

- {{% a_in "./../../../terminology/imbalance/" "データの偏り・不均衡なデータ" %}}
- {{% a_in "./../../../operating_instruction/create_model/select_target_detail/" "モデル設定画面（詳細）" %}}
