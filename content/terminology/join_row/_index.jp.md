---
title: "縦結合"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["データ結合", "結合"]
---

{{% cloud_only_info %}}
データ結合は{{% a_in "../desktop/" "デスクトップ版" %}}のみ利用可能です。
{{% /cloud_only_info %}}

データ結合における**縦結合**とは、予測モデル作成(学習)用データに関連データを行方向に連結するようなデータ結合方法を指します。

関連データの項目名群と予測モデル作成(学習)用データの項目名群が完全に一致する場合、Prediction One は縦結合を行います。
縦結合により、予測モデル作成(学習)用データの行数が増加します。

データ結合についての説明は、{{% a_in "../../tips/new_features/join_dataset/" "データ結合" %}}も参照してください。

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/new_features/join_dataset/" "データ結合" %}}
- {{% a_in "../../terminology/join_additional_column/" "追加項目（データ結合）" %}}
- {{% a_in "../../terminology/join_column/" "横結合" %}}
  {{% /div_relitem %}}
