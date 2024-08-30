---
title: "再学習APIの仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  [
    "API",
    "REST API",
  ]
---

### API一覧

| No.  |  API名     | 機能概要              |
| :--- | :--------- | :------------------  |
|1 | Retrain Data Upload | 作成済モデルに対して再学習を実行する|
|2 | Retrain Status Check | 再学習状況を取得する|
|3 | Retrain Model Switch| API作成済モデルの切り替えを実行する|

クレデンシャルの取得方法については「{{% a_in "log_in_credential/" "ログインクレデンシャルの取得"%}}」のページをご覧ください。

各APIの関係性は以下の図をご覧ください。

![](../img/t_slide109.png)


