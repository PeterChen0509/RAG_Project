---
title: "Delete Data Set APIの仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 10
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
    "Train",
    "train"
  ]
---

REST APIを使用して、Prediction Oneも予測モデルを削除ができます。

※クラウドアプリ上からも確認ができなくなりますので、data_set_idをご確認の上実行ください。

### Delete Data Set

予測モデルを削除します。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/data-sets/{data_set_id}

HTTPメソッドは、DELETEです。

#### Request

##### header

| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key。       |

##### path parameter

| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| data_set_id         | 削除するデータセットID       |

##### query parameter

ありません。

##### body

ありません。

#### Response

##### body

ありません。

##### error message

| code       | error       | message               | reason               |
| :--------- | :---------- | :-------------------- | :------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | APIキーが存在しない |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This user may be deleted. | ユーザー情報が削除されている可能性がある |

#### 実行例 1

Delete Data Set APIのpythonによる実行例が以下となります。

```
import requests

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/data-sets'
api_key = 'YOUR_API_KEY'

headers = {'x-api-key': api_key}

# 削除するdata_set_Id
data_set_Id = {data_set_Id}
api_url = f'{api_url}/{data_set_Id}'

# request
response = requests.delete(api_url, headers=headers)
```

#### 実行例 2

Train APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. リクエストする
$ curl -o "response.json" -H "x-api-key:{Get API Key APIから取得したAPI KEY}" -H "Content-Type: application/json" -X DELETE -d @"{2.のファイルのフルパス}" -G https://developer-api.predictionone.sony.biz/v1/external/data-sets/{削除するdata_set_Id}
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -H "Content-Type: application/json" -X DELETE -d @body.txt https://developer-api.predictionone.sony.biz/v1/external/data-sets/xxx
```

