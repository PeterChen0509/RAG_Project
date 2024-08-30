---
title: "Get API Key API Specifications"
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

Prediction One can also use the REST API to create a prediction model. This process is executed by the series of API operations indicated below.
1.Get API Key API: Retrieves the API key
2.Data Upload API: Uploads the data
3.Create Model API: Executes training
4.Status Check API: Checks the status of training and retrieves a URL for downloading the results file after training

### Get A Key API

Retrieves the API key.

#### URL

https://developer-api.predictionone.sony.biz/v1/external/api-key

The HTTP GET method is used.

#### Request

##### header

| name              | Description              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| x-api-key         | Secret Key。            |

##### path parameter

Not used.

##### query parameter

| name              | Description              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| credential_type         | retrain: Retrain, train: Learning|
| model_id         | Required when retrain is specified in credential_type. Specify the {{% a_in "../../model_api/" "model ID of the model API to retrain"%}}.|

##### body

Not used.

#### Response

##### body

The format is indicated below.

```
{
  "api_key": str,
	"end_date": str
}
```

##### error message

| code       | error       | message               | reason               |
| :--------- | :---------- | :-------------------- | :------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | The API key does not exist. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | The API key is incorrect. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | The API key is incorrect. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This user may be deleted. | The user information may have been deleted. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This model may be deleted. | The model may have been deleted. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Model id is required. | The model ID may not be specified. |

#### Execution Example 1

An example of executing the Get API Key API in Python is indicated below.

```
import requests

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/api-key'
secret_key = 'YOUR_SECRET_KEY'

headers = {'x-api-key': secret_key}


# When retraining
params = {'credential_type': 'retrain', 'model_id': YOUR_MODEL_ID}

# When training
params = {'credential_type': 'train'}

# request
response = requests.get(api_url, params=params, headers=headers)
response_json = response.json()
api_key = response_json['api_key']
```

#### Execution Example 2

An example of executing the curl command from the command prompt of the Get API Key API is indicated below.

```
1.Launch the command prompt.

2. Save a file including credential_type (with the name param.txt).

3. Make a request.
$ curl -o "response.json" -H "x-api-key:{Secret key retrieved from screen}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/api-key --data-urlencode filename@"{Full path of file in 3}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/api-key --data-urlencode filename@param.txt

4. Check the response.json file and retrieve api_key.
```

