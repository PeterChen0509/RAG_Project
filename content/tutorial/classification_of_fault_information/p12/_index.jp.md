---
title: "故障タイプの分類"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 12
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

{{% div_slide "予測結果を利用したタイプ割り当ての自動化" normal first-page %}}

各故障情報に対する予測確率から、もっとも確率の高い故障タイプを割り当てることで、故障タイプの割り当てを自動的に行うことができます。

![](../img/t_slide20.png)

実際は、予測精度は 100%ではないので間違えることもあります。もっとも高い予測確率の値が大きくない場合は、予測の確信度が低いことになりますので、こういったケースは人間がチェックする方が良い場合もあります。
{{% /div_slide %}}
