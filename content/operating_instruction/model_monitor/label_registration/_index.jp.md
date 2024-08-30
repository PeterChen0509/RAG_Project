---
title: "正解を登録する方法"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 5
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
    "モデルの監視",
    "モデルの運用",
    "本番環境",
    "Additional Info API",
    "正解の登録"
  ]
---

正解の登録APIを用いて、予測したデータに対し正解ラベルを付与することができます。

### Additional Info API

Additional Info API を使用することで、{{% a_in "../../model_api/inference/" "Inference API"%}} で予測したデータに対して正解ラベルを付与することができます。これにより、予測したデータに対する予測精度を表示したり学習時からのモデルの劣化の検知や期間に応じた予測精度を把握することができます。過去の予測結果は、モデルの監視タブの出力ボタンから「過去の予測データと予測結果を保存」を選択することでダウンロードすることができ、この中に含まれる transactionID というキーを用いて過去の予測と正解を紐づけることができます。

#### URL

正解の登録APIのURLは<br>
https://developer-api.predictionone.sony.biz/v1/external/additional_info
<br>
で、HTTPメソッドは、PATCHです。

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
    "additional_info": [{
      "transaction_id": "xxxxxxxxx",
      "ground_truth": "1"
    ]}
}
```

`additional_info` の各要素に指定するパラメータ(`additional_info` にリストとして複数の要素を含めることで複数の正解を同時に登録することが可能です)

| name          | type       |          | 説明                                                                     |
| :------------ | :--------- | :------- | :---------------------------------------------------------------------- | 
|  transaction_id           | string| required |  正解を登録したいデータに対するID。モデルの監視タブの出力ボタンから「過去の予測データと予測結果を保存」を選択し transactionID 列を見ることで、過去に予測したデータ(行)に対するIDを知ることができる。 　|
|  ground_truth           | string    | required |  予測したデータに対して登録する正解データ。二値分類または多値分類の場合は学習データに正解として含まれる文字列を指定する必要がある。数値予測の場合は数値に変換できる文字列である必要がある。 |

#### Response

##### body

以下のフォーマットです。すべて登録できた場合はレスポンスは空のリストとなります。

```
{
    "error_result": [{
      "transaction_id": "xxxxxxxxx",
      "code": "400100204",
      "message": "invalid_api_key"
	}]
}
```

##### error message

| code       | error         | message                          | reason                         |
| :--------- | :------------ | :------------------------------- | :----------------------------- |
| 4001000204 | BAD_REQUEST | invalid_api_key. | APIキーが存在しない |
| 4001000204 | BAD_REQUEST | Inactive_credential. | APIキーが間違っている |
| 4001000204 | BAD_REQUEST | Not_found_credential. | APIキーが間違っている |
| 4001000204 | BAD_REQUEST | Expired_classifier. | APIの有効期限切れ |
| 4001000204 | BAD_REQUEST | This user may be deleted. | ユーザー情報が削除されている可能性がある |
| 4001000204 | BAD_REQUEST | This model may be deleted. | モデルが削除されている可能性がある |
| 4001000204 | BAD_REQUEST | This job may be deleted. | ジョブが削除されている可能性がある |
| 4001000204 | BAD_REQUEST | Not found inference additional info. | 正解の登録ができません |
| 4001000204 | BAD_REQUEST | Not in classify value. | 正解が間違っている可能性がある |
| 4001000204 | BAD_REQUEST | Not format value. | 正解が間違っている可能性がある |
| 5001000201 | INTERNAL_SERVER_ERROR | Not found configuration_file. | 設定ファイルが削除されている可能性がある |

#### 実行例

正解の登録APIのpythonによる実行例が以下になります。サンプルデータの「1_プレミアムサービス購入.csv」で作成したモデルに対して、API作成を行った状態を前提としています。また、予測対象として「2_プレミアムサービス購入（予測用）.csv」を利用して、Inference APIの実行例をもとに予測を実行した状態を前提としています。(参考：{{% a_in "../../model_api/inference/" "Inference API"%}})

まず、過去の予測のtransactionIDを入手するために、モデルの監視タブの出力ボタンから「過去の予測データと予測結果を保存」を選択して過去の予測結果のcsvファイル(inference_data.csv)をダウンロード行います。その後、それらのtransactionIDに正解を紐づけるために正解の登録APIを実行します。この例では先頭の50行の正解が「購入あり」となっていて、51-100行目の正解が「購入なし」だった場合の例となります。

```

import json
import requests
import pandas as pd

api_key = 'YOUR_API_KEY'
api_url = 'https://developer-api.predictionone.sony.biz/v1/external/additional_info'
transaction_path = 'inference_data.csv'
data = pd.read_csv(transaction_path, encoding='utf-8-sig', engine='python')

header = {"x-api-key": api_key, "Content-Type": "application/json; charset=UTF-8"}
body = {'additional_info': []}
for i, transaction_id in enumerate(data['transactionID'].values):
    if i < 50:
        body['additional_info'].append({"transaction_id": transaction_id, "ground_truth": '購入あり'})
    elif i < 100:
        body['additional_info'].append({"transaction_id": transaction_id, "ground_truth": '購入なし'})
    else:
        break
body = json.dumps(body, ensure_ascii=True)
body = body.encode('utf-8')
response = requests.patch(api_url, data=body, headers=header)
print(response.json())
```
