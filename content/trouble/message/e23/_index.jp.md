---
title: "項目が1つしかないため、データを読み込めません"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
# weight: カテゴリごとにまとめる
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
keywords: ["項目", "読み込めない", "1つ"]
---

{{% h4_error_cause %}}
予測モデル作成(学習)用データに列が一つしか存在しない場合、そのデータを読み込んで学習・分析することはできません。
時系列予測モードを使用しない場合、予測モデル作成(学習)用データには予測したい項目である「予測したい項目」の列と予測したい項目に関連する情報を含んだ列が<u>最低一つ</u>以上含まれている必要があります。
時系列予測モードを使用する場合、予測モデル作成(学習)用データには予測したい項目である「予測したい項目」の列と、<u>予測したい項目の時間情報である「予測したい項目の時間情報項目」の列</u>が含まれている必要があります。

{{% h4_error_avoid %}}
Prediction One で予測分析したいデータには、予測したい項目とそれに関連する情報を含んだ項目の最低２つの列が含まれている必要があります。
{{% a_in "../../../tips/how_to_create_dataset/" "TIPS「データセットの作り方」" %}}もご参照ください。
