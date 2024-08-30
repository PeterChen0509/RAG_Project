---
title: "Story: Improving accuracy of incoming call prediction"
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

#### Situations and Challenges: Prediction accuracy of incoming calls is poor

You are in charge of call center management. On the 20th of every month, you set the operator shifts for the next month. You predict the number of incoming calls for every day of the next month and decide how many operators to place based on that.
The number of incoming calls from the previous year can be used as a reference, so you calculated it by multiplying the number of incoming calls from one year ago by a coefficient, but it has been bad for the last six months, so the prediction is not good. The error rate is over 15%, which is considered a problem.

#### Using Predictive Analytics: Data-based incoming call prediction

- Prepare historical data of incoming calls (you will use sample datasets in the tutorial)
- Use Prediction One to predict number of incoming calls
- Set the operator's shift based on the predicted number of incoming calls.

#### Expected Effect: Reduced abandonment rate and reduced operator costs. Reduction of management man-hours.

Because the accuracy of the prediction of the number of incoming calls is improved, both the abandonment rate and operator labor cost can be reduced.
You'll be able to predict incoming calls in less time, and you'll be able to do less work (and reduce your mental burden).

Let's try to predict the number of incoming calls with Prediction One.
