---
title: "Story: Automating the Labeling of Review Sentences"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
tutorial_page:
  is_next_exists: true
---

#### Situations and Challenges: Labeling effort is time-consuming

You belong to the marketing department of a manufacturer that manufactures certain audio products. You analyze review statements on review sites to determine the reputation of your products. In particular, in order to analyze negative content, you collect low-rated review statements and label them by type. You share this type with your colleagues, but you also find it inefficient because it takes a few hours every week. This work itself is not fun.

#### Using predictive analytics: Replace labeling efforts with results from predictive analytics

- Prepare data summarizing the review statement and the results of classification so far (You will use sample datasets in the tutorial)
- Use Prediction One to predict types for review statements that have not yet been classified
- Reduce labeling effort by relying on Prediction One to label review statements

#### Expected Effect: Reduction of labeling effort. Stabilization of classification results

You can automate the labeling of review statements to reduce effort.
There were cases where the criteria for labeling differed from person to person, but automation is expected to make this more uniform.

**Now let's create a customer list based on the prediction with Prediction One.**
