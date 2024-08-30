---
title: "Train API Specifications"
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
    "Train",
    "train"
  ]
---

Prediction One can also use the REST API to create a prediction model. This process is executed by the series of API operations indicated below.
1.Get API Key API: Retrieves the API key
2.Train Data Upload API: Uploads the data
3.Train API: Executes training
4.Status Check API: Checks the status of training and retrieves a URL for downloading the results file after training

### Train API

Creates a prediction model.

#### URL

https://developer-api.predictionone.sony.biz/v1/external/models

The HTTP GET method is used.

#### Request

##### header

| name              | Description              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| x-api-key         | API Key。       |

##### path parameter

Not used.

##### query parameter

Not used.

##### body

| name              | Description              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| external_process_id    | external_process_id included in the response of the Train Data Upload API.|
| name    | Prediction model name|
| config    | See the config below|

#### config
| name              | Description              　　　　　　　　　　　　　　|
| :---------------- | :----------------------------------------- |
| tc    | The name of the item used as the item to predict (prediction target).|
| tt    | The prediction type. Specify ‘binary_classification’ for binary classification, ‘multi_classification’ for multiclass classification, or ‘regression’ for numerical prediction.|
| tv    | The prediction value. Required if the prediction type specifies binary classification. Otherwise not specified.|
| cv    | The division count for k division cross-validation. If ‘0’ is specified, whether to perform cross-validation and the division count are automatically determined based on the training data. If ‘-1’ is specified, cross-validation is always performed but the division count is automatically determined based on the training data. If ‘1’ is specified, cross-validation is not performed. If ‘2’ or higher is specified, k division cross-validation is performed with the specified number k. If omitted, the operation is the same as if ‘0’ was specified.|
| im    | Whether to correct value bias in the item to predict. Can only be set when Prediction Type is Classification. Specify ‘true’ to perform correction or ‘false’ to not perform correction. If omitted, the operation is the same as if ‘false’ was specified.|
| tsm    | Whether to use the time series prediction mode. Specify ‘true’ to use the time series prediction mode, or ‘false’ to not use the time series prediction mode. If omitted, the operation is the same as if ‘false’ was specified. The time series prediction mode can only be used when the prediction type (-tt) is set to numerical prediction (regression).|
| tsu    | The time unit for time series prediction. Specify ‘year’ for year, ‘month’ for month, ‘day’ for day, ‘hour’ for hour, ‘minute’ for minute, or ‘eom’ for the last day of the month. To automatically determine the unit, do not specify this option (-tsu).|
| tsc    | The time information item of the item to predict (prediction target) for time series prediction. Required if using time series prediction mode (-tsm true).|
| tsi    | The time interval for time series prediction. Specify an integer. The time unit specified by -tsu is used. For example, for a 2-month interval, specify ‘-tsu month -tsi 2’. To automatically determine the interval, do not specify this option (-tsi), or specify ‘0’.|
| tsf    | The start of the prediction period for time series prediction. Required if using time series prediction mode (-tsm true). Specify an integer of 1 or greater. The time unit specified by -tsu is used. For example, to specify from two months ahead to four months ahead as the prediction period, specify ‘-tsu month -tsf 2 -tst 4’.|
| tst    | The end of the prediction period for time series prediction. Required if using time series prediction mode (-tsm true). Specifies an integer greater than or equal to the value specified by -tsf. The time unit specified by -tsu is used. For example, to specify from two months ahead to four months ahead as the prediction period, specify ‘-tsu month -tsf 2 -tst 4’.|
| tss    | The time series item for time series prediction. Only specify this when there is a time series item.|
| tsin    | Whether the prediction period for time series prediction obtains items other than the item to predict. Specify ‘true’ to obtain all items or ‘false’ to not obtain all items. If omitted, the operation is the same as if ‘false’ was specified. If there are both items to obtain and items to not obtain, specify exceptions using the -tsine option indicated below.<br/>(To perform the same training as version 3.0 or earlier, specify ‘`true`’.) For details, see "{{% a_in "../../../tips/new_features/timeseries_features/" "Items other than items to predict" %}}".)|
| tsine    | Specifies exceptions for whether to obtain items other than the item to predict, in the prediction period for time series prediction. When ‘true’ is specified for the -tsin option, specifies items to not obtain values for. When ‘false’ is specified for the -tsin option, specifies items to obtain values for. To specify multiple items, use the -tsine option multiple times (like "-tsine {item name 1} -tsine {item name 2}").|

#### Response

##### body

The format is indicated below.

```
{
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

An example of executing the Train API in Python is indicated below.

This assumes that the Train Data Upload API was executed and training was performed using the "1_premium_service_purchase.csv" sample data.

```
import requests

api_url = 'https://developer-api.predictionone.sony.biz/v1/external/models'
api_key = 'YOUR_API_KEY'
# external_process_id retrieved when executing the Train Data Upload API
external_process_id = 'YOUR_EXTERNAL_PROCESS_ID'

headers = {'x-api-key': api_key}

# request

body = {
  'external_process_id': external_process_id,
  'name': 'MODEL_NAME',
  'config': {
    'tc':'Premium service (prediction target)',
    'tt':'binary_classification',
    'tv':'Purchased',
    'cv':"2"
  }
}
response = requests.post(api_url, data=data, headers=headers)
response_json = response.json()
external_process_id = response_json['external_process_id']
```

#### Execution Example 2

An example of executing the curl command from the command prompt of the Train API is indicated below.

```
1.Launch the command prompt.

2. Save a file including the body information (with the name body.txt).

3. Make a request.
$ curl -o "response.json" -H "x-api-key:{API key retrieved from Get API Key API}" -H "Content-Type: application/json" -X POST -d @"{Full path of file in 2}" -G https://developer-api.predictionone.sony.biz/v1/external/models
ex) $ curl -o "response.json" -H "x-api-key:xxxx-xxx-xxx-xxxx" -H "Content-Type: application/json" -X POST -d @body.txt https://developer-api.predictionone.sony.biz/v1/external/models
```

