---
title: "Retrain Status Check API Specifications"
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
    "Training API",
    "Retraining API",
    "Retrain Status Check",
    "retrain status check"
  ]
---

Prediction One can also use the REST API to update a prediction model (perform model retraining with the latest data). This process is executed by the series of API operations indicated below.
1.Retrain Data Upload API: Uploads data and executes retraining
2.Retrain Status Check API: Checks the status of retraining and retrieves a URL for downloading the results file after training
3.Retrain Model Switch API: Switches the model with API created to the retrained model

### Retrain Status Check API

Retrieves the status of retraining.
This enables you to retrieve the URL for downloading the retraining results file when retraining is complete.

#### URL

https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{retrain_job_id}

The HTTP GET method is used.

#### Request

##### header

| name              | Description                                       |
| :---------------- | :----------------------------------------- |
| x-api-key         | The API key. One is assigned to each model.       |

##### path parameter

| name              | Description                                       |
| :---------------- | :----------------------------------------- |
| retrain_job_id    | retrain_job_id。 Issued when the upload URL is retrieved.       |

##### query parameter

Not used.

##### body

Not used.

#### Response

##### body

The format is indicated below.

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
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | The API key does not exist. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | The API key is incorrect. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | The API key is incorrect. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not found retrain job. | retrain_job_id is incorrect. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This job may be deleted. | The job may have been deleted. |

#### Execution Example 1

An example of executing the Retrain Status Check API in Python is indicated below.

This assumes that the Get retrain job dataset upload url API has been executed.

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


#### Execution Example 2

An example of executing the curl command from the command prompt of the Retrain Status Check API is indicated below.
This assumes that the Get retrain job dataset upload url API has been executed.

```
1.Launch the command prompt.

2. Change the view to UTF-8.
$ chcp 65001

3. Make a request.
$ curl -o "response.json" -H "x-api-key:{YOUR_API_KEY}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{retrain_job_id}
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{xxxx-xxxx-xxxx-xxxx}

4. Check the status in the response.json file.
If the status is job_finished, retrieve download_url.

5. Retrieve the retraining results.
$ curl -G GET {download_url retrieved in 4}
```