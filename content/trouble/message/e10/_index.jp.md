---
title: "予測データに、予測可能な時刻のデータが含まれていません"
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
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["時系列モード"]
---

{{% h4_error_cause %}}
時系列予測モードで指定した予測期間の範囲外のデータに対して予測を行うことはできません。
たとえば、`2020/1/1`~`2020/1/31`の期間のデータに対して予測を行う予測モデルは、`2020/2/1`以降のデータに対して予測を行うことはできません。

{{% h4_error_avoid %}}
予測用データの予測したい項目の時間情報項目の列に予測期間に含まれる時間情報が含まれているかをご確認ください。
予測を行いたい時刻が含まれるように予測期間を設定し、予測モデルの学習を行ってください。
