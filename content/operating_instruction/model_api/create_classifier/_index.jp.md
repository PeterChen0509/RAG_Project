---
title: "Create Classifier APIの仕様"
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
  "API作成",
  "API公開",
  "デプロイ",
  "予測API",
  ]
---

REST APIを使用して、予測APIを作成できます。
以下の一連のAPIによって実行します。
1. Get API Key API：API KEYを取得
2. Create Classifier API：予測APIを作成
3. Get Classifier: 予測APIを取得

### Create Classifier API

予測APIを作成します。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/classifiers

HTTPメソッドは、POSTです。

#### Request

##### header

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key。       |
| content-type      | application/json |

##### path parameter

ありません。

##### query parameter

ありません。

##### body

以下のフォーマットです。

```
{
  "model_id": int,
  "rules": [{
    "source": str,
    "order": str,
    "priority": int
  }]
}
```

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| model_id         | モデルID       |
| rules      | 下記rules参照 |

#### rules

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| source         | IP すべてを許可する場合は0.0.0.0/0を指定       |
| order      | allow: 許可, deny: 拒否 |
| priority      | 優先度 |

#### Response

##### body

以下のフォーマットです。

```
{
    "classifier_id": str,
    "api_key": str,
    "version": str
}
```

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| classifier_id         | 予測API ID       |
| api_key      | API KEY |
| version      | 予測API バージョン |

##### error message

| code       | error       | message               | reason               |
| :--------- | :---------- | :-------------------- | :------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | APIキーが存在しない |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This user may be deleted. | ユーザー情報が削除されている可能性がある |

#### 実行例 1

Create Classifier APIのpythonによる実行例が以下となります。

```
import requests

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/classifiers'
api_key = 'YOUR_API_KEY'

model_id = int('YOUR_MODEL_ID')
headers = {'x-api-key': api_key, 'content-type': 'application/json'}

# request
body = {
    'model_id': model_id,
    'rules': [{
        'source': '0.0.0.0/0',
        'order': 'allow',
        'priority': 0
    }]
}
response = requests.post(api_url, json=body, headers=headers)
response_json = response.json()
classifier_id = response_json['classifier_id']
```


#### 実行例 2

Create Classifier APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. body情報を記載したファイルを保存(body.txtとする)

3. リクエストする
$ curl -o "response.json" -H "x-api-key:{Get API Key APIから取得したAPI KEY}" -H "Content-Type: application/json" -X POST -d @"{2.のファイルのフルパス}" -G https://developer-api.predictionone.sony.biz/v1/external/classifiers
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -H "Content-Type: application/jsonn" -X POST -d @body.txt https://developer-api.predictionone.sony.biz/v1/external/classifiers
```
