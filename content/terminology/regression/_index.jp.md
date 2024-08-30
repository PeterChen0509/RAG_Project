---
title: "数値予測（回帰）"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 3300
draft: false
# metaタグのパラメータ
meta:
  description: "数値予測とは、たとえば天気や湿度から気温を予測するように、いくつかの項目から数値を予測することです。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["回帰", "リグレッション"]
---

**数値予測**とは、たとえば天気や湿度から気温を予測するように、いくつかの項目から数値を予測することです。

### Prediction One で数値予測を行う

{{% a_in "../../tips/specification/dataset_format/" "TIPS「データセットとは」" %}}を参照して、数値予測問題として扱えるようなデータセットを作成してください。また、特に時間に沿った数値の変化を予測したい場合は「{{% a_in "../timeseries_mode/" "時系列予測モード" %}}」を使用してください。
