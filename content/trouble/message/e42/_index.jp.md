---
title: "システム時刻の異常を検出したため、失敗しました"
date: 2024-05-31T15:54:09+09:00
lastmod: 2024-05-31T15:54:09+09:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
  hide_on_dist_type: ["RDC"]
# 検索でヒットする文字列の指定
keywords: ["システム時刻"]
keywordsForRDC: [""]
---

{{% dist_type_only "SNC" %}}

{{% h4_error_cause %}}
以下のケースが考えられます.  

- (a)システムの時間が巻き戻されたことを検出した。  
- (b)インストールにおいて何らかの問題が発生して、正しくインストールされなかった。  

{{% h4_error_avoid %}}
(a)の場合、システム時刻を元の時刻に戻すことでエラーを解消できることがあります。  
それでも解決しない場合や(b)の場合は、サポート窓口へご相談いただきますようお願いいたします。  

{{% /dist_type_only %}}
