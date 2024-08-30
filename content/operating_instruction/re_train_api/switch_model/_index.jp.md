---
title: "Retrain Model Switch APIの仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4
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
    "学習API",
    "再学習API",
    "Retrain Model Switch ",
    "retrain model switch"
  ]
---

REST APIを使用して、Prediction Oneも予測モデルのアップデート（最新データによるモデルの再学習）ができます。以下の一連のAPIによって実行します。
1. Retrain Data Upload API：データアップロードし、再学習を実行
2. Retrain Status Check API：再学習の状態確認と、学習後の結果ファイルダウンロードURLの取得
3. Retrain Model Switch API：API作成済のモデルを再学習したモデルに切り替え

### Retrain Model Switch API

公開済のモデルを再学習したモデルで更新します。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{retrain_job_id}/update_model

HTTPメソッドは、PUTです。

#### Request

##### header

| name              | 説明                                       |
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key。モデル毎に１つ割り当てられる。       |

##### path parameter

| name              | 説明                                       |
| :---------------- | :----------------------------------------- |
| retrain_job_id    | retrain_job_id。アップロードURL取得時に発行される。       |

##### query parameter

ありません。

##### body

ありません。

#### Response

##### body

以下のフォーマットです。

```
{
  "metadata": {
    "retrain_job_id": str
  }
}
```

##### error message

| code       | error         | message                          | reason                         |
| :--------- | :------------ | :------------------------------- | :----------------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | APIキーが存在しない |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not found retrain job. | retrain_job_idが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not found classifier. | 予測APIが削除された可能性があります |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Retrain job is not finished. | 再学習が完了していません |

#### 実行例 1

Retrain Model Switch APIのpythonによる実行例が以下となります。

再学習が完了し実行結果の確認を行った状態を前提としています。

```
import requests

retrain_job_id = 'YOUR_RETRAIN_JOB_ID'
api_url = f'https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{YOUR_RETRAIN_JOB_ID}/update_model'
api_key = 'YOUR_API_KEY'

headers = {
    'x-api-key': api_key
}
response = requests.put(api_url, headers=headers)

```

#### 実行例 2

Retrain Model Switch APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。
再学習が完了し実行結果の確認を行った状態を前提としています。

```
1. コマンドプロンプトを立ち上げる

2. 表示をUTF-8に変更
$ chcp 65001

3. リクエストする
$ curl -H "x-api-key:{YOUR_API_KEY}" -X PUT https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{retrain_job_id}/update_model
ex) $ curl -H "x-api-key:xxxx-xxx-xxx-xxxx" -X PUT https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{xxxx-xxxx-xxxx-xxxx}/update_model
```
