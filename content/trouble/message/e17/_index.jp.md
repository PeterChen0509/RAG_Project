---
title: "対象外の文字エンコードなので、データを読み込めません"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
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
keywords: ["エンコード"]
---

{{% h4_error_cause %}}
Prediction One が対応していない文字エンコードを使用したファイルを読み込んだ場合、このメッセージが表示されます。

{{% h4_error_avoid %}}
ファイルの文字コードを

- UTF-8 (BOM あり)
- Shift_JIS

に変更することでファイルを読み込むことが可能になります。
