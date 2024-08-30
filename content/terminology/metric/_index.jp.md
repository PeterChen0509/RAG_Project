---
title: "精度評価"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2500
draft: false
# metaタグのパラメータ
meta:
  description: "精度評価とは、予測モデル作成(学習)用データから作成した予測モデルがどれくらいの性能であるか評価することを指します。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["評価値", "精度評価", "評価指標", "予測精度"]
---

**精度評価**とは、予測モデル作成(学習)用データから作成した予測モデルがどれくらいの性能であるか評価することを指します。
Prediction One では、予測モデル作成(学習)用データの一部をランダムに抜き取り残りのデータを用いて予測モデルを作成し、作成した予測モデルを先ほど抜き取ったデータに対して予測を行います。
その予測と正解を比較することで、これまでに見たことの無いデータに対してどれくらい予測を当てることができるかを評価します。

「評価用データを指定」からファイルを指定することで、精度評価に使用するデータを指定することもできます。

精度評価指標は、問題設定によって変わります。各指標の詳細は以下のリンク先を参照してください。

### 二値分類の評価指標

- {{% a_in "../../tips/result/eval_bin/" "TIPS「予測精度の概要（二値分類）」" %}}
- {{% a_in "../roc_curve_auc/" "AUC" %}}
- {{% a_in "../accuracy/" "正解率（Accuracy）" %}}
- {{% a_in "../precision/" "精度（Precision）" %}}
- {{% a_in "../recall/" "再現率（Recall）" %}}
- {{% a_in "../f_value/" "F値" %}}

### 多値分類の評価指標

- {{% a_in "../../tips/result/eval_mul/" "TIPS「予測精度の概要（多値分類）」" %}}
- {{% a_in "../accuracy/" "正解率（Accuracy）" %}}
- {{% a_in "../precision/" "精度（Precision）" %}}
- {{% a_in "../recall/" "再現率（Recall）" %}}
- {{% a_in "../f_value/" "F値" %}}

### 数値予測の評価指標

- {{% a_in "../../tips/result/eval_reg/" "TIPS「予測精度の概要（数値予測）」" %}}
- {{% a_in "../mean_absolute_error/" "誤差平均" %}}
- {{% a_in "../rmse/" "RMSE" %}}
- {{% a_in "../median_absolute_error/" "誤差中央値" %}}
- {{% a_in "../median_absolute_error_ratio/" "誤差率中央値" %}}
- {{% a_in "../r2/" "決定係数" %}}
