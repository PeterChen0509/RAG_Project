---
title: "How to Utilize Prediction Results"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 9
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["How to use", "Utilize", "Operation", "Sorting", "Probability"]
---

{{% div_slide "Introduction" normal first-page %}}
Using the prediction model created by Prediction One, you can predict the future state of the input data.

This document provides an example of how prediction models can help you make decisions and improve your business.

![](img_en/t_slide2.png)
{{% /div_slide %}}

{{% div_slide "Make decisions based on probability of occurrence" normal %}}
Prediction models that perform classification such as binary classification and multiclass classification not only perform classification but also output the probability when classified. It is possible to predict whether an event will occur, and to take measures against those with high or low probability of occurrence.

![](img_en/t_slide4.png)

#### Example 1:  {{% a_in "../../../tutorial/predicting_equipment_failures/" "Preventing failures by predicting equipment failures" %}}

To prevent a failure by preparing a prediction model using data of equipment which has failed in the past and equipment which operates normally, and checking the equipment with high possibility of failure in the future based on the prediction model.

#### Example 2:  {{% a_in "../../../tutorial/crm_predict_unsubscribe/" "Reduction of withdrawal by withdrawal prediction" %}}

A prediction model for classifying whether or not a customer withdraws in the future is prepared, and a decision is made by using the withdrawal probability of each customer outputted from the prediction model.{{% /div_slide %}}

{{% div_slide "Predict what the value will be based on past cases" normal %}}
A large number of past cases are prepared as a dataset, and a prediction model is created using the dataset. The prediction results are used for decision making. You can make predictions with a prediction model and make decisions based on the predicted results before you know what the actual numbers will be.

![](img_en/t_slide5.png)

#### Example 1:  {{% a_in "../../../tutorial/real_estate_price_forecast/" "Prediction of the closing price of real estate" %}}

Based on the data of past real estate contracts, we predict the price at which uncontracted real estate will be closed.

#### Example 2:  {{% a_in "../../../tutorial/predicting_characteristics/" "Characteristic value prediction" %}}

Based on the data of a large number of past experiment results, we predict in advance what kind of result will be obtained from a specific experiment setting, and decide what kind of experiment will be performed next using the result.
{{% /div_slide %}}

{{% div_slide "Predict how things will change in the future" normal %}}
Intuitively predictable numbers can be more accurately predicted by creating prediction models for regression.

![](img_en/t_slide6.png)

#### Example 1:  {{% a_in "../../../tutorial/forecast_demand/" "Improving accuracy of production plans by shipments prediction" %}}

Based on past shipments of multiple products, it predicts how many products it expects to ship in the next three months.

#### Example 2:  {{% a_in "../../../tutorial/determining_the_number_of_operators/" "Determining the number of operators by predicting incoming calls" %}}

To determine the number of operators in the call center, predict how many calls are coming in each day.
{{% /div_slide %}}

{{% div_slide "Use results of contribution analysis for decision making" normal %}}
Depending on how the data is collected, it may be difficult to collect prediction data in advance to make predictions.
For example, you may want to predict whether a contract will close for each customer, but it may take some time for customer records to become organized.

In such cases, a prediction model can be created for past cases, and the results of analysis of the contribution can be used for decision making.

![](img_en/t_slide7.png)

#### Example 1:  {{% a_in "../../../tutorial/find_promising_customers/" "Targeting promising customers by closing prediction" %}}

By creating a prediction model that predicts what customers will close, you can look at what factors are involved in the close.

#### Example 2:  {{% a_in "../../../tutorial/forecast_behavior/" "Employee behavior prediction" %}}

Promote work-style reforms by encouraging employees to take time off based on predictions of which employees will be able to take time off.
{{% /div_slide %}}

{{% div_slide "Automate mass sorting" normal %}}
It is possible to improve the business by automating the process of sorting and classifying a large amount of data using the predicted result of the prediction model.

![](img_en/t_slide3.png)

Create a prediction model using the data that people have sorted as prediction model creation (training) data, and prepare the data that has not been sorted as prediction data.
By entering prediction data into a prediction model, you automatically sort data that has not yet been sorted.

#### Example 1:  {{% a_in "../../../tutorial/crm_automate_voice_of_the_customer_labeling/" ""Automated labeling of customer feedback""%}}

Use prediction models to automatically label and categorize large numbers of customer review statements that arrive at the call center.

#### Example 2:  {{% a_in "../../../tutorial/classification_of_fault_information/" "automatic classification of failure information" %}}

With the background that we want to automatically sort out which parts of the machine are out of order in a stream of text messages about equipment failures, we automate sorting using prediction models.
{{% /div_slide %}}

{{% div_slide "Summary" summary %}}
In this document, we explained how to use the predicted results obtained from the prediction model to improve decision making and business operations. The following is an example of how you can use the results of the prediction model created by Prediction One.

- Create a prediction model to classify and make decisions based on the predicted results and probabilities
- Predict values that you would be happy to predict in advance using prediction models
- Predict how things will change in the future
- Use results of contribution analysis for decision making
- Automate the mass sorting that people were doing.

Beyond these examples, the use of predictive analytics varies from user to user.
Consider how to use the contribution and predicted results from Prediction One in your own case.
{{% /div_slide %}}
