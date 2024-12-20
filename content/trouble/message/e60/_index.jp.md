---
title: "前回の学習データに今回指定された範囲の評価データ期間が含まれています"
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
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["モデル更新", "評価データ", "含まれる"]
---

{{% h4_error_cause %}}
今回使用するデータのみを使用してモデル更新を行う場合において、今回の評価データ抽出条件が前回モデル作成時の評価データ抽出条件よりも範囲が広くなると、前回の学習データが今回の評価データに混入してしまうため、更新したモデルの性能をを正しく評価することができずにエラーとなります。  

{{% h4_error_avoid %}}
今回の評価データ抽出条件としては、前回の評価データ抽出条件と同じかより狭い範囲となるように値を調整します。  
もしくは、前回学習データと前回からの差分学習データを別々に用意してモデル更新を行うと、評価データへ学習データが混入するのを避けられるため、このエラーの発生を回避することができます。  
