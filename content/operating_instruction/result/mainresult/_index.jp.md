---
title: "評価結果画面"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["評価サマリ", "ソート"]
---

この画面では、学習された予測モデルの予測精度などの評価結果を閲覧できます。
評価では、学習に使用していないデータに対して、学習した予測モデルで予測を実行し、
予測結果と正解の比較により、予測精度を評価します。
各予測タイプ (二値分類、多値分類、数値予測) に即した内容が表示されます。
サマリ、寄与度、精度、改善ヒント、モデルの詳細をクリックすることで表示内容を切り替えることができます。

![](../../img/t_slide24.png)

{{% div_method_area "予測精度の概要を理解する" %}}
{{% step_n_area2 1 "予測精度サマリをご覧ください。" %}}
各予測タイプの主要な精度評価指標と、予測精度レベル、その説明文が表示されます。
予測精度レベルは星の数が多いほど良いことを示します。
データ数を増やすと精度が上がると判定された場合は、その旨がテキストとして表示されます。

精度が良ければこのモデルの活用方法へのリンクが表示されます。
改善すべきところがある場合には改善方法を確認できる【改善ヒント】タブへのボタンが表示されます。
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "寄与度の概要を理解する" %}}
{{% step_n_area2 1 "寄与度サマリをご覧ください。" %}}
各入力項目について、学習した予測モデルがどの程度重要視しているか・予測に有効かを表します。
棒グラフが長いほど重要度・有効度が高いことを表します。
重要度・有効度の高い項目が予測結果に大きな影響を与えています。
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "表示内容を画像で保存する" %}}
{{% step_n2 1 "画像保存ボタンをクリックしてください。 " %}}
{{% step_n2 2 "画像を保存するフォルダーの名前を指定してください。表示内容が画像(png)で保存されます。 " %}}
{{% /div_method_area %}}

{{% div_method_area "寄与度の詳細を閲覧する" %}}
{{% step_n_area2 1 "「寄与度」ボタンをクリックしてください。" %}}
![](../../img/t_slide25.png)
{{% /step_n_area2 %}}
{{% /div_method_area %}}
