---
title: "使用できない文字が含まれています"
date: 2024-06-06T15:20:16+09:00
lastmod: 2024-06-06T15:20:16+09:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["データコネクタ", "使用できない文字"]
---

{{% h4_error_cause %}}
入力に使用できない文字が含まれているときに表示されるメッセージです。  

{{% h4_error_avoid %}}
接続先ごとに入力できない文字が異なりますのでご注意ください。  
入力時に使用できない文字は以下のとおりです。  
  
- Amazon S3 選択時  
  !-_.*\'() 以外の記号等  
- Azure: Blob Storage 選択時  
  \- 以外の記号等  
- Google Cloud: Cloud Storage 選択時  
  \-_. 以外の記号等  
