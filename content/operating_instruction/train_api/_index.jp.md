---
title: "学習APIの仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1
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
|1 | Get API Key| API KEYを取得する|
|2 | Train Data Upload| 学習用データセットをアップロードする|
|3 | Train Data Set Info| 学習用データセット情報を取得する|
|4 | Train| 予測モデルを作成する|
|5 | Train Status Check| 学習状況を取得する|

シークレットキーの取得方法については「{{% a_in "secret_key/" "シークレットキーを取得"%}}」のページをご覧ください。

各APIの関係性は以下の図をご覧ください。

![](../img/t_slide109.png)


