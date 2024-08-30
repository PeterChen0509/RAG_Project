---
title: "APIの仕様"
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

| No.  | カテゴリ    |  API名     | 機能概要              |
| :--- | :--------- | :--------- | :------------------  |
|1 | 学習 | {{% a_in "../train_api/api_key/" "Get API Key"%}} | API KEYを取得する|
|2 | 学習 | {{% a_in "../train_api/train_data_upload/" "Train Data Upload"%}} | 学習用データセットをアップロードする|
|3 | 学習 | {{% a_in "../train_api/get_data_set_info/" "Train Data Set Info"%}} | 学習用データセット情報を取得する|
|4 | 学習 | {{% a_in "../train_api/train/" "Train"%}} | 予測モデルを作成する|
|5 | 学習 | {{% a_in "../train_api/train_status_check/" "Train Status Check"%}} | 学習状況を取得する|
|6 | 学習 | {{% a_in "../train_api/get_model/" "Get Model"%}} | 予測モデルを取得する|
|7 | 学習 | {{% a_in "../train_api/delete_model/" "Delete Model"%}} | 予測モデルを削除する|
|8 | 学習 | {{% a_in "../train_api/get_data_set/" "Get Data Set"%}} | データセットを取得する|
|9 | 学習 | {{% a_in "../train_api/delete_data_set/" "Delete Data Set"%}} | データセットを削除する|
|10 | 予測 | {{% a_in "../model_api/inference/" "Inference"%}}  | 予測データに対して作成済モデルによる予測を実行する|
|11 | 予測 | {{% a_in "../model_api/create_classifier/" "Create Classifier"%}} | 予測APIを作成する|
|12 | 予測 | {{% a_in "../model_api/get_classifier/" "Get Classifier"%}} | 予測APIを取得する|
|12 | 予測 | {{% a_in "../model_api/update_classifier/" "Update Classifier"%}} | 予測APIを更新する|
|14 | 予測 | {{% a_in "../model_api/delete_classifier/" "Delete Classifier"%}} | 予測APIを削除する|
|15 | 再学習 | {{% a_in "../re_train_api/re_train_data_upload/" "Retrain Data Upload"%}} | 作成済モデルに対して再学習を実行する|
|16 | 再学習 | {{% a_in "../re_train_api/re_train_status_check/" "Retrain Status Check"%}} | 再学習状況を取得する|
|17 | 再学習 | {{% a_in "../re_train_api/switch_model/" "Retrain Model Switch"%}} | 予測API作成済モデルの切り替えを実行する|


各APIの関係性は以下の図をご覧ください。

![](../img/t_slide109.png)


