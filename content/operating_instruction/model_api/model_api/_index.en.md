---
title: "API Creation Screen"
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
    "Create API",
    "Publish API",
    "Deploy"
  ]
---

Clicking the [Create API] tab of a created prediction model takes you to this screen.
For the API specifications, refer to "{{% a_in "../inference/" "Inference API Specifications"%}}."

![](../../img_en/t_slide103.png)

{{% div_method_area "Create prediction API" %}}
{{% step_n2 1 "Clicking the [Create API] tab with the model that you want to create a prediction API for selected takes you to this screen." %}}
{{% step_n2 2 "Click the [Launch] button" %}}
{{% step_n2 3 "Select the API type in the [Start API creation] window, then click the [Start] button." %}}

- Create API: Creates an official API. It can be used by purchasing the API option. You can create one API for each API option you purchase. This type cannot be selected with the trial version.
- Create trial API: Creates a trial API. The created API can be used for up to 100 requests.

{{% step_n2 4 "The building API screen will be displayed. It takes about 5 to 20 minutes to build the API. The prediction API can be used after building is complete." %}}
{{% /div_method_area %}}

![](../../img_en/t_slide104.png)

The following screen is displayed when the API has been created.

![](../../img_en/t_slide105.png)

{{% div_method_area "Check prediction API information" %}}
Check [API information].

- API type: Displays whether the API is an official API or trial API.
- Model ID: The ID of the model.
- API ID: The ID of the API.
- API URL: The endpoint URL of the API.
- API Key: The API key.
- IP whitelist: The IP address whitelist. Only the IP addresses registered to the whitelist can use this API. To allow all IP addresses, specify ‘0.0.0.0/0’.
- Date/time created: The date and time that the API was created.
{{% /div_method_area %}}

{{% div_method_area "Check prediction API request count" %}}
Check [API request count]. The number of requests is counted daily and displayed as a graph.

- Status 200: The number of requests without an error.
- Status 4xx or 5xx: The number of requests with an error. 4xx refer to client errors and 5xx refer to server errors, but the total count is displayed.
{{% /div_method_area %}}

{{% div_method_area "Check prediction API status" %}}
Check [API status].

- Building: Building the API.
- Updating: Updating the API.
- Operating: The API is operating. Requests to the API can be processed in this state.
- Stopped: The API is stopped. Requests to the API cannot be processed in this state.
- Deleting: Deleting the API.
{{% /div_method_area %}}

{{% div_method_area "Configure IP whitelist of prediction API" %}}
{{% step_n2 1 "Click the [Configure IP whitelist] button" %}}
{{% step_n2 2 "In the text box of the displayed window, enter the whitelist of IP addresses to allow. Enter the addresses in the CIDR format." %}}
{{% step_n2 3 "Click the [Add] button." %}}
To delete an IP address from the IP whitelist, click the [Delete] button on the right of the corresponding IP address.
{{% /div_method_area %}}

{{% div_method_area "Stop prediction API" %}}
Click the [Stop] button.
{{% /div_method_area %}}

{{% div_method_area "Delete prediction API" %}}
With the prediction API stopped, click the [Delete] button. When you delete an API, the number of API options in use decreases and you can create an API with another model.
{{% /div_method_area %}}

{{% div_method_area "Lock prediction API" %}}
Click the [Lock API] button. The API is locked and cannot be stopped. This prevents users from accidentally stopping the API.
{{% /div_method_area %}}

{{% div_method_area "Unlock prediction API" %}}
 With the prediction API locked, click the [Lock API] button. Only an account with the administrator role can perform this operation.
 The administrator role is configured in the User Portal.
{{% /div_method_area %}}


