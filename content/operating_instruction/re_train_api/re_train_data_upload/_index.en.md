---
title: "Retrain Data Upload API Specifications"
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
    "Training API",
    "Retrain",
    "Retraining API",
    "re train"
  ]
---

Prediction One can also use the REST API to update a prediction model (perform model retraining with the latest data). This process is executed by the series of API operations indicated below.
1.Retrain Data Upload API: Uploads data and executes retraining
2.Retrain Status Check API: Checks the status of retraining and retrieves a URL for downloading the results file after training
3.Retrain Model Switch API: Switches the model with API created to the retrained model

### Retrain Data Upload API

Retrieves the URL to upload the data for retraining.
When the file upload is complete, retraining is automatically executed.

#### URL

https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/upload_url

The HTTP GET method is used.

#### Request

##### header

| name              | Description              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| x-api-key         | The API key. One is assigned to each model.       |

##### path parameter

Not used.

##### query parameter

| name              | Description              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| filename         | Name of file to upload       |

##### body

Not used.

#### Response

##### body

The format is indicated below.

```
{
    "retrain_job_id": str,
	"upload_url": str
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
| 4001000204 | PREDA_EXTERNAL_BAD_REQUEST | This job may be deleted. | The job may have been deleted. |
| 5001000201 | PREDA_EXTERNAL_INTERNAL_SERVER_ERROR  | Not found configuration_file. | The configuration file may have been deleted. |

#### Execution Example 1

An example of executing the Retrain Data Upload API in Python is indicated below.

```
import requests
import tempfile
import zipfile
import subprocess

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/upload_url'
api_key = 'YOUR_API_KEY'

headers = {'x-api-key': api_key}


# When Using a Training File Only
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

# When Using Both a Training File and Evaluation File
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

#### Execution Example 2

An example of executing the curl command from the command prompt of the Retrain Data Upload API is indicated below.

```
1.Launch the command prompt.

2. Change the view to UTF-8.
$ chcp 65001

3. Save a file indicating the file name in the UTF-8 format (with the name param.txt).

4. Make a request.
$ curl -o "response.json" -H "x-api-key:{YOUR_API_KEY}" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/upload_url --data-urlencode filename@"{Full path of file in 3}"
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -X GET -G https://developer-api.predictionone.sony.biz/v1/external/retrain_jobs/upload_url --data-urlencode filename@param.txt

5. Check the response.json file and retrieve retrain_job_id and upload_url.

6. Upload the file.
$ curl -X PUT --upload-file {File path of data set for retraining} {upload_url retrieved in 5}
```

