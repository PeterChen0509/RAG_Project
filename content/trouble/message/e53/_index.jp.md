---
title: "データ結合に必要な項目がないため、結合ができません。"
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
keywords: ["データ準備", "データ結合", "結合できない"]
---

{{% h4_error_cause %}}
結合しようとするデータから外部結合を行うための外部キー候補が見つからない場合に発生します。

{{% h4_error_avoid %}}
結合対象のファイルそれぞれにデータ結合の外部キーの候補となる数値型や文字列型のカラムが存在するファイルを選択します。  
自動で判定されたカラム型が誤っている場合は、入力ファイルのタブメニューから「データタイプの設定」を行い、正しい型で読み込まれるようにします。  