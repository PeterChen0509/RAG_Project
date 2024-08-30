---
title: "Automatic classification of the latest failure information"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 19
draft: false
# metaタグのパラメータ
meta:
  description: "This is a tutorial on Prediction One, a piece of software that can be easily operated by non-experts, which calculates predictions from data. This section explains how to use Prediction One using an example of automatic classification of failure information."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords:
  ["failure", "Equipment", "Sensor", "Binary", "classification", "tutorials", "How to use", "Model update", "Latest data"]
tutorial_page:
  is_next_exists: true
---

### Introduction: Automatic classification of failure information trained with the latest data

In various businesses, information may be accumulated, classified, and labeled to give a bird's-eye view of the situation.
In the {{% a_in "../classification_of_fault_information/" "classification of failure information" %}} tutorial, we looked at an example of how to deal with this process.

Here, let's assume that some time has passed since the last tutorial and new, up-to-date data is available for use.
Over time, the types of problems and failures that occur are prone to change;
models thus tend to become less and less accurate as they age.

To avoid problems stemming from these tendencies, you need to create a model with newly obtained data and do an evaluation on the latest data,
which allows you to see how much the new information can improve overall accuracy. In this tutorial, we'll assume that you've obtained new data and show you how to
take care of those key steps in Prediction One.

By continually creating new models that reflect trends in the latest data, you can enhance the efficiency of automation and operations.

<br>

![](img_en/t_slide2.png)

