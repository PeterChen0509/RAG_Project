---
title: "予測誤差の分布"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8500
draft: false
# metaタグのパラメータ
meta:
  description: "予測誤差の分布とは、予測モデルを評価用データを用いて評価したとき、評価用データに含まれるデータのうち何%がどれくらい予測を誤ったか（＝誤差）をグラフで表現したものです。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
---

**予測誤差の分布**とは、予測モデルを評価用データを用いて評価したとき、評価用データに含まれるデータのうち何%がどれくらい予測を誤ったか（＝誤差）をグラフで表現したものです。

予測誤差の分布から、予測誤差全体の様子がわかります。
予測誤差が 0 以上 5 未満に収まるのは全体の何％か、5 以上 10 未満に収まるのは全体の何％か、…といった予測誤差の分布が棒グラフとして表示されます。
予測がどういった誤差になりやすいのかを見ることができます。

![](../img/t_slide7.png)

上の図の場合、評価用データに含まれるデータのおよそ 11.4%が 0~100 に収まる範囲の誤差で予測を行うことができたことを表しています。
また、誤差が 700~800 であるデータは一件も存在しなかったことを示しています。

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/result/eval_reg/" "予測精度の概要（数値予測）" %}}

{{% /div_relitem %}}