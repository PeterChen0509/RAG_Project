---
title: "予測したい項目に含まれる値の中に、出現回数が少なすぎるものがあるため、予測モデルを作成できません・予測ターゲットのユニーク数が少なすぎます"
date: 2024-06-03T13:15:15+09:00
lastmod: 2024-06-03T13:15:15+09:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["予測したい項目", "予測ターゲット", "出現回数", "ユニーク数", "データ", "少なすぎる"]
---

{{% h4_error_cause %}}
自動評価データ抽出や交差検証を行う分類系モデルの学習において、学習データとして分割されたデータ内に出現する予測したい項目の種類の数が少ない場合に発生することがあります。  

{{% h4_error_avoid %}}
予測したい項目に出現するラベルの種類の出現数に大きく偏りのある場合は、どのラベルも同程度の数が含まれるようにデータを準備します。  
入力する学習データの並び順をランダムに並び替えたり、交差検証の分割数を少なくすると、このエラーを回避できることがあります。  
それでも回避ができない場合は、あらかじめ評価データを手動で分割し、評価データを指定してモデル作成を行うことでエラーを回避することができます。  