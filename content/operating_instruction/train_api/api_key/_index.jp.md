---
title: "Get API Key APIの仕様"
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
    "API KEYAPI",
    "API KEY",
    "apikey"
  ]
---

REST APIを使用して、Prediction Oneも予測モデルの作成ができます。以下の一連のAPIによって実行します。
1. Get API Key API：API KEYを取得
2. Data Upload API：データをアップロード
3. Train Data Set Info: 学習用データセットの情報を取得
4. Create Model API：学習の実行
5. Status Check API：学習の状態確認と、学習後の結果ファイルダウンロードURLの取得

### Get API Key API

API KEYを取得します。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/api-key

HTTPメソッドは、GETです。

#### Request

##### header

| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| x-api-key         | Secret Key。            |

##### path parameter

ありません。

##### query parameter

| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| credential_type         | 下記credential_type参照|
| model_id         | credential_typeでretrainを指定した場合必須。{{% a_in "../../re_train_api/" "再学習する予測APIのモデルID"%}}を指定|

#### credential_type

| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| train         | {{% a_in "../" "学習API"%}}用|
| deploy         | {{% a_in "../../model_api/" "予測API"%}}用|
| retrain         | {{% a_in "../../re_train_api/" "再学習API"%}}用|

##### body

ありません。

#### Response

##### body

以下のフォーマットです。

```
{
  "api_key": str,
  "end_date": str
}
```

##### error message

| code       | error       | message               | reason               |
| :--------- | :---------- | :-------------------- | :------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | APIキーが存在しない |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This user may be deleted. | ユーザー情報が削除されている可能性がある |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This model may be deleted. | モデルが削除されている可能性がある |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Model id is required. | モデルIDが指定されていない可能性がある |

#### 実行例 1

Get API Key APIのpythonによる実行例が以下となります。

```
import requests

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/api-key'
secret_key = 'YOUR_SECRET_KEY'

headers = {'x-api-key': secret_key}


# 再学習の場合​
params = {'credential_type': 'retrain', 'model_id': YOUR_MODEL_ID}

# 学習の場合​
params = {'credential_type': 'train'}

# 予測APIデプロイの場合
params = {'credential_type': 'deploy'}

# request
response = requests.get(api_url, params=params, headers=headers)
response_json = response.json()
api_key = response_json['api_key']
```

#### 実行例 2

Get API Key APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. credential_typeを記載したファイルを保存(param.txtとする)

3. リクエストする
$ curl -o "response.json" -H "x-api-key:{画面から取得したシークレットキー}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/api-key --data-urlencode filename@"{3.のファイルのフルパス}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/api-key --data-urlencode filename@param.txt

4. response.jsonを確認しapi_keyを取得
```

