---
title: "予測理由・寄与度"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8500
draft: false
# metaタグのパラメータ
meta:
  description: "寄与度とは、データの各項目・各値がどの程度予測結果に影響を与えているかを数値で表現したものです。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["重要度", "importance"]
---

**寄与度**とは、データの各項目・各値がどの程度予測結果に影響を与えているかを数値で表現したものです。
たとえば、不動産の成約価格を予測する予測モデルを作成した結果、以下の図のような結果が得られたとします。

![](../img/t_slide2.png)

この場合、「所在地」が「東京 23 区」である不動産は「成約価格」が増加する傾向にありそうだ、と読み取ることができます。
より詳細な寄与度の見方については、{{% a_in "../../tips/result/contribution/" "予測寄与度の概要" %}}を参照してください。

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/result/contribution/" "予測寄与度の概要" %}}
  {{% /div_relitem %}}
