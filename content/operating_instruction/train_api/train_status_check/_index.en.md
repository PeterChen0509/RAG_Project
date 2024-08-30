---
title: "Train Status Check API Specifications"
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
    "REST API",
    "Training API",
    "Train Status Check",
    "train status check"
  ]
---

Prediction One can also use the REST API to create a prediction model. This process is executed by the series of API operations indicated below.
1.Get API Key API: Retrieves the API key
2.Train Data Upload API: Uploads the data
3.Train API: Executes training
4.Status Check API: Checks the status of training and retrieves a URL for downloading the results file after training

### Train Data Upload API

Retrieves the status of training.
This enables you to retrieve the URL for downloading the training results file when training is complete.

#### URL

https://developer-api.predictionone.sony.biz/v1/external/models/results

The HTTP GET method is used.

#### Request

##### header

| name              | Description              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| x-api-key         |The API key.       |

##### path parameter

Not used.

##### query parameter

| name              | Description              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| external_process_id    | external_process_id included in the response of the Train Data Upload API.|

##### body

Not used.

#### Response

##### body

The format is indicated below.

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
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | The API key does not exist. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | The API key is incorrect. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | The API key is incorrect. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This user may be deleted. | The user information may have been deleted. |

#### Execution Example 1

An example of executing the Train Status Check API in Python is indicated below.

This assumes that the Train Data Upload API has been executed.

```
import requests
import time
import zipfile

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/models/results'
api_key = 'YOUR_API_KEY'
# external_process_id Retrieved when Executing the Train Data Upload API
external_process_id = 'YOUR_EXTERNAL_PROCESS_ID'

headers = {'x-api-key': api_key}

# request
params = {'external_process_id': external_process_id}

while True:
  response = requests.get(api_url, params=daparamsta, headers=headers)
  response_json = response.json()
  status = response_json['status']
  if status == 'finished':
    break
  time.sleep(30)

result_url = response_json['result_url']

# Downloading the Results File
result_data = requests.get(result_url).content
with open('result.zip' ,mode='wb') as f:
  f.write(result_data)

# Checking the Results File
zf = zipfile.ZipFile('result.zip')
```

#### Execution Example 2

An example of executing the curl command from the command prompt of the Train Status Check API is indicated below.

```
1.Launch the command prompt.

2. Save a file including external_process_id (with the name params.txt).

3. Make a request.
$ curl -o "response.json" -H "x-api-key:{API key retrieved from Get API Key API}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/models/results --data-urlencode filename@"{Full path of file in 2}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET https://developer-api.predictionone.sony.biz/v1/external/models/results --data-urlencode filename@params.txt

4. Check the status in the response.json file.
If the status is finished, retrieve result_url.

5. Retrieve the training results.
$ curl -G GET {result_url retrieved in 4}
```

