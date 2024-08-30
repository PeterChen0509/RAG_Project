---
title: "予測モデル作成(学習)用データの準備"
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
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
tutorial_page:
  is_next_exists: true
---

予測分析では、下記のように、予測モデル作成(学習)用データとして各商品の販売チャネル別の売上実績データを、関連データとして商品属性データと販売チャネル属性データを用いて、売上金額を予測する予測モデルを作成します。<br/>
予測モデルは、予測モデル作成(学習)用データと関連データからどのような販売チャネルでどんな商品を売ると、売上金額がどれくらいになるかを学習します。
本チュートリアルでは、すでに準備してあるサンプルデータを利用します。

{{% tutorial_file_location "/ja-JP/doc/sample_dataset/use_case/販売管理_商品売上予測による入荷計画の改善" %}}

![](../img/t_slide4.png)

![](../img/t_slide5.png)

以降のページでは、Prediction One の操作について説明します。