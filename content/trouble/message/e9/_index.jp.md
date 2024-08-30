---
title: "対応期間外の日時があるため、データを読み込めません"
date: 2018-12-29T11:02:05+06:00
lastmod: 2024-05-31T15:26:01+09:00
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
keywords: ["時系列モード", "対応期間"]
---

{{% h4_error_cause %}}
Prediction One では 1970年1月1日よりも前のデータ、および、4000年1月1日以降のデータを予測したい項目の時間情報項目として扱うことができません。

{{% h4_error_avoid %}}
1970年1月1日以降、4000年1月1日未満のデータのみを予測モデル作成(学習)用データに使用してください。
