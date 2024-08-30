---
title: "対応していない時間間隔のデータを含むため、データを読み込めません"
date: 2018-12-29T11:02:05+06:00
lastmod: 2024-05-31T15:09:54+09:00
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
keywords: ["時系列モード", "時間間隔", "フォーマット"]
---

{{% h4_error_cause %}}
Prediction One では、分未満単位の時間間隔データに対して時系列予測を行うことができません。

{{% h4_error_avoid %}}
分以上の単位で時間間隔が等しいデータを準備してください.  
Prediction One では、予測したい項目の時間情報項目がすべて月末日で揃っている場合は、月末日揃えでも予測モデルを作成できます。もし、月末日で予測したい項目の時間情報項目を揃えている場合、月末日でないデータが含まれていないかをご確認ください。  
  
「{{% a_in "../../../tips/specification/dataset_for_timeseries/" "数値予測(時系列予測モード)用のデータセットにて対応している時間間隔" "time-interval" %}}」の内容もご参照ください。
