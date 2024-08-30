---
title: "Get Data Set APIの仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 9
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

REST APIを使用して、Prediction Oneも予測モデルを取得できます。

### Get Data Set API

予測モデルを取得します。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/data-sets

HTTPメソッドは、GETです。

#### Request

##### header

| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key。       |

##### path parameter

ありません。

##### query parameter

| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| Optional(offset)    | 取得開始位置(デフォルト: 0)|
| Optional(limit)    | 取得件数(デフォルト: 30)|

##### body

ありません。

#### Response

##### body

以下のフォーマットです。

```
{
  "data_sets": [{
    "data_set_id": int,
    "owner_user_id": str,
    "name": Or(str, None),
    "extension": str,
    "column_count": int,
    "data_count": int,
    "data_size": int,
    "download_url": str,
    "updated_date": str,
    "created_date": str
  }],
  "metadata": {
    "offset": int,
    "limit": int,
    "total": int
  }
}
```

##### error message

| code       | error       | message               | reason               |
| :--------- | :---------- | :-------------------- | :------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | APIキーが存在しない |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This user may be deleted. | ユーザー情報が削除されている可能性がある |

#### 実行例 1

Get Data Set APIのpythonによる実行例が以下となります。

```
import requests

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/data-sets'
api_key = 'YOUR_API_KEY'

headers = {'x-api-key': api_key}
params = {'offset': 0, 'limit': 30}

# request
response = requests.get(api_url, params=params, headers=headers)
response_json = response.json()
```

#### 実行例 2

Get Data Sets APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. offset, limitを記載したファイルを保存(params.txtとする)

3. リクエストする
$ curl -o "response.json" -H "x-api-key:{Get API Key APIから取得したAPI KEY}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/data-sets --data-urlencode filename@"{2.のファイルのフルパス}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET https://developer-api.predictionone.sony.biz/v1/external/data-sets --data-urlencode filename@params.txt
```

