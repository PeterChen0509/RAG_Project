---
title: "Retrain Model Switch API Specifications"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4
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
    "Retrain Model Switch ",
    "retrain model switch"
  ]
---

Prediction One can also use the REST API to update a prediction model (perform model retraining with the latest data). This process is executed by the series of API operations indicated below.
1.Retrain Data Upload API: Uploads data and executes retraining
2.Retrain Status Check API: Checks the status of retraining and retrieves a URL for downloading the results file after training
3.Retrain Model Switch API: Switches the model with API created to the retrained model

### Retrain Model Switch API

Updates a published model with a retrained model.

#### URL

https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{retrain_job_id}/update_model

The HTTP PUT method is used.

#### Request

##### header

| name              | Description                                       |
| :---------------- | :----------------------------------------- |
| x-api-key         | The API key. One is assigned to each model.

##### path parameter

| name              | Description                                       |
| :---------------- | :----------------------------------------- |
| retrain_job_id    | retrain_job_id. Issued when the upload URL is retrieved.       |

##### query parameter

Not used.

##### body

Not used.

#### Response

##### body

The format is indicated below.

```
{
  "metadata": {
    "retrain_job_id": str
  }
}
```

##### error message

| code       | error         | message                          | reason                         |
| :--------- | :------------ | :------------------------------- | :----------------------------- |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | invalid_api_key. | The API key does not exist. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Inactive_credential. | The API key is incorrect. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not_found_credential. | The API key is incorrect. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not found retrain job. | retrain_job_id is incorrect. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Not found classifier. | The model API may have been deleted. |
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | Retrain job is not finished. | Retraining is not complete. |

#### Execution Example 1

An example of executing the Retrain Model Switch API in Python is indicated below.

It assumes that retraining is complete and the execution results have been checked.

```
import requests

retrain_job_id = 'YOUR_RETRAIN_JOB_ID'
api_url = f'https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{YOUR_RETRAIN_JOB_ID}/update_model'
api_key = 'YOUR_API_KEY'

headers = {
    'x-api-key': api_key
}
response = requests.put(api_url, headers=headers)

```

#### Execution Example 2

An example of executing the curl command from the command prompt of the Retrain Model Switch API is indicated below.
It assumes that retraining is complete and the execution results have been checked.

```
1.Launch the command prompt.

2. Change the view to UTF-8.
$ chcp 65001

3. Make a request.
$ curl -H "x-api-key:{YOUR_API_KEY}" -X PUT https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{retrain_job_id}/update_model
ex) $ curl -H "x-api-key:xxxx-xxx-xxx-xxxx" -X PUT https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/{xxxx-xxxx-xxxx-xxxx}/update_model
```
