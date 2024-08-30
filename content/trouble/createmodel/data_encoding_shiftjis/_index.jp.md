---
title: "データファイルの文字コードはShift_JISなのに文字化けが発生するのはなぜですか？"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["文字化け", "Shift-JIS"]
---

Prediction One ではファイルの先頭 1000 バイトを読み込んで文字コードを判定しています。そのため、先頭 1000 バイトに文字コードを判定できる情報がないと誤判定が起きることがあります。
その場合、データファイルを UTF-8 (BOM あり)に変換していただくようお願いいたします。
