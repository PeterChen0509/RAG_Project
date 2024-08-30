---
title: "Retrain Data Upload APIの仕様"
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
    "学習API",
    "Retrain",
    "再学習API",
    "re train"
  ]
---

REST APIを使用して、Prediction Oneも予測モデルのアップデート（最新データによるモデルの再学習）ができます。以下の一連のAPIによって実行します。
1. Retrain Data Upload API：データアップロードし、再学習を実行
2. Retrain Status Check API：再学習の状態確認と、学習後の結果ファイルダウンロードURLの取得
3. Retrain Model Switch API：API作成済のモデルを再学習したモデルに切り替え

### Retrain Data Upload API

再学習用のデータをアップロードするURLを取得します。
ファイルアップロードが完了すると自動で再学習が実行されます。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/upload_url

HTTPメソッドは、GETです。

#### Request

##### header

| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key。モデル毎に１つ割り当てられる。       |

##### path parameter

ありません。

##### query parameter

| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| filename         | アップロードするファイル名       |

##### body

ありません。

#### Response

##### body

以下のフォーマットです。

```
{
    "retrain_job_id": str,
	"upload_url": str
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
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This job may be deleted. | ジョブが削除されている可能性がある |
| 5001000201 | PREDA_EXTERNAL_INTERNAL_SERVER_ERROR  | Not found configuration_file. | 設定ファイルが削除されている可能性がある |

#### 実行例 1

Retrain Data Upload APIのpythonによる実行例が以下となります。

```
import requests
import tempfile
import zipfile
import subprocess

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/upload_url'
api_key = 'YOUR_API_KEY'

headers = {'x-api-key': api_key}


# 学習ファイルのみの場合​
re_train_data_file_path = 'YOUR_RE_TRAIN_DATA_FILE_PATH'
re_train_data_file_name = 'YOUR_RE_TRAIN_DATA_FILE_NAME'

# request
params = {'filename': re_train_data_file_name}
response = requests.get(api_url, params=params, headers=headers)
response_json = response.json()
retrain_job_id = response_json['retrain_job_id']
upload_url = response_json['upload_url']

# upload_file
with open(re_train_data_file_path, 'rb') as f:
  data = f.read()
res = requests.put(upload_url, data=data)

# 学習ファイルと評価ファイルを使用する場合
re_train_zip_file_name = 'YOUR_RE_TRAIN_ZIP_FILE_NAME'
re_train_data_file_name = 'YOUR_RE_TRAIN_DATA_FILE_NAME'
re_train_data_file_path = 'YOUR_RE_TRAIN_DATA_FILE_PATH'
re_train_eval_data_file_name = 'YOUR_RE_TRAIN_EVAL_DATA_FILE_NAME'
re_train_eval_data_file_path = 'YOUR_RE_TRAIN_EVAL_DATA_FILE_PATH'

"""
dir_name
  |   |--train_src
  |   |   |--train_data.csv
  |   |--eval_src
  |   |   |--eval_data.csv
"""

with tempfile.TemporaryDirectory() as temp:
  zip_file_path = f'{temp}/{re_train_zip_file_name}'
	with zipfile.ZipFile(zip_file_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
		zf.write(re_train_data_file_path, arcname=f'train_src/{re_train_data_file_name}')
		zf.write(re_train_eval_data_file_path, arcname=f'eval_src/{re_train_eval_data_file_name}')

  # request
  params = {'filename': re_train_zip_file_name}
  response = requests.get(api_url, params=params, headers=headers)
  response_json = response.json()
  retrain_job_id = response_json['retrain_job_id']
  upload_url = response_json['upload_url']

  # upload_file
  with open(zip_file_path, 'rb') as f:
    data = f.read()
  res = requests.put(upload_url, data=data)
  ret = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

#### 実行例 2

Retrain Data Upload APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. 表示をUTF-8に変更
$ chcp 65001

3. ファイル名を記載したファイルをUTF-8で保存(param.txtとする)

4. リクエストする
$ curl -o "response.json" -H "x-api-key:{YOUR_API_KEY}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/upload_url --data-urlencode filename@"{3.のファイルのフルパス}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/upload_url --data-urlencode filename@param.txt

5. response.jsonを確認しretrain_job_idとupload_urlを取得

6. ファイルをアップロード
$ curl -X PUT --upload-file {再学習用データセットファイルパス} {5で取得したupload_url}
```

