---
title: "予測データに、(有効な期間内の)予測可能な系列のデータが含まれていません"
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
keywords: ["系列", "予測データ"]
---

{{% h4_error_cause %}}
入力した予測用データに予測可能な系列のデータが1件も含まれていない場合にエラーとなります。  

{{% h4_error_avoid %}}
予測モデルを作成するとき、使用する学習データの内容によっては予測ができない系列ができてしまうことがあります。  
入力する予測用データの各データの系列が予測可能な系列のものかを確認してください。  
