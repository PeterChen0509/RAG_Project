---
title: "How to Read the Predictive Contribution"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 3
draft: false
# metaタグのパラメータ
meta:
  description: "Prediction One is a predictive analytics tool that allows you to easily see what has an effect on your prediction results. This section describes the expected contribution that can be seen in Prediction One."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Degree of contribution", "Predictive contribution", "Meaning", "How to read", "Importance", "importance"]
---

{{% div_slide "Introduction" normal first-page %}}

This document describes the concept of predictive contribution in Prediction One.<br />
You can use the predictive contribution to determine which data variables and which values affect the prediction results to what extent.<br />
This is very important when you actually use predictive analytics.<br />

- You can use the prediction results with confidence because you can understand and confirm how to predict.
- You can get explain the results of predictive analytics to stakeholders in a way that is easier to understand.
- You can see which parts of the data are important and how much, which leads to better datasets. This makes it easier to notice errors.
- Contribution of previously unimagined variables leads to new discoveries.
  {{% /div_slide %}}

{{% div_slide "Training and Predicting for Predictive Analytics" normal %}}

Predictive analytics involves two steps: training and predicting. The following is an example of predicting a customer's purchase from actual purchase data.

![](img_en/t_slide2.png)
{{% /div_slide %}}

{{% div_slide "Outline of calculation method of predictive contribution" normal %}}

The predictive contribution is calculated against the prediction model. First, calculate the predicted result (for example, probability of purchase) for some data (for example, customer A).<br />

![](img_en/t_slide3.png)

Next, with some variables (for example, department information) removed from the input data, the predicted results are calculated again.<br />

![](img_en/t_slide4.png)

The predicted contribution of the removed variable is the difference in the prediction probability when the variable is included or removed. In the above example, the predictive contribution of information for Customer A's department is 0.85 - 0.70 = 0.15. This example assumes that the department information variable has increased the prediction probability by 0.15. <br />
The larger the difference in the prediction probability, the more likely the variable is to contribute to the prediction. For example, if there is a variable that does not affect the prediction result (no contribution), the difference in the prediction probability should be zero, because it is the same whether it exists or not. You can also see whether it contributes to increasing or decreasing the probability of purchase by looking at whether it is increasing or decreasing the prediction probability.
{{% /div_slide %}}

{{% div_slide "Detailed screen of predictive contribution (binary classification)" normal %}}

The detail screen of prediction contribution is described using a dataset for binary classification as an example.<br />
A dataset used to predict the purchase of premium services from customer data.<br />

{{% desktop_only %}}
<small>This sample dataset is in the following folder: `C:/Program Files/Sony/Prediction One/ja-JP/doc/sample_dataset/use_case/マーケティング_顧客行動予測に基づいたターゲティング`</small>
{{% /desktop_only %}}
{{% cloud_only %}}
<small>This sample dataset is available from the Data -> Samples tab data list.</small>
{{% /cloud_only %}}

![](img_en/t_slide5.png)

<hr/>

![](img_en/t_slide6.png)

The left side of the screen lists the predictive contribution of each variable. The greater the contribution, the longer the bar. The bar length is relative to the variable with the highest contribution. <br />
The blue bar represents the amount of contribution to increasing the probability of purchase (the probability of "purchased"). The red bar represents the degree of contribution to decreasing the purchase probability.<br />
You can toggle which bar is displayed in the Sort Order pull-down. When you click a variable name or bar, the display on the left switches to that of the variable you clicked.

<hr/>

![](img_en/t_slide7.png)

The right side of the screen displays details about the variable selected on the left. Suppose you click the "Customer Rank" variable on the screen. "Customer Rank" can be "Platinum," "Gold," "Silver," or "Bronze." From this screen, you can see that "Platinum" customers contribute to the prediction by increasing the probability of "purchased".

Contribution strength is displayed as the length of the Contribution bar. Percentage of Values is the percentage of customers whose selected variable in the dataset is the value of the variable's contents.
For this dataset, 32% of all customers have a Customer Rank of "Platinum". Platinum is important information that contributes greatly and has many customers.

<hr />

![](img_en/t_slide8.png)

You can see that customers with a Customer Rank of Bronze, Silver, or Gold contribute to the prediction results in a way that increases the prediction probability of No Purchase (and decreases the prediction probability of Purchased). Contributions are listed in descending order, and the magnitude of the contribution is indicated by the length of the Contribution bar.

These results may seem obvious if there are practitioners familiar with the service. Confirming that it matches the perceptions and intuitions of practitioners can increase confidence in predictions.

<hr />

![](img_en/t_slide9.png)

Now, let's say you clicked on the Past Purchases variable. Past Purchases is a numeric variable. For a numeric variable, a range of values is automatically set, and each range shows how it contributes to the purchase probability.
By looking at the "range of numbers", you can see at a glance which range of "past purchases" will increase or decrease the prediction probability. Blue contributes to purchase and red contributes to no purchase.

{{% /div_slide %}}

{{% div_slide "Detailed screen of predictive contribution (multiclass classification)" normal %}}

Next, the predictive contribution screen of multiclass classification will be explained. Let's take an example of the analysis results of the dataset below. A dataset to predict which complaint types to classify for review statements.<br/>
{{% desktop_only %}}
<small>This sample dataset is in the following folder: `C:/Program Files/Sony/Prediction One/ja-JP/doc/sample_dataset/use_case/CRM_顧客の声のラベリング自動化`</small>
{{% /desktop_only %}}
{{% cloud_only %}}
<small>This sample dataset is available from the Data -> Samples tab data list.</small>
{{% /cloud_only %}}

![](img_en/t_slide10.png)

<hr/>

![](img_en/t_slide11.png)

The left side of the screen lists the predictive contribution of each variable.
Multiclass classification calculates the contribution for each class (complaint type), but initially displays the total. You can toggle which classes' contributions are displayed in the Filter pull-down. You can also use the Filter button on the right to toggle in the same way.
As with binary classification, click the variable name or bar to switch the display on the right.

<hr/>

![](img_en/t_slide12.png)

Let's look at the right side. Multiclass classification calculates the contribution for each class (complaint type), so each class displays the contents of the variables that contribute to that class. There are five classes in this dataset, so there are five.
The Post Content variable is a text type. The variable content displays the words contained in the text. Inclusion of "different", "look", and "feel" increases the probability of the "(a) look" class.
{{% /div_slide %}}

{{% div_slide "Detailed screen of predictive contribution (regression, time series prediction)" normal %}}

The screen of the predictive contribution of regression is described below. Let's take an example of the analysis results of the dataset below. You predict the number of incoming calls in the future from the number of incoming calls in the past at the call center.<br/>
{{% desktop_only %}}
<small>This sample dataset is in the following folder: `C:/Program Files/Sony/Prediction One/ja-JP/doc/sample_dataset/use_case/コールセンター_入電予測によるオペレータ人数決定`</small>
{{% /desktop_only %}}
{{% cloud_only %}}
<small>Click "Select from Uploaded Data" and select the sample data from the data list on the "Samples" tab.</small>
{{% /cloud_only %}}

![](img_en/t_slide13.png)

<hr/>

![](img_en/t_slide14.png)

The left side of the screen lists the predictive contribution of each variable. The greater the contribution, the longer the bar. The bar length is relative to the variable with the highest contribution.
The blue bar indicates the magnitude of the contribution to the increase in the predicted value (predicted number of incoming calls). The red bar represents the degree of contribution to decreasing the predicted value. You can toggle which bar is displayed in the Sort Order pull-down.
When you click a variable name or bar, the display on the left switches to that of the variable you clicked.

<hr/>

![](img_en/t_slide15.png)

Let's look at the right side. Let's say you clicked on the "Day of Week" variable.
From this screen, you can see that "Monday", "Wednesday", and "Friday" increase the predicted number of incoming calls. "Saturday" and "Sunday" will reduce the predicted number of incoming calls.
Percentage of Values is the same as binary classification or multiclass classification. For example, you can see that 15% of the data in this dataset has the day of the week as "Monday".

<hr />

![](img_en/t_slide16.png)

This section describes the predictive contribution of date-type variables. Suppose you click "Date," a date-type variable.
In this dataset, the "Date" is something like "2018/2/1", but Prediction One shows the most predictive year, month, day, etc. In this dataset, the "month" is selected. For example, you can see that "January" contributes to reducing the predicted number of incoming calls.
{{% /div_slide %}}

{{% div_slide "About the Add Prediction Reason Option for Predicting" normal %}}

This section describes the Add Prediction Reason option and how to read its output when predicting.
![](img_en/t_slide17.png)

You can add prediction reasons for each row of prediction data by checking the Add Prediction Reason option when predicting.
<hr />

![](img_en/t_slide18.png)

When the option "Add Prediction Reason" is ON, columns "Increase ~ 1", "Increase ~ 2", "Increase ~ 3", "Decrease ~ 1", "Decrease ~ 2", and "Decrease ~ 3" are added to the prediction result CSV file. This means Top 1, Top 2, and Top 3, which are factors that increase or decrease the predicted probability or value.
Each prediction reason column is output in the format`[項目名]:[項目内容]:[寄与度]`.
In this example, a customer with a "Customer ID" of "ID01006" has a high probability of purchasing of 71.95%, but you can see that the Top 1 factor that increases the probability of a purchase is because the "Customer Rank" is "Platinum". You can also see that having a "Customer Rank" of "Platinum" increased the probability of a purchase by 21.61%.
(`寄与度` can be interpreted as an increase/decrease in prediction probability for binary classification and an increase/decrease in predicted value for regression. However, multiclass classification cannot be interpreted as prediction probability.)

<hr />
{{% /div_slide %}}

{{% div_slide "Summary" summary %}}

In this document, we have explained the predictive contribution of Prediction One.<br/>
As I explained at the beginning of this document, predictive contribution is very useful when you actually use predictive analytics in your business.<br/>
There are many users who place more importance on predictive contribution than on prediction accuracy.<br/>
This software has been developed with an emphasis on calculation and display of predictive contribution. Please get to know the perspective of the contribution screen in this document, and use it for predictive analytics.<br/>
{{% /div_slide %}}
