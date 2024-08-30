---
title: "顧客リストの作成"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 13
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

{{% div_slide "苦情タイプの割り当て" normal  first-page %}}

予測結果のファイルから、各レビュー文に対してもっとも予測確率の高い苦情タイプをそのレビュー文の苦情タイプとします。

![](../img/t_slide20.png)

実際は、予測精度は 100%ではないので間違えることもあります。もっとも高い予測確率の値が大きくない場合は、予測の確信度が低いことになりますので、こういったケースは人間がチェックする方が良い場合もあります。
{{% /div_slide %}}
