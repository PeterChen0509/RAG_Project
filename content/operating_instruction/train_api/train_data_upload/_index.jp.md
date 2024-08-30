---
title: "Train Data Upload APIの仕様"
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
    "学習API",
    "Train",
    "train"
  ]
---

REST APIを使用して、Prediction Oneも予測モデルの作成ができます。以下の一連のAPIによって実行します。
1. Get API Key API：API KEYを取得
2. Train Data Upload API：データをアップロード
3. Train Data Set Info: 学習用データセットの情報を取得
4. Create Model API：学習の実行
5. Status Check API：学習の状態確認と、学習後の結果ファイルダウンロードURLの取得

### Train Data Upload API

学習用のデータをアップロードするURLを取得します。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/data-sets/upload-url

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
| extension         | アップロードするファイル拡張子       |

##### body

ありません。

#### Response

##### body

以下のフォーマットです。

```
{
    "learn_data_set_upload_url": str,
    "eval_data_set_upload_url": str,
    "column_info_upload_url": str,
    "external_process_id": str
}
```

| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| learn_data_set_upload_url         | 学習用データセットアップロードURL       |
| eval_data_set_upload_url         |  評価用データセットアップロードURL      |
| column_info_upload_url         | カラム情報アップロードURL       |
| external_process_id         | プロセスID       |

##### error message

| code       | error       | message               | reason               |
| :--------- | :---------- | :-------------------- | :------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | APIキーが存在しない |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This user may be deleted. | ユーザー情報が削除されている可能性がある |

#### 実行例 1

Train Data Upload APIのpythonによる実行例が以下となります。

Train Data Upload APIを使用してサンプルデータの「1_プレミアムサービス購入.csv」をアップロードします。

```
import requests
import subprocess

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/data-sets/upload-url'
api_key = 'YOUR_API_KEY'

headers = {'x-api-key': api_key}

# 学習ファイルのみの場合​
train_data_file_path = 'train_data_file_path'
column_info_file_path = 'column_info.csv'

# 項目情報ファイルの作成
with open(column_info_file_path, 'w', encoding='utf-8-sig') as f:
  f.write('column_name,column_type\n')
  f.write('プレミアムサービス(予測対象),string\n')
  f.write('入会時期,date\n')
  f.write('年齢,float\n')
  f.write('性別,string\n')
  f.write('顧客ランク,string\n')
  f.write('過去購入額,float\n')
  f.write('クーポン利用回数,float\n')
  f.write('メアド登録,string\n')


# request
params = {'extension': 'csv'}
response = requests.get(api_url, params=params, headers=headers)
response_json = response.json()
train_data_set_upload_url = response_json['learn_data_set_upload_url']
train_eval_data_set_upload_url = response_json['eval_data_set_upload_url']
column_info_upload_url = response_json['column_info_upload_url']
external_process_id = response_json['external_process_id']

# upload_file
with open(train_data_file_path, 'rb') as f:
  train_data = f.read()
res = requests.put(train_data_set_upload_url, data=train_data)

with open(column_info_file_path, 'rb') as f:
  column_info_data = f.read()
res = requests.put(column_info_upload_url, data=column_info_data)

# 評価用データを利用する場合
train_eval_data_file_path = 'YOUR_TRAIN_EVAL_DATA_FILE_PATH'
with open(train_eval_data_file_path, 'rb') as f:
  train_eval_data = f.read()
res = requests.put(train_eval_data_set_upload_url, data=train_eval_data)
```

#### 実行例 2

Train Data Upload APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. credential_typeを記載したファイルを保存(param.txtとする)

3. リクエストする
$ curl -o "response.json" -H "x-api-key:{Get API Key APIから取得したAPI KEY}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/data-sets/upload-url --data-urlencode filename@"{3.のファイルのフルパス}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/data-sets/upload-url --data-urlencode filename@param.txt

4. response.jsonを確認しretrain_job_idとupload_urlを取得

5. ファイルをアップロード
$ curl -X PUT --upload-file {学習用データセットファイルパス} {4で取得したlearn_data_set_upload_url}
# 評価用データも使用する場合
$ curl -X PUT --upload-file {評価用データセットファイルパス} {4で取得したeval_data_set_upload_url}
$ curl -X PUT --upload-file {カラム情報ファイルパス} {4で取得したcolumn_info_upload_url}

```

