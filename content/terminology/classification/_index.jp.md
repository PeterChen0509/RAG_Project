---
title: "分類"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 6300
draft: false
# metaタグのパラメータ
meta:
  description: "分類とは、たとえばあるゴミを可燃物か不燃物に分けるように、与えられたデータがどのグループに所属するかを判定する問題の総称です。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["分類", "classify", "分ける", "仕分け", "選別"]
---

**分類**とは、たとえばあるゴミを可燃物か不燃物に分けるように、与えられたデータがどのグループに所属するかを判定する問題の総称です。

### 分類で解ける問題の具体例

- コンバージョン・退会などの顧客行動：顧客行動の記録を複数のグループに分類することで、どの様な要素が顧客行動を決めているか分析をしたり、各顧客がどのような行動をするか予測できます。
- 苦情・レポートなどの分類：大量の文章を自動的に分類することで、人手で行っていた工程をより簡単に行うことができます。

### Prediction One で分類を行う

{{% a_in "../../tips/how_to_create_dataset/" "「データセットの作り方」" %}}を参照して、分類問題として扱えるようなデータセットを作成してください。
Prediction One では 2 つのグループのどちらに所属するかを当てる{{% a_in "../binary_classification/" "二値分類" %}}と、3 つ以上のグループのどれに所属するかを当てる{{% a_in "../multiclass_classification/" "多値分類" %}}の 2 タイプの分類問題を扱うことができます。

{{% div_relitem contents-bottom %}}

- {{% a_in "../binary_classification/" "二値分類" %}}
- {{% a_in "../multiclass_classification/" "多値分類" %}}
- {{% a_in "../../tips/specification/dataset_format/" "データセットとは" %}}

{{% /div_relitem %}}
