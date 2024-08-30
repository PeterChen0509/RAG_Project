---
title: "Train Data Upload API Specifications"
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
    "Train",
    "train"
  ]
---

Prediction One can also use the REST API to create a prediction model. This process is executed by the series of API operations indicated below.
1.Get API Key API: Retrieves the API key
2.Train Data Upload API: Uploads the data
3.Create Model API: Executes training
4.Status Check API: Checks the status of training and retrieves a URL for downloading the results file after training

### Train Data Upload API

Retrieves the URL to upload the data for training.

#### URL

https://developer-api.predictionone.sony.biz/v1/external/data-sets/upload-url

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
| extension         | Extension of file to upload       |

##### body

Not used.

#### Response

##### body

The format is indicated below.

```
{
    "learn_data_set_upload_url": str,
    "eval_data_set_upload_url": str,
    "column_info_upload_url": str,
    "external_process_id": str
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

An example of executing the Train Data Upload API in Python is indicated below.

The Train Data Upload API is used to upload the "1_premium_service_purchase.csv" sample data.

```
import requests
import subprocess

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/data-sets/upload-url'
api_key = 'YOUR_API_KEY'

headers = {'x-api-key': api_key}

# When Using a Training File Only
train_data_file_path = 'train_data_file_path'
column_info_file_path = 'column_info.csv'

# Creating an Item Information File
with open(column_info_file_path, 'w', encoding='utf-8-sig') as f:
  f.write('column_name,column_type\n')
  f.write('premium_service(prediction_target),string\n')
  f.write('joined_on,date\n')
  f.write('age,float\n')
  f.write('sex,string\n')
  f.write('customer_rank,string\n')
  f.write('previous_purchases,float\n')
  f.write('coupon_usage_count,float\n')
  f.write('email_registration,string\n')


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

# When Using Evaluation Data
train_eval_data_file_path = 'YOUR_TRAIN_EVAL_DATA_FILE_PATH'
with open(train_eval_data_file_path, 'rb') as f:
  train_eval_data = f.read()
res = requests.put(train_eval_data_set_upload_url, data=train_eval_data)
```

#### Execution Example 2

An example of executing the curl command from the command prompt of the Train Data Upload API is indicated below.

```
1.Launch the command prompt.

2. Save a file including credential_type (with the name param.txt).

3. Make a request.
$ curl -o "response.json" -H "x-api-key:{API key retrieved from Get API Key API}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/data-sets/upload-url --data-urlencode filename@"{Full path of file in 3}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/data-sets/upload-url --data-urlencode filename@param.txt

4. Check the response.json file and retrieve retrain_job_id and upload_url.

5. Upload the file.
$ curl -X PUT --upload-file {File path of data set for training}{learn_data_set_upload_url retrieved in 4}
# When Also Using Evaluation Data
$ curl -X PUT --upload-file {File path of data set for evaluation} {eval_data_set_upload_url retrieved in 4}
$ curl -X PUT --upload-file {column information file path} {column_info_upload_url retrieved in 4}

```

