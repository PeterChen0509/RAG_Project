---
title: "Inference API Specifications"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1
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
    "Create API",
    "Publish API",
    "Deploy",
	"Prediction API"
  ]
---

The REST API can be used to run Prediction One predictions.

### Inference API

Predictions can be run on prediction data using a previously created model.
Create the endpoints (URLs), API keys, etc. required to run from the "{{% a_in "../model_api/" "API Creation Screen"%}}".
You can check the necessary information on the screen after the API is created.

#### URL

You can check the URL on the "{{% a_in "../model_api/" "API Creation Screen"%}}".

The HTTP POST method is used.

#### Request

##### header

| name              | Description                                        |
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key. One is assigned to each model.       |
| content-type      | Specify application/json; charset=utf-8 |

##### path parameter

Not used.

##### query parameter

Not used.

##### body

The format is indicated below.

```
{
	"inputs": [
		{
			"name": "pr",   # prediction data
			"type": "csv",
			"data": "6LfjeFlG/xxxxxx"
		},
		{
			"name": "ar",	# add analysis result
			"type": "boolean",
			"data": true
		},
		{
			"name": "ad",	# add prediction data
			"type": "boolean",
			"data": true
		},
		{
			"name": "nc",	# without classification results
			"type": "boolean",
			"data": true
		},
		{
			"name": "nr",	# without row numbers
			"type": "boolean",
			"data": true
		},
		{
			"name": "pc",
			"type": "string",
			"data": "column_name"
		}
	]
}
```

`inputs` parameter

| name          | type       |          | Description                                                                     |
| :------------ | :--------- | :------- | :---------------------------------------------------------------------- |
|  pr           | csv(base64)| required |  Value of the base64-encoded csv of the prediction file consisting of a row of the variable name of the data you wish to predict and one row of data 　|
|  ar           | boolean    | required |  Whether to calculate the reason for the prediction (output prediction_analysis.csv). Specify `true` if a prediction reason is required. Specify `false` to reduce the processing time without requiring a prediction reason.|
|  ad           | boolean    | required |  Whether to add prediction data to the output. Specify `true` to add it.|
|  nc           | boolean    | required |  Whether to output the classification results (in addition to the predicted probabilities) during binary and multiclass classification. Specify `true` if classification results are not required. `false` if classification results are required.　|
|  nr           | boolean    |          |  Whether to output row numbers in the prediction results. Specify `true` if the row number is not required. Specify `false` if the row number is required.|
|  pc           | string     |          |  Name of the variable to be attached to the left end of the prediction result.Specify one of the variable names contained in the prediction file specified with pr. |

#### Response

##### body

The format is indicated below.

```
{
    "version": str,
	"outputs": [
		{
			"name": "prediction_analysis.csv",
			"data": "6LfjeFlG/xxxxxx"
		},
		{
			"name": "prediction_valid.csv",
			"data": "6LfjeFlG/xxxxxx"
		}
	]
}
```

`outputs` parameter

| name                       | type       | Description                                                                     |
| :------------------------- | :--------- | :---------------------------------------------------------------------- |
|  prediction_valid.csv      | csv(base64)|  Value of the base64-encoded csv of the prediction results                                  　 |
|  prediction_analysis.csv   | csv(base64)|  Value of the base64-encoded csv of the prediction reasons. Included only if ar is set to `true` in Request. 　|

##### error message

| code       | error         | message                          | reason                         |
| :--------- | :------------ | :------------------------------- | :----------------------------- |
| 4001030101 | NOT_FOUND_CLASSIFIER| Not found classifier in classifiers table | classifier_id is incorrect |
| 4001030104 | BAD_REQUEST| Invalid request | Schema error. Please make sure your input is in the correct format. |
| 4031030201 | ACCESS_DENIED | Invalid API key | The API key is incorrect |
| 4031030201 | ACCESS_DENIED | Invalid classifier id | classifier_id not found |
| 4031030201 | ACCESS_DENIED | Not allowed source ip | Unable to access source IP of connection |
| 5031030101 | SERVICE_UNAVAILABLE_ERROR | status is not running (status: stopped) | Server is not running |

#### Execution Example

An example of executing the Inference API in Python is indicated below.

It is based on the assumption that the API has been created for a model created with the sample data "1_Premium Service Purchase.csv".
The prediction is calculated using the Inference API, using "2_Premium Service Purchase (for prediction).csv" as the prediction target.

```
import base64
import requests

prediction_data_file_path = '2_Premium Service Purchase (for prediction).csv'
api_url = 'YOUR_API_URL'
api_key = 'YOUR_API_KEY'

headers = {
    'x-api-key': api_key, 'content-type': 'application/json; charset=utf-8'}

with open(prediction_data_file_path, 'rb') as f:
    lines = f.readlines()

header = lines[0]
for line in lines[1:]:
    prediction_data = base64.b64encode(header + line).decode("ascii")
    body = {
        "inputs": [
            {
                "name": "pr",  # prediction data
                "type": "csv",
                "data": prediction_data
            },
            {
                "name": "ar",  # add analysis result
                "type": "boolean",
                "data": True
            },
            {
                "name": "ad",  # add prediction data
                "type": "boolean",
                "data": True
            },
            {
                "name": "nc",  # without classification results
                "type": "boolean",
                "data": True
            }
        ]
    }

    response = requests.post(api_url, headers=headers, json=body)
    response_json = response.json()
    if 'outputs' in response_json:
        for output in response_json['outputs']:
            print(output['name'])
            print(base64.b64decode(output['data']).decode())
    else:
        print(response_json)

```

