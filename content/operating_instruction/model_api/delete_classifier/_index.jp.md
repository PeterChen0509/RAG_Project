---
title: "Delete Classifier APIの仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 5
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
    "API作成",
    "API公開",
    "デプロイ",
	"予測API"
  ]
---

REST APIを使用して、予測APIを削除できます。

※クラウドアプリ上からも確認ができなくなりますので、classifier_idをご確認の上実行ください。

### Delete Classifier API

予測APIを削除します。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/classifiers

HTTPメソッドは、DELETEです。

#### Request

##### header

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key。       |

##### path parameter

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| classifier_id         | 予測API ID       |

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

Delete Classifier APIのpythonによる実行例が以下となります。

```
import requests

classifier_id = 'YOUR_CLASSIFIER_ID'
api_url = f'https://developer-api.predictionone.sony.biz/v1/external/classifiers/{classifier_id}'
api_key = 'YOUR_API_KEY'

headers = {'x-api-key': api_key}

# request
response = requests.delete(api_url, headers=headers)
response_json = response.json()
```

#### 実行例 2

Delete Classifier APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. リクエストする
$ curl -o "response.json" -H "x-api-key:{Get API Key APIから取得したAPI KEY}" -H "Content-Type: application/json" -X DELETE -G https://developer-api.predictionone.sony.biz/v1/external/classifiers/{YOUR_CLASSIFIER_ID}
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -H "Content-Type: application/jsonn" -X DELETE https://developer-api.predictionone.sony.biz/v1/external/classifiers/xxxxxx
```

