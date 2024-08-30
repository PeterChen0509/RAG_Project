---
title: "有効なデータ数が少ないため、データを読み込めません"
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
keywords: ["有効データ", "読み込めない"]
---

{{% h4_error_cause %}}
学習用データで予測したい項目が欠損したり無効な値のものが多いとエラーとなる場合があります。  

{{% h4_error_avoid %}}
学習用データにおいて予測したい項目が欠損したり無効な値のものは利用できないので、欠損や無効値のデータが多くならないようにデータを準備します。  
学習・予測用データ仕様の詳細については、「{{% a_in "../../../tips/specification/dataset_format_detail/" "データセットのより詳細な仕様" %}}」もご参照ください。  
