---
title: "Train Status Check APIの仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 6
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
    "Train Status Check",
    "train status check"
  ]
---

REST APIを使用して、Prediction Oneも予測モデルの作成ができます。以下の一連のAPIによって実行します。
1. Get API Key API：API KEYを取得
2. Train Data Upload API：データをアップロード
3. Train Data Set Info: 学習用データセットの情報を取得
4. Create Model API：学習の実行
5. Status Check API：学習の状態確認と、学習後の結果ファイルダウンロードURLの取得

### Train Data Upload API

学習用状況を取得します。
学習が完了したときに学習結果ファイルダウンロードURLが取得できます。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/models/results

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
    "status": str,
    "created_datetime": str
    "updated_datetime": str
    Optional("result_url"): str
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

Train Status Check APIのpythonによる実行例が以下となります。

Train Data Upload APIの実行を行った状態を前提としています。

```
import requests
import time
import zipfile

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/models/results'
api_key = 'YOUR_API_KEY'
# Train Data Upload API実行時に取得したexternal_process_id
external_process_id = 'YOUR_EXTERNAL_PROCESS_ID'

headers = {'x-api-key': api_key}

# request
params = {'external_process_id': external_process_id}

while True:
  response = requests.get(api_url, params=params, headers=headers)
  response_json = response.json()
  status = response_json['status']
  if status == 'finished':
    break
  time.sleep(30)

result_url = response_json['result_url']

# 結果ファイルのダウンロード
result_data = requests.get(result_url).content
with open('result.zip' ,mode='wb') as f:
  f.write(result_data)

# 結果ファイルの確認
zf = zipfile.ZipFile('result.zip')
```

#### 実行例 2

Train Status Check APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. external_process_idを記載したファイルを保存(params.txtとする)

3. リクエストする
$ curl -o "response.json" -H "x-api-key:{Get API Key APIから取得したAPI KEY}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/models/results --data-urlencode filename@"{2.のファイルのフルパス}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET https://developer-api.predictionone.sony.biz/v1/external/models/results --data-urlencode filename@params.txt

4. response.jsonを確認statusを確認
statusがfinishedの場合にresult_urlを取得

5. 学習結果を取得
$ curl -G GET {4.で取得したresult_url}
```

