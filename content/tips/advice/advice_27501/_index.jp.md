---
title: "精度が改善しきらなくても業務に活用する方法をご紹介します (時系列予測)"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4
draft: false
# metaタグのパラメータ
meta:
  description: "予測分析ツールPrediction Oneが提案する精度改善のための改善ヒントについて説明するページです。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  ["ヒント","改善ヒント","tips","精度改善","寄与度"]
toc: true
---

### 説明

予測精度が悪い場合でも、一部の予測については活用できる場合があります。
例えば、頻出する数値の範囲に絞ってみると、精度良く予測できている可能性があります。

以下の画像は{{% a_in "./../../../tutorial/real_estate_price_forecast/" "不動産の成約価格の予測" %}}のチュートリアルでの
{{% a_in "./../../../terminology/predict_true_distribution/" "予測の分布" %}}です。
グラフを見ると不動産価格が高い領域では予測と実際の値が離れやすい傾向にあることが分かります。
このような場合は、予測値が高い場合はPrediction Oneの予測だけでなく人の目も使って確認をすると良いでしょう。

![](../img/t_slide24.png)

(※時系列予測では画像のような予測の分布が表示されませんが、Excelを使って似たようなグラフを描画することで特に精度の悪い領域を特定できます。)

### 関連資料

- {{% a_in "./../../../tutorial/real_estate_price_forecast/" "不動産の成約価格の予測" %}}

