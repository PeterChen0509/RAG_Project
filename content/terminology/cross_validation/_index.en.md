---
title: "Cross-validation"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2500
draft: false
# metaタグのパラメータ
meta:
  description: "Cross-validation is a method of verifying the performance of a prediction model more accurately by dividing a given piece of data for learning and verification, and repeating the work of learning and evaluating the prediction model while changing the division point."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Cross-validation", "Cross-validation", "Always perform cross-validation"]
---

**Cross-validation** is a method of verifying the performance of a prediction model more accurately by dividing a given piece of data for learning and verification, and repeating the work of learning and evaluating the prediction model while changing the division point.

Prediction One performs cross-validation internally if the option of cross-validation is specified.
It also automatically performs cross-validation when the amount of data is small.

Cross-validation increases the number of times the predictive model is learned and evaluated, which can increase the time it takes to obtain evaluation results.

### Perform cross-validation with Prediction One

Please check Advanced Settings on the prediction model creation screen, and
check [Cross-validation].

![](../img_en/t_slide28.png)
