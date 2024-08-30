---
title: "Preparing the latest data for creating a prediction model (training) and evaluation data"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: [""]
tutorial_page:
  is_next_exists: true
---

We now have more training data than we did during the last training process. It also appears that the current data includes some new failure information.
Let's go ahead and update the model with the latest data.

In this tutorial, we'll use the model we created for the {{% a_in "../../classification_of_fault_information/" "classification of failure information" %}}.
Before we get started, though, we suggest creating a model in the above tutorial if you haven't already.

{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/InformationManagement_Automatic classification of the latest failure information" %}}

The data we're working with now has new additions: failure information from 2018 and 2019. Training the model with both the data for creating a prediction model (training) from last time and the latest data
will improve the accuracy of the model.

We'll also extract portions of the training data for the period since January 2019 to use as evaluation data.
Using that evaluation data, we'll compare the accuracy levels of the previously trained model with the current one.

The sample data file name and details of the files we'll be using are as follows.

![](../img_en/t_slide3.png)

![](../img_en/t_slide5.png)

The following pages describe how Prediction One operates.
