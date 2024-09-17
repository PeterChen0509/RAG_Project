---
title: "Inference APIの仕様"
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
  "API作成",
  "API公開",
  "デプロイ",
  "予測API",
  ]
---

REST APIを使用して、Prediction Oneの予測を実行できます。

### Inference API

予測データに対して作成済モデルによる予測を実行できます。
実行に必要なエンドポイント（URL）やAPIキー等は「{{% a_in "../model_api/" "API作成画面"%}}」から作成してください。
API作成後の画面で必要な情報を確認することができます。

#### URL

URLは「{{% a_in "../model_api/" "API作成画面"%}}」で確認できます。

HTTPメソッドは、POSTです。

#### Request

##### header

| name              | 説明                                        |
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key。モデル毎に１つ割り当てられる。       |
| content-type      | application/json; charset=utf-8 を指定する |

##### path parameter

ありません。

##### query parameter

ありません。

##### body

以下のフォーマットです。

```
{
	"inputs": [
		{
			"name": "pr",   # prediction data
			"type": "csv",
			"data": "6LfjeFlG/xxxxxx"
		},
		{
			"name": "ar",	# add analysis result
			"type": "boolean",
			"data": true
		},
		{
			"name": "ad",	# add prediction data
			"type": "boolean",
			"data": true
		},
		{
			"name": "nc",	# without classification results
			"type": "boolean",
			"data": true
		},
		{
			"name": "nr",	# without row numbers
			"type": "boolean",
			"data": true
		},
		{
			"name": "pc",
			"type": "string",
			"data": "column_name"
		}
	]
}
```

`inputs`のパラメータ

| name          | type       |          | 説明                                                                     |
| :------------ | :--------- | :------- | :---------------------------------------------------------------------- | 
|  pr           | csv(base64)| required |  予測したいデータの項目名の行とデータ１行からなる予測ファイルのcsvをbase64エンコードした値 　|
|  ar           | boolean    | required |  予測理由の算出を行う(prediction_analysis.csv を出力する)かどうか。予測理由が必要な場合は`true`を指定する。予測理由が不要で処理時間を短縮したい場合は`false`を指定する。|
|  ad           | boolean    | required |  予測用データを出力に追加するかどうか。追加する場合は`true`を指定する。|
|  nc           | boolean    | required |  二値分類・多値分類時に、(予測確率に加えて)分類結果を出力しないかどうか。分類結果が不要な場合は`true`を指定する。分類結果が必要な場合は`false`。　|
|  nr           | boolean    |          |  予測結果に行番号を出力しないかどうか。行番号が不要な場合`true`を指定する。行番号が必要な場合は`false`を指定する。|
|  pc           | string     |          |  予測結果の左端に付与する項目の名前。prで指定した予測ファイルに含まれる項目名のいずれかを指定する。|

#### Response

##### body

以下のフォーマットです。

```
{
    "version": str,
	"outputs": [
		{
			"name": "prediction_analysis.csv",
			"data": "6LfjeFlG/xxxxxx"
		},
		{
			"name": "prediction_valid.csv",
			"data": "6LfjeFlG/xxxxxx"
		}
	]
}
```

`outputs`のパラメータ

| name                       | type       | 説明                                                                     |
| :------------------------- | :--------- | :---------------------------------------------------------------------- | 
|  prediction_valid.csv      | csv(base64)|  予測結果のcsvをbase64エンコードした値                                  　 |
|  prediction_analysis.csv   | csv(base64)|  予測理由のcsvをbase64エンコードした値。Requestでarを`true`と設定した場合のみ含まれる。 　|

##### error message

| code       | error         | message                          | reason                         |
| :--------- | :------------ | :------------------------------- | :----------------------------- |
| 4001030101 | NOT_FOUND_CLASSIFIER| Not found classifier in classifiers table | classifier_idが間違っている |
| 4001030104 | BAD_REQUEST| Invalid request | スキーマエラー。入力が正しい形式かご確認ください。 |
| 4031030201 | ACCESS_DENIED | Invalid API key | APIキーが間違っている |
| 4031030201 | ACCESS_DENIED | Invalid classifier id | classifier_idが見つからない |
| 4031030201 | ACCESS_DENIED | Not allowed source ip | 接続元のIPはアクセスできない |
| 5031030101 | SERVICE_UNAVAILABLE_ERROR | status is not running (status: stopped) | サーバーが実行中ではない |

#### 実行例 1

Inference APIのpythonによる実行例が以下となります。

サンプルデータの「1_プレミアムサービス購入.csv」で作成したモデルに対して、API作成を行った状態を前提としています。
予測対象として「2_プレミアムサービス購入（予測用）.csv」を利用して、Inference APIを使用して予測を算出しています。

```
import base64
import requests

prediction_data_file_path = '2_プレミアムサービス購入（予測用）.csv'
api_url = 'YOUR_API_URL'
api_key = 'YOUR_API_KEY'

headers = {
    'x-api-key': api_key, 'content-type': 'application/json; charset=utf-8'}

with open(prediction_data_file_path, 'rb') as f:
    lines = f.readlines()

header = lines[0]
for line in lines[1:]:
    prediction_data = base64.b64encode(header + line).decode("ascii")
    body = {
        "inputs": [
            {
                "name": "pr",  # prediction data
                "type": "csv",
                "data": prediction_data
            },
            {
                "name": "ar",  # add analysis result
                "type": "boolean",
                "data": True
            },
            {
                "name": "ad",  # add prediction data
                "type": "boolean",
                "data": True
            },
            {
                "name": "nc",  # without classification results
                "type": "boolean",
                "data": True
            }
        ]
    }

    response = requests.post(api_url, headers=headers, json=body)
    response_json = response.json()
    if 'outputs' in response_json:
        for output in response_json['outputs']:
            print(output['name'])
            print(base64.b64decode(output['data']).decode())
    else:
        print(response_json)

```

#### 実行例 2

Inference APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. body情報を記載したファイルを保存(body.txtとする)

3. リクエストする
$ curl -o "response.json" -H "x-api-key:{Get API Key APIから取得したAPI KEY}" -H "Content-Type: application/jsonn; charset=utf-8" -X POST -d @"{2.のファイルのフルパス}" -G {YOUR_API_URL}
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -H "Content-Type: application/jsonn; charset=utf-8" -X POST -d @body.txt https://user-api.predictionone.sony.biz/v1/groups/xxxxxxxxx/classifiers/xxxxxxxxx/inference
```
