---
title: "結合キー項目"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2400
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["データ結合", "結合キー"]
---

{{% cloud_only_info %}}
データ結合は{{% a_in "../desktop/" "デスクトップ版" %}}のみ利用可能です。
{{% /cloud_only_info %}}

データ結合における**結合キー項目**とは、予測モデル作成(学習)用データと関連データの間の対応を表現するための、共通の値を持つ項目を指します。
関連データを{{% a_in "../../terminology/join_column/" "横結合" %}}する時、結合キー項目の値の一致を見ることで結合処理が実行されます。

### Prediction One での結合キー項目の扱い

![](../../operating_instruction/img/t_slide61.png)

Prediction One ではデータ結合画面において、関連データが追加されると、予測モデル作成(学習)用データと関連データの結合キー項目の自動判定をおこない、結合関係を表示します。
自動判定では、項目の名前・データタイプ・値の一致度を元に判定が行われ、もっとも一致度の高い項目が結合キー項目と判定されます。

想定と異なる結合キーが選択されている場合は、結合キー項目変更プルダウンから結合キー項目を変更することが可能です。

データ結合についての説明は、{{% a_in "../../tips/new_features/join_dataset/" "データ結合" %}}も参照してください。

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/new_features/join_dataset/" "データ結合" %}}
- {{% a_in "../../terminology/join_column/" "横結合" %}}
  {{% /div_relitem %}}
