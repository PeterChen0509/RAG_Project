---
title: "指定された範囲に該当しないデータが存在しないため、学習用データが作成できませんでした"
date: 2024-05-31T15:54:09+09:00
lastmod: 2024-05-31T15:54:09+09:00
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
keywords: ["範囲指定", "学習用データ"]
#keywordsForRDC: [""]
---

{{% h4_error_cause %}}
数値や日付の範囲を指定して評価データを抽出する時、指定した範囲にすべてのデータが含まれてしまい学習用データが0件となる場合に発生します。  

{{% h4_error_avoid %}}
条件に当てはまらないデータが残るように、指定する日付や値を調整してください。  
