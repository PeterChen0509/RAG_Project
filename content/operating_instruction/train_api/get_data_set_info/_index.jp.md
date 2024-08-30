---
title: "Train Data Set Info APIの仕様"
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
    "Train",
    "train"
  ]
---

REST APIを使用して、Prediction Oneも予測モデルのできます。以下の一連のAPIによって実行します。
1. Get API Key API：API KEYを取得
2. Train Data Upload API：データをアップロード
3. Train Data Set Info: 学習用データセットの情報を取得
4. Create Model API：学習の実行
5. Status Check API：学習の状態確認と、学習後の結果ファイルダウンロードURLの取得

### Train Data Set Info API

学習用のデータをアップロードするURLを取得します。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/data-sets/column-info

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
| external_process_id    | Train data upload APIのレスポンスに含まれるexternal_process_id|

##### body

ありません。

#### Response

##### body

以下のフォーマットです。

```
{
  "raw_column_names": [str],
  "raw_training_data": [{
    "row_data": str
  }],
  "training_data_columns": [{
    "column_id": int,
    "name": str,
    "initial_data_type": int,
    "available_data_types": [
      int
    ],
    "unique_count": int,
    "data_count": int,
    "missing_count": int,
    "cor_score": Or(float, None),
    "classify_value": [Or(
      Optional({
        "name": str,
        "value": int
      }), None)
    ],
    "numerical_value": [Or(
      Optional({
        "max_value": float,
        "min_value": float,
        'avg_value': float,
        'median_value': float
      }), None)
    ],
    Optional("range_pick_info"): Or({
      Optional("numeric"): Or({
        "max_val": float,
        "min_val": float,
        "initial_threshold": float
      }, None),
      Optional("date"):  Or({
        "max_epoc_sec": int,
        "min_epoc_sec": int,
        "initial_threshold_epoc_sec": int,
        "time_unit_id": int
      }, None)
    }, None)
  }],
  "useless_column_list": [Or(str, None)],
  "trainingdata_row_count": int
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

Train Data Set Info APIのpythonによる実行例が以下となります。

```
import requests

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/data-sets/column-info'
api_key = 'YOUR_API_KEY'
# Train Data Upload API実行時に取得したexternal_process_id
external_process_id = 'YOUR_EXTERNAL_PROCESS_ID'

headers = {'x-api-key': api_key}

# request
params = {'external_process_id': external_process_id}

response = requests.get(api_url, params=params, headers=headers)
response_json = response.json()
```

#### 実行例 2

Train Data Set Info APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. external_process_idを記載したファイルを保存(params.txtとする)

3. リクエストする
$ curl -o "response.json" -H "x-api-key:{Get API Key APIから取得したAPI KEY}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/data-sets/column-info --data-urlencode filename@"{2.のファイルのフルパス}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET https://developer-api.predictionone.sony.biz/v1/external/data-sets/column-info --data-urlencode filename@params.txt

4. response.jsonを確認しカラム情報
```

