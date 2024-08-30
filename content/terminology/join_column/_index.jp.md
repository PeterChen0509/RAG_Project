---
title: "横結合"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 8500
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["データ結合", "結合", "ジョイン"]
---

{{% cloud_only_info %}}
データ結合は{{% a_in "../desktop/" "デスクトップ版" %}}のみ利用可能です。
{{% /cloud_only_info %}}

データ結合における**横結合**とは、項目を増やす（ファイルの列方向を増やす）様なデータ結合方法のことです。

Prediction One では、関連データの結合キー項目値に重複がない（ユニークである）場合、横結合は結合キーの値で各行を対応付け、項目をコピーをする事により実行されます。

関連データの結合キー項目値に重複がある場合、項目値の平均やユニーク数などのさまざまな集計方法により、関連データの情報をまとめ上げます。
集計方法の種類については、{{% a_in "../../terminology/join_additional_column/" "追加項目（データ結合）" %}}を参照してください。

データ結合についての説明は、{{% a_in "../../tips/new_features/join_dataset/" "データ結合" %}}も参照してください。

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/new_features/join_dataset/" "データ結合" %}}
- {{% a_in "../../terminology/join_additional_column/" "追加項目（データ結合）" %}}
- {{% a_in "../../terminology/join_row/" "縦結合" %}}
  {{% /div_relitem %}}
