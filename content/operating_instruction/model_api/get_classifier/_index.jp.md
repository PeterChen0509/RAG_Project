---
title: "Get Classifier APIの仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 3
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

REST APIを使用して、予測APIを取得できます。
以下の一連のAPIによって実行します。
1. Get API Key API：API KEYを取得
2. Create Classifier API：予測APIを作成
3. Get Classifier: 予測APIを取得

### Get Classifier API

予測APIを取得します。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/classifiers

HTTPメソッドは、GETです。

#### Request

##### header

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key。       |

##### path parameter

ありません。

##### query parameter

ありません。

##### body

ありません。

#### Response

##### body

以下のフォーマットです。

```
{
    "classifiers": [{
        "classifier_id": str,
        "model_id": int,
        "status": str,
        "api_key": str,
        "version": str,
        "url": Or(str, None),
        "active": bool,
        "is_editable": bool,
        "create_datetime": str,
        "update_datetime": str,
        "rules": [{
            "source": str,
            "order": str,
            "priority": int
        }]
    }]
}
```

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| classifier_id         | 予測API ID       |
| model_id      | モデルID |
| status      | 下記status参照 |
| api_key         | 予測APIのAPI KEY       |
| version      | 予測APIのバージョン |
| url      | 予測APIのURL |
| active         | 予測APIが動作中かどうか       |
| is_editable      | 予測APIが編集制限中かどうか |
| create_datetime      | モ予測APIの作成日 |
| update_datetime         | 予測APIの更新日          |
| rules      | 下記rules参照 |

#### status

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| building         | 作成中       |
| running      | 実行中 |
| updating      | 更新中 |
| failed      | 失敗 |
| terminating         | 停止中       |
| terminated      | 停止済 |

#### rules

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| source         | IP すべてを許可する場合は0.0.0.0/0を指定       |
| order      | allow: 許可, deny: 拒否 |
| priority      | 優先度 |

##### error message

| code       | error       | message               | reason               |
| :--------- | :---------- | :-------------------- | :------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | APIキーが存在しない |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This user may be deleted. | ユーザー情報が削除されている可能性がある |

#### 実行例 1

Get Classifier APIのpythonによる実行例が以下となります。

```
import requests

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/classifiers'
api_key = 'YOUR_API_KEY'

headers = {'x-api-key': api_key}

# request
response = requests.get(api_url, headers=headers)
response_json = response.json()
```

#### 実行例 2

Get Classifier APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. body情報を記載したファイルを保存(body.txtとする)

3. リクエストする
$ curl -o "response.json" -H "x-api-key:{Get API Key APIから取得したAPI KEY}" -H "Content-Type: application/json" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/classifiers/{YOUR_CLASSIFIER_ID}
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -H "Content-Type: application/jsonn" -X GET https://developer-api.predictionone.sony.biz/v1/external/classifiers/xxxxxx
```