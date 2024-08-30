---
title: "関連データ"
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
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["データ結合", "リレーショナル"]
---

{{% cloud_only_info %}}
データ結合は{{% a_in "../desktop/" "デスクトップ版" %}}のみ利用可能です。
{{% /cloud_only_info %}}

データ結合における**関連データ**とは、予測モデル作成(学習)用データに対して関係性のある情報を持つデータを指します。

### Prediction One での関連データの扱い

Prediction One では、{{% a_in "../../terminology/join_column/" "横結合" %}}と{{% a_in "../../terminology/join_row/" "縦結合" %}}
により、関連データを結合することが可能です。
関連データは直接予測モデル作成(学習)用データと結合する必要があります。関連データ同士の結合には対応していません。

データ結合についての説明は、{{% a_in "../../tips/new_features/join_dataset/" "データ結合" %}}も参照してください。

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/new_features/join_dataset/" "データ結合" %}}
- {{% a_in "../../terminology/join_column/" "横結合" %}}
- {{% a_in "../../terminology/join_row/" "縦結合" %}}
  {{% /div_relitem %}}
