---
title: "ROCカーブとAUC"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["ROC", "AUC", "ROCAUC", "感度", "曲線", "受信者操作特性"]
---

**ROC カーブ** (Receiver Operatorating Characteristic curve) は 2 値分類の予測モデルが出す予測確率を使って描かれる曲線です。グラフ中の黄色の実線が ROC カーブを示します。

予測モデルがランダムに予測をしている場合、ROC カーブは左下から右上への対角線 (グラフ上の破線) に重なります。ROC カーブが左上に膨らむほど良い予測モデルとなります。カーブの形状に関する詳細な理解は難しいので、まずは AUC の大小を基準にモデルの良し悪しを判断すると良いでしょう。

![](../img/t_slide35_tmp_roc.png)

**AUC** (Area Under the Curve) は二値分類の評価指標の一つです。ROC カーブの下 (黄色の領域) の面積を指します。大きければ大きいほど良く、最良で 100%となります。予測モデルがランダムに予測をしているときは AUC の値が 50%になり、反対にモデルが非常に精度高く予測できているときは AUC の値が 100%に近づきます。

AUC は Accuracy, Recall, Precision, F 値と異なり、予測確率から予測結果を得るための閾値の影響を受けないため、二値分類の予測精度の評価値としてよく利用されます。

{{% div_relitem contents-bottom %}}

- {{% a_in "../../tips/result/eval_bin/" "予測精度の概要（二値分類）" %}}
  {{% /div_relitem %}}
