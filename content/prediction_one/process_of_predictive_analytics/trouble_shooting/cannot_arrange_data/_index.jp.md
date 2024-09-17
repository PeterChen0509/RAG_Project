---
title: "前処理で表形式データを用意出来なかった場合"
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
keywords: ["予測分析", "機械学習", "AI", "予測", "未来予測", "未来", "将来"]
---

{{< notice note >}}
行が各レコード、列がそれを説明する情報という1つの表の形でデータを用意できなかった場合に参考にしていただきたいページです。<br/>
データの用意方法については「{{% a_in "../../prepare_data/" "2 データを用意する" %}}」をご覧ください。
{{</ notice >}}

予測分析は表形式データに対する予測技術であるため、行が各レコード、列がそれを説明する情報というフォーマットの表形式データは必須です。このフォーマットに従わないデータ（音声・画像・動画などの非構造化データ。詳しくは「<b>{{% a_in "../../../knowledge_of_predictive_analytics/" "予測分析の基礎知識" %}} ▶ {{% a_in "../../../knowledge_of_predictive_analytics/about_data/" "データとは" %}}</b>」をご覧ください。）は適切に前処理をする必要があります。<br/>
例えば、音声データであれば数ミリ秒ごとの波形（周波数）データに変換することで表形式で表せるようにしたり、画像データであれば画像中の重要なピクセルの平均RGB値を利用したりすることが考えられます。<br/>
一方でこのような非構造化データの取り扱いに特化した機械学習技術（≠予測分析）も存在します。非構造化データを扱いたい場合は予測分析が最適なソリューションなのか検討が必要です。<br/>
また、社内で情報が散らばっており個々のデータは表形式ではあるが、1つの表にまとまっていない場合もあるかもしれません。Prediction Oneには「{{% a_in "../../../../tips/new_features/dataprep_custom/" "データ準備機能" %}}」があり複数ファイルから1つの表形式データを作成することもできます。<br/>
これらを踏まえ追加の情報を1つの表形式で用意出来そうな場合は「<b>{{% a_in "../../prepare_data/" "2 データを用意する" %}}</b>」をもう一度してみましょう。<br/>
もし設定した課題で、行が各レコード、列がそれを説明する情報というフォーマットの表形式データを用意出来そうにない場合は、課題を設定しなおす必要があります。「<b>{{% a_in "../../setting_theme/" "1 課題を設定する" %}}</b>」を参考にもう一度課題を設定してみましょう。