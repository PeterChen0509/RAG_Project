---
title: "データが存在しない期間が長いため、データが読み込めません"
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
keywords: ["読み込まれない", "読み込めない", "時系列モード"]
---

{{% h4_error_cause %}}
「時系列予測モード」で時系列予測を行う場合、指定された予測したい項目の時間情報項目に含まれる時間の時間間隔はなるべく一定にしていただく必要があります。  
予測したい項目の時間情報項目に含まれるタイムスタンプを時間に沿って並べなおした時に、長期間のデータ欠損が検出されると、このメッセージが表示されます。

{{% h4_error_avoid %}}
予測したい項目の時間情報項目に含まれるデータを確認し、時間間隔が空いている箇所のデータを収集して予測モデル作成(学習)用データに追加してください。もしくは、時間間隔が空いている箇所以前のデータを予測モデル作成(学習)用データから取り除いてください。
時系列予測モードで使用する学習・予測用データの作成方法については、「{{% a_in "../../../tips/specification/dataset_for_timeseries/" "数値予測(時系列予測モード)用のデータセット" %}}」もご参照ください。