---
title: "Retrain Status Check APIの仕様"
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
    "再学習API",
    "Retrain Status Check",
    "retrain status check"
  ]
---

REST APIを使用して、Prediction Oneも予測モデルのアップデート（最新データによるモデルの再学習）ができます。以下の一連のAPIによって実行します。
1. Retrain Data Upload API：データアップロードし、再学習を実行
2. Retrain Status Check API：再学習の状態確認と、学習後の結果ファイルダウンロードURLの取得
3. Retrain Model Switch API：API作成済のモデルを再学習したモデルに切り替え

### Retrain Status Check API

再学習用状況を取得します。
再学習が完了したときに再学習結果ファイルダウンロードURLが取得できます。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{retrain_job_id}

HTTPメソッドは、GETです。

#### Request

##### header

| name              | 説明                                       |
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key。モデル毎に１つ割り当てられる。       |

##### path parameter

| name              | 説明                                       |
| :---------------- | :----------------------------------------- |
| retrain_job_id    | retrain_job_id。アップロードURL取得時に発行される。       |

##### query parameter

ありません。

##### body

ありません。

#### Response

##### body

以下のフォーマットです。

```
{
  "status": str,
  Optional("model_id"): int,
  Optional("message"): str,
  Optional("download_url"): str,
  "metadata": {
    "retrain_job_id": str
  }
}
```

##### error message

| code       | error         | message                | reason                 |
| :--------- | :------------ | :--------------------- | :--------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | APIキーが存在しない |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not found retrain job. | retrain_job_idが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This job may be deleted. | ジョブが削除されている可能性がある |

#### 実行例 1

Retrain Status Check APIのpythonによる実行例が以下となります。

Get retrain job dataset upload url APIの実行を行った状態を前提としています。

```
import requests
​
retrain_job_id = 'YOUR_RETRAIN_JOB_ID'
api_url = f'https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{YOUR_RETRAIN_JOB_ID}'
api_key = 'YOUR_API_KEY'
​
headers = {
    'x-api-key': api_key
}
​
response = requests.get(api_url, headers=headers)
response_json = response.json()
status = response_json['status']

download_url = None
while True:
  if response_json['status'] == 'job_finished':
    download_url = response_json['download_url']

  if download_url:
    response = requests.get(download_url)
    with open(result_file_path, 'w') as f:
      print(response.content)
      
```


#### 実行例 2

Retrain Status Check APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。
Get retrain job dataset upload url APIの実行を行った状態を前提としています。

```
1. コマンドプロンプトを立ち上げる

2. 表示をUTF-8に変更
$ chcp 65001

3. リクエストする
$ curl -o "response.json" -H "x-api-key:{YOUR_API_KEY}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{retrain_job_id}
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{xxxx-xxxx-xxxx-xxxx}

4. response.jsonを確認statusを確認
statusがjob_finishedの場合にdownload_urlを取得

5. 再学習結果を取得
$ curl -G GET {4.で取得したdownload_url}
```