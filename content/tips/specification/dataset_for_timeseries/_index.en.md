---
title: "Dataset for Time Series Prediction Mode"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4
draft: false
# metaタグのパラメータ
meta:
  description: "This page describes the format of the data that Prediction One prepares to create a time series model. Prediction One, a predictive analytics tool, makes it easy to make time series predictions."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  [
    "Time series prediction",
    "Time series regression",
    "Time interval",
    "Examples",
    "Prediction model creation (training) data",
    "How to make",
    "Training data",
    "Time information variable",
  ]
toc: true
---

Time Series Prediction Mode allows you to predict future values from past values over time.
However, to predict "N periods ahead," prediction model creation (training) data for "2N+1 periods or more" is required.
(For example, if there is 84 months worth of prediction model creation (training) data, a prediction can be made 41 months ahead.)

### Variables Required to Run Time Series Prediction Mode

The following variables are required to use the time series prediction mode.

<table>
    <thead>
        <tr>
            <td>Variable category</td>
            <td>Variable Data Types</td>
            <td>Required or not</td>
            <td style="width: 20em;">Description</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Variable to be predicted</td>
            <td>Numeric values</td>
            <td>Required</td>
            <td>Variable that contains the numeric value to be predicted.</td>
        </tr>
        <tr>
            <td>Time information variable of the variable to be predicted</td>
            <td>Datetime</td>
            <td>Required</td>
            <td>A variable that contains time information that indicates the date of the variable you want to predict. All dates and times must be unique and evenly spaced, and the entire data set must be sorted in ascending or descending order by this variable.</td>
        </tr>
        <tr>
            <td>Variables identifying the series</td>
            <td>String/numeric value</td>
            <td>Required if there is more than one series</td>
            <td>If there is more than one series (up to 200), the variable containing the values to separate the series.</td>
        </tr>
        <tr>
            <td>Other variables</td>
            <td>String/Text/Numeric value/Datetime</td>
            <td>Optional</td>
            <td>Variables that may be relevant to the variable you want to predict. However, do not use variables that cannot be prepared for actual prediction.</td>
        </tr>
    </tbody>
</table>

{{% a_id "time-interval" %}}

### Supported Time Intervals

The date and time included in the time information variable for the variable you want to predict must be in years, months, days, hours, and minutes, **and must be mostly at regular intervals**. For each time unit, the supported time interval is:

| Time unit | Supported time interval |
| :------: | :------------------- |
|    Years    | 1–10 year intervals          |
|    Months    | 1–11 month intervals          |
|   Days    | 1–28 day intervals          |
|    Hours    | 1–23 hour intervals          |
|   Minutes    | 1–59 minute intervals          |

You can improve the accuracy of time series prediction by adding variables that are likely to be related to the variables you want to predict as "Other Variables".
<!-- ただし、実際の予測時に用意できない項目は使用することができません。たとえば、10 日先の販売数を予測するには、販売日の 10 日前の時点で、10 日先の「イベント(予定)」と「広告費(予定)」の項目を用意する必要があります。 -->

{{< notice tip >}}
Although time information variables must be spaced at regular intervals in order to use the time series prediction feature, data can be arranged into regular intervals by using the **"Aggregate by date/time" feature of the Data Preparation feature**.
For example, to predict the weekly average of a variable, specify "week" as the aggregation unit in "Aggregate by date/time" and then specify "average" as the aggregation method.
{{</ notice >}}

### Sample Data Set for Time Series Prediction

#### The series does not exist and there are other variables.

In this example, the variable you want to predict = "Sales", the time information variable of the variable you want to predict = "Date", and the other variables = "Sale (schedule)", "Advertising expenses (schedule)".

**Prediction model creation (training) data**

<div class="csv_table">

|    Date    |  Sales  | Sale (schedule) | Advertising expenses (schedule) |
| :--------: | :------: | :--------------: | :----------: |
| 2018/10/08 | 2,000,000 yen |       No      |   200,000 yen    |
| 2018/10/15 | 1,490,000 yen |       No      |   190,000 yen    |
| 2018/10/22 | 1,120,000 yen |       No      |   200,000 yen    |
| 2018/10/29 | 1,000,000 yen |       No      |   190,000 yen    |
| 2018/11/05 | 1,140,000 yen |       Yes      |   200,000 yen    |
| 2018/11/12 | 1,530,000 yen |      Yes       |   190,000 yen   |
| 2018/11/19 | 2,040,000 yen |       No      |   190,000 yen    |
| 2018/11/26 | 2,540,000 yen |       No      |   200,000 yen    |
| 2018/12/03 | 2,890,000 yen |       No      |   190,000 yen    |
| 2018/12/10 | 2,990,000 yen |       No      |   200,000 yen    |
| 2018/12/17 | 2,820,000 yen |       No      |   190,000 yen    |
| 2018/12/24 | 2,420,000 yen |       No      |   190,000 yen    |
|     …      |   　…    |       　…        |     　…      |
| 2019/07/29 | 2,820,000 yen |       No      |   190,000 yen    |
| 2019/08/05 | 2,420,000 yen |       No      |   190,000 yen    |

</div>

This dataset has data for every 7 days in the "Date" variable, which is the variable information of the variable to be predicted. Because the time information is sorted in ascending order and the time intervals are evenly spaced, this dataset can be used in Time Series Prediction Mode.

Suppose we want to predict sales for the period `2019/08/12` to `2019/10/07` using a prediction model created with this prediction model creation (training) data.

If you selected "set automatically" for the "Data to be entered during prediction" setting during training, please check the "Auto-generation of prediction data" checkbox to perform the prediction. When specifying prediction data, prepare the following data as prediction data. The "Sales" column, which is the variable to be predicted, can be predicted even if it is not included in the prediction data.

**Prediction data (set automatically)**

<div class="csv_table">

|    Date    | 　Sales |
| :--------: | :------: |
| 2019/08/12 |          |
| 2019/08/19 |          |
| 2019/08/26 |          |
| 2019/09/02 |          |
| 2019/09/09 |          |
| 2019/09/16 |          |
| 2019/09/23 |          |
| 2019/09/30 |          |
| 2019/10/07 |          |

</div>

If you selected "set individually" in "Data to be entered during prediction" setting during training, data for the prediction period for the selected variable is required. Please prepare the following data for prediction (example shows the selection of Sale (schedule) and Advertising expenses (schedule)). The "Sales" column, which is the variable to be predicted, can be predicted even if it is not included in the prediction data.

**Prediction data (set individually)**

<div class="csv_table">

|    Date    |  Sales  | Sale (schedule) | Advertising expenses (schedule) |
| :--------: | :------: | :--------------: | :----------: |
| 2019/08/12 |          |       No      |   200,000 yen    |
| 2019/08/19 |          |       No      |   190,000 yen    |
| 2019/08/26 |          |       No      |   200,000 yen    |
| 2019/09/02 |          |       Yes      |   190,000 yen    |
| 2019/09/09 |          |       No      |   200,000 yen    |
| 2019/09/16 |          |      Yes      |   190,000 yen    |
| 2019/09/23 |          |       No       |   190,000 yen    |
| 2019/09/30 |          |       No      |   200,000 yen    |
| 2019/10/07 |          |       Yes      |   190,000 yen    |

</div>

If the "Date" variable in the prediction model creation (training) data has data every 7 days, the "Date" variable in the prediction data set should also be every 7 days.

{{% a_id "timeseries-no-feature" %}}

#### If the series does not exist and there are no other variables.

In this example, the variable you want to predict = "number of shipments", the time information variable of the variable you want to predict = "Month", and there are no other variables.

**Prediction model creation (training) data**

<div class="csv_table">

|   Month   |  Shipments  |
| :-----: | :------: |
| 2016-10 | 10000 |
| 2017-01 | 11400 |
| 2017-04 | 15300 |
| 2017-07 | 20400 |
| 2017-10 | 25400 |
| 2018-01 | 28900 |
| 2018-04 | 29900 |
| 2018-07 | 28200 |
| 2018-10 | 24200 |
| 2019-01 | 19100 |
| 2019-04 | 14100 |
| 2019-07 | 10800 |
| 2019-10 | 10000 |

</div>

In this dataset, there is data for every 3 months in the "month" variable, which is the time information variable of the item you want to predict.
Because the time information is sorted in ascending order and the time intervals are evenly spaced, this dataset can be used in Time Series Prediction Mode.

If you want to predict number of shipments for the period `2020-01` to `2020-07` using a prediction model created using this prediction model creation (training) data, check "Auto-generation of prediction data" and make a prediction.
When specifying prediction data, prepare the following data as prediction data. The "number of shipments" column, which is the variable to be predicted, can be predicted even if it is not included in the prediction data.

**Prediction Data**

<div class="csv_table">

|   Month   | Number of shipments |
| :-----: | :----: |
| 2020-01 |        |
| 2020-04 |        |
| 2020-07 |        |

</div>

#### There is more than one series and there are other variables.

In this example, the variable you want to predict = "Number of sales", the time information variable of the variable you want to predict = "Date", series variables = "Sales region", and others = "Event (schedule)", "Advertising expenses (schedule)".

**Prediction model creation (training) data**

<div class="csv_table">

|   Date    | Sales region | Number of sales |  Event (schedule) | Advertising expenses (schedule) |
| :-------: | :------: | :----: | :--------------: | :----------: |
| 2019/4/1  |  Region A  |  814   |                  |     100      |
| 2019/4/1  |  Region B  |  1940  |                  |     100      |
| 2019/4/2  |  Region A  |  834   |                  |      50      |
| 2019/4/2  |  Region B  |  1783  |                  |      50      |
| 2019/4/3  |  Region A  |  802   |   Regular event   |      20      |
| 2019/4/3  |  Region B  |  1744  |   Regular event   |      20      |
| 2019/4/4  |  Region A  |  806   |                  |      20      |
| 2019/4/4  |  Region B  |  1909  |                  |      20      |
| 2019/4/5  |  Region A  |  939   | Discount campaign |      20      |
| 2019/4/5  |  Region B  |  1882  |                  |      20      |
| 2019/4/6  |  Region A  |  1333  |   Weekend event   |     120      |
| 2019/4/6  |  Region B  |  2288  |                  |     120      |
| 2019/4/7  |  Region A  |  1341  |                  |     120      |
| 2019/4/7  |  Region B  |  2207  |   Weekend event   |     120      |
|     …     |    …     |   …    |        …         |      …       |
| 2019/4/29 |  Region A  |  1333  |   Weekend event   |     120      |
| 2019/4/30 |  Region B  |  2288  |                  |     120      |
| 2019/4/29 |  Region A  |  1341  |                  |     120      |
| 2019/4/30 |  Region B  |  2207  |   Weekend event   |     120      |

</div>

This dataset contains two duplicate dates and times (example: 2019/4/1) in the "Date" variable, which is the time information variable for the variable you want to predict.
Such a data set is considered to contain multiple series (i.e., series named Region A and Region B), and so a variable to separate the series is required. When the series are separated by the values "Region A" and "Region B" in the "Sales region" field, this dataset can be used in time-series prediction mode because all dates and times within the series are arranged without overlap and at one-day intervals, and the time information is sorted in ascending order.

Suppose we want to predict number of sales for the period `2019/5/01` to `2019/5/04` using a prediction model created with this prediction model creation (training) data.

If you selected "set automatically" for the "Data to be entered during prediction" setting during training, please check the "Auto-generation of prediction data" checkbox to perform the prediction. When specifying prediction data, prepare the following data as prediction data. The "number of sales" column, which is the variable to be predicted, can be predicted even if it is not included in the prediction data.

**Prediction data (set automatically)**

<div class="csv_table">

|   Date   | Sales region | Number of sales |
| :------: | :------: | :----: |
| 2019/5/1 |  Region A  |        |
| 2019/5/1 |  Region B  |        |
| 2019/5/2 |  Region A  |        |
| 2019/5/2 |  Region B  |        |
| 2019/5/3 |  Region A  |        |
| 2019/5/3 |  Region B  |        |
| 2019/5/4 |  Region A  |        |
| 2019/5/4 |  Region B  |        |

If you selected "set individually" in "Data to be entered during prediction" setting during training, data for the prediction period for the selected variable is required. Please prepare the following data for prediction (example shows the selection of Event (schedule) and Advertising expenses (schedule)). The "number of sales" column, which is the variable to be predicted, can be predicted even if it is not included in the prediction data.

**Prediction data (set individually)**

<div class="csv_table">

|   Date    | Sales region | Number of sales | Event (schedule) | Advertising expenses (schedule) |
| :------: | :------: | :----: | :------------: | :----------: |
| 2019/5/1 |  Region A  |        |                |     100      |
| 2019/5/1 |  Region B  |        |                |     100      |
| 2019/5/2 |  Region A  |        |                |      50      |
| 2019/5/2 |  Region B  |        |                |      50      |
| 2019/5/3 |  Region A  |        |  Regular event  |      20      |
| 2019/5/3 |  Region B  |        |  Regular event  |      20      |
| 2019/5/4 |  Region A  |        |                |      20      |
| 2019/5/4 |  Region B  |        |                |      20      |

</div>

#### There is more than one series and no other variables.

In this example, the variable you want to predict = "Sales", the time information variable of the variable you want to predict = "Year", series variables = "Store name", and there are no other variables.

**Prediction model creation (training) data**

<div class="csv_table">

| Year | Store name |  Sales   |
| :--: | :----: | :-------: |
| 1990 | Store A | 20,000,000 yen |
| 1990 | Store B | 25,000,000 yen |
| 1990 | Store C | 25,000,000 yen |
| 1991 | Store A | 14,900,000 yen |
| 1991 | Store B | 24,390,000 yen |
| 1991 | Store C | 24,300,000 yen |
| 1992 | Store A | 11,200,000 yen |
| 1992 | Store B | 22,400,000 yen |
| 1992 | Store C | 22,400,000 yen |
| 1993 | Store A | 10,000,000 yen |
| 1993 | Store B | 19,800,000 yen |
| 1993 | Store C | 19,800,000 yen |
|  …   |   …    |     …     |
| 2002 | Store A | 19,100,000 yen |
| 2002 | Store B | 24,900,000 yen |
| 2002 | Store C | 24,900,000 yen |
| 2003 | Store A | 14,100,000 yen |
| 2003 | Store B | 24,000,000 yen |
| 2003 | Store C | 24,000,000 yen |
| 2004 | Store A | 10,800,000 yen |
| 2004 | Store B | 22,000,000 yen |
| 2004 | Store C | 22,000,000 yen |

</div>

This dataset contains year-by-year data for the "Year" variable, which is the time information variable of the variable you want to predict.
Because the time information is sorted in ascending order and the time intervals are evenly spaced, this dataset can be used in Time Series Prediction Mode.

If you are using a prediction model created using this prediction model creation (training) data to predict sales for the period `2005` to `2007`, please check "Auto-generation of prediction data", then perform the prediction.
When specifying prediction data, prepare the following data as prediction data. The "Sales" column, which is the variable to be predicted, can be predicted even if it is not included in the prediction data.

**Prediction Data**

<div class="csv_table">

| Year | Store name | Sales  |
| :--: | :----: | :----: |
| 2005 | Store A |        |
| 2005 | Store B |        |
| 2005 | Store C |        |
| 2006 | Store A |        |
| 2006 | Store B |        |
| 2006 | Store C |        |
| 2007 | Store A |        |
| 2007 | Store B |        |
| 2007 | Store C |        |

</div>
