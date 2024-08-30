---
title: "過去の予測したい項目の値"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["ラグ特徴量", "時間差", "過去の値", ""]
---

過去の予測したい項目の値とは、ある時点よりも未来の値を予測するために、過去の値を参照しつつ作成した項目のことを指しています。

たとえば、{{% a_in "../../tutorial/forecast_demand/" "製品の出荷数予測のチュートリアル" %}}では、これから 12 カ月先までの出荷数を予測しようとしています。
この時、ある時点から 3 か月先や 4 カ月先の予測を行うために、12 カ月前や 24 カ月前の出荷数の情報などを参照しながら予測を行います。
どの時点での値を参照するかは Prediction One の時系列モデルが自動的に決定します。
このように、過去の情報を元にして作成した項目を Predition One では過去の予測したい項目の値として表示しています。

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/new_features/timeseries/" "時系列予測" %}}
  {{% /div_relitem %}}
