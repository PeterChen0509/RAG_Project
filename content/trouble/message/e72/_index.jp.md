---
title: "系列数に対して学習対象のデータの件数が不足しています"
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
1系列当たりの有効な学習データ数が少ない場合にエラーとなります。  

{{% h4_error_avoid %}}
予測モデルの作成では系列ごとに学習を行うため、有効な学習データ数が (系列数 × 11)件 以上となるようにデータを準備します。  
また、予測したい項目が欠損したり無効な値のものは利用できないので、欠損や無効値のデータが多くならないように注意してください。  
時系列予測モードで使用する学習・予測用データの作成方法については、「{{% a_in "../../../tips/specification/dataset_for_timeseries/" "数値予測(時系列予測モード)用のデータセット" %}}」もご参照ください。  
