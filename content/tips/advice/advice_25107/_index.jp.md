---
title: "要因分析にPrediction Oneを使用していますか？そのような場合の事例を紹介します。"
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

Prediction Oneは、何か予測したい対象を一つ選び、それを予測する予測モデルを作成し、未知のデータについて予測対象を予測分析するツールです。
しかし、どの項目が予測対象への影響度が強いのかを分析したい場合は、「寄与度」画面から影響度の強い項目を確認できます。
次のアクションを起こす際に影響度の強い項目から順番に施策を行うことで、効率的に予測対象を改善できると考えられます。

例えば、チュートリアルの{{% a_in "./../../../tutorial/targeting_based_on_predictive_customer_behavior/" "顧客行動予測に基づいたターゲティング" %}}を見てみます。<br/>
このチュートリアルでは顧客ランクの寄与度が最も高いことが分かり、かつ顧客ランクがプラチナだと購入ありになる傾向があると分かります
 ({{% a_in "./../../../tutorial/targeting_based_on_predictive_customer_behavior/p9/" "こちら" %}}のステップ4参照)。
このことからプレミアムサービスの購入確率を上げるには顧客ランクをゴールドやシルバーからプラチナに上げる施策が効果的であると読み取れます。

![](../img/t_slide20.png)

寄与度の活用方法について、詳しくは以下の関連資料をご覧ください。

### 関連資料

- {{% a_in "./../../../tips/result/contribution/" "予測寄与度の概要" %}}
- {{% a_in "./../../../tips/result/contribution_bin/" "予測寄与度の読み解き方と活用方法（二値分類）" %}}
- {{% a_in "./../../../tips/result/contribution_mul/" "予測寄与度の読み解き方と活用方法（多値分類）" %}}
- {{% a_in "./../../../tips/result/contribution_timeseries/" "予測寄与度の読み解き方と活用方法（時系列予測）" %}}

