---
title: "同じ日時で系列間の全ての予測したい項目がそろっているデータが少なすぎます"
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
keywords: ["系列数", "データ", "不足"]
---

{{% h4_error_cause %}}
系列ありの時系列予測モデルの学習において、時間情報項目が同じ日付のデータが全系列分そろっている割合が少ないとエラーとなることがあります。  

{{% h4_error_avoid %}}
予測モデルの作成では系列ごとに学習を行うため、時間情報項目が同じ日付のデータが系列の数だけ必要となります。  
すべての系列のデータがそろっていない日付ができるだけ少なくなるようにデータを準備します。  
予測したい項目が欠損したり無効な値のものは利用できないので、欠損や無効値のデータにもご注意ください。  