---
title: "Get Model APIの仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 7
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

### Get Model API

予測モデルを取得します。

#### URL

https://developer-api.predictionone.sony.biz/v1/external/models

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
  "models": [{
    "model_id": int,
    "owner_user_id": str,
    "target_type": Or(str, None),
    "name": Or(str, None),
    "version": Or(str, None),
    "config": 下記config参照,
    "is_api_option": bool,
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

#### config
| name              | 説明              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| tc    | 予測したい項目(予測ターゲット)として使用する項目の名前。|
| tt    | 予測タイプ。二値分類ならbinary_classification、多値分類ならmulti_classification、数値予測ならregressionを指定する。|
| tv    | 予測値。予測タイプで二値分類を指定した場合は必須。それ以外は指定なし。|
| cv    | k 分割交差検証の分割数。0を指定すると学習データに基づき、交差検証を行うかどうかとその分割数を自動決定する。-1を指定すると交差検証は必ず行うが、その分割数は学習データに基づき自動決定する。1を指定すると交差検証を行わない。2以上を指定すると、指定された数 k で k 分割交差検証を行う。省略した場合は0指定と同じ。|
| im    | 予測したい項目の値の偏りを補正するかどうか。予測タイプが分類のときのみ設定可能。補正する場合はtrue、補正しない場合はfalseを指定。省略した場合はfalseと同じ。|
| tsm    | 時系列予測モードを使用するかどうか。時系列予測モードを使用する場合はtrueを指定、使用しない場合はfalseを指定する。省略した場合はfalseと同じ。時系列予測モードが使用できるのは予測タイプ(-tt)が数値予測(regression)のときのみ。|
| tsu    | 時系列予測の時間単位。年の場合year、月の場合month、日の場合day、時間の場合hour、分の場合minute、月末日の場合eomを指定する。自動判定の場合は、本オプション(-tsu)を指定しない。|
| tsc    | 時系列予測の予測したい項目(予測ターゲット)の時間情報項目。時系列予測モードを使用する(-tsm true)場合は必須。|
| tsi    | 時系列予測の時間間隔。整数を指定する。時間単位は-tsu で指定したものが使用される。たとえば 2 ヶ月間隔の場合、-tsu month -tsi 2 と指定する。自動判定の場合は、本オプション(-tsi)を指定しないか、0 を指定する。|
| tsf    | 時系列予測の予測期間の開始時期。時系列予測モードを使用する(-tsm true)の場合必須。1 以上の整数を指定する。時間単位は-tsu で指定したものが使用される。たとえば、予測期間が「2 ヶ月後から 4 ヶ月後まで」の場合、-tsu month -tsf 2 -tst 4 と指定する。|
| tst    | 時系列予測の予測期間の終了時期。時系列予測モードを使用する(-tsm true)の場合必須。-tsf で指定した値以上の整数を指定する。時間単位は-tsu で指定したものが使用される。たとえば、予測期間が「2 ヶ月後から 4 ヶ月後まで」の場合、-tsu month -tsf 2 -tst 4 と指定する。|
| tss    | 時系列予測の系列項目。系列項目がある場合のみ指定する。|
| tsin    | 時系列予測の予測期間について、予測したい項目以外の項目が手に入るかどうか。全ての項目が手に入る場合はtrue、全て手に入らない場合はfalseを指定する。省略した場合はfalseと同じ。手に入る項目、手に入らない項目が混在する場合は次の-tsineで例外を指定する。<br/>(v3.0以前と同じ学習を行いたい場合は、`true`を指定する。詳細は、{{% a_in "../../../tips/new_features/timeseries_features/" "予測したい項目以外の項目" %}}を参照)|
| tsine    | 時系列予測の予測期間について、予測したい項目以外の項目が手に入るかどうか、例外項目を指定する。-tsinがtrueの場合は、予測期間について値が手に入らない項目を指定する。-tsinがfalseの場合は、予測期間について値が手に入る項目を指定する。複数の項目を指定したい場合は、-tsine {項目名1} -tsine {項目名2} …のように複数回用いる。|

##### error message

| code       | error       | message               | reason               |
| :--------- | :---------- | :-------------------- | :------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | APIキーが存在しない |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | APIキーが間違っている |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This user may be deleted. | ユーザー情報が削除されている可能性がある |

#### 実行例 1

Get Model APIのpythonによる実行例が以下となります。

```
import requests

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/models'
api_key = 'YOUR_API_KEY'

headers = {'x-api-key': api_key}
params = {'offset': 0, 'limit': 30}

# request
response = requests.get(api_url, params=params, headers=headers)
response_json = response.json()
```

#### 実行例 2

Get Model APIのコマンドプロンプトからcurlコマンドによる実行例が以下となります。

```
1. コマンドプロンプトを立ち上げる

2. offset, limitを記載したファイルを保存(params.txtとする)

3. リクエストする
$ curl -o "response.json" -H "x-api-key:{Get API Key APIから取得したAPI KEY}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/models --data-urlencode filename@"{2.のファイルのフルパス}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET https://developer-api.predictionone.sony.biz/v1/external/models --data-urlencode filename@params.txt
```

