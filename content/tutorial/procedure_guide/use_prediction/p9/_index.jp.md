---
title: "「4.1 作成した予測モデルの精度と目標としていた精度を比べる」に取り組む"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 9
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  [""]
tutorial_page:
  is_next_exists: false
---

{{% div_slide "「4.1.1 目標に即した予測モデルの精度を確認/算出する」に取り組む" normal first-page %}}
「{{% a_in "../../../../prediction_one/process_of_predictive_analytics/check_model/" "4 精度を確かめる" %}}」には、<br/>

- {{% a_in "../../../../prediction_one/process_of_predictive_analytics/check_model/check_metrics/" "4.1 作成した予測モデルの精度と目標としていた精度を比べる" %}}
- {{% a_in "../../../../prediction_one/process_of_predictive_analytics/check_model/check_feature_importance/" "4.2 寄与度を確認する" %}}

のステップがあるのか…。まずは「{{% a_in "../../../../prediction_one/process_of_predictive_analytics/check_model/check_metrics/" "4.1 作成した予測モデルの精度と目標としていた精度を比べる" %}}」と…。ああ、「{{% a_in "../../../../prediction_one/process_of_predictive_analytics/setting_theme/setting_detailed_theme/" "1.2 予測分析で解きたい課題を設定する" %}}」で設定した目標と今回作成した予測モデルの精度を比べればよいのか。一応細かいタスクも見てみよう。<br/>
 <br/>
![](../img/t_slide26.png)
 <br/>
「4.1.1 目標に即した予測モデルの精度を確認/算出する」によると、個別のユースケースに即した評価指標は自ら計算する必要があるようだ。確かに自分の場合もPrediction Oneが自動で算出する精度指標を目標にはしていないから自分で計算しないとな…。ええと、評価データと評価データに対する予測結果を出力して計算すればいいんだな…！<br/>
 <br/>
![](../img/t_slide27.png)
 <br/>
{{% /div_slide %}}

{{% div_slide "「4.1.2 目標としていた精度を比べ予測モデルの精度が十分であることを確認する」に取り組む" normal %}}
精度も算出できたから次は「4.1.2 目標としていた精度を比べ予測モデルの精度が十分であることを確認する」だ。予測モデルだと上位50人中パーソナルトレーニング申込に至ったのは31人で62%か…。もともと70%を目標にしていたから、目標には届いていないな…。<br/>
お、「{{% a_in "../../../../prediction_one/process_of_predictive_analytics/trouble_shooting/unachieved_metrics/" "十分な精度が出なかった場合" %}}」のリンクがある。なるほど…。今はBIツールのデータをそのまま引っ張ってきただけだからユーザ一人ひとりの情報量、つまり項目数は多くないかもな。ユーザの年齢や性別、入会日といった基本的な情報は入っているけど、ジムまでの近さ（住所）、利用時間帯、利用頻度、平均滞在時間とか、もっとパーソナルトレーニングに入ってくれそうかどうかの参考になりそうな情報があるはずだ。<br/>
となると、「{{% a_in "../../../../prediction_one/process_of_predictive_analytics/prepare_data/" "2 データを用意する" %}}」に戻ってもう一度トライする必要があるということだ。<br/>
 <br/>
![](../img/t_slide28.png)
![](../img/t_slide29.png)
 <br/>
{{% /div_slide %}}

{{% div_slide "まとめ" summary %}}
このページでタケシさんは以下のタスクを完了しました。

- 4.1.1 目標に即した予測モデルの精度を確認/算出する

ここではタケシさんになったと思って進め方ガイドのチェックを埋めてみましょう。
 <br/>
![](../img/t_slide30.png)
 <br/>
一方で、以下のタスクを完了できず、「{{% a_in "../../../../prediction_one/process_of_predictive_analytics/prepare_data/" "2 データを用意する" %}}」に戻ることになりました。「『2 データを用意する』をやり直す」ボタンを押してやるべきタスクに戻ることができます。こちらもタケシさんと同様にボタンを押してみましょう。

- 4.1.2 目標としていた精度を比べ予測モデルの精度が十分であることを確認する

 <br/>
![](../img/t_slide31.png)
 <br/>
{{< notice note >}}
タケシさんは「4.1.2 目標としていた精度を比べ予測モデルの精度が十分であることを確認する」まで進めたところで精度が目標に達していないことが分かりました。そこで「{{% a_in "../../../../prediction_one/process_of_predictive_analytics/trouble_shooting/unachieved_metrics/" "十分な精度が出なかった場合" %}}」を読みパーソナルトレーニングの申し込みに関係のありそうな項目をもっと増やせるかもしれないことに気づきます。ただ、最初から項目を十分用意せずに予測モデルの作成を行ったのは間違いではありません。予測精度が十分出るかどうかはやってみるまで分からないからです。<br/>
予測分析プロジェクトでは予測モデルの作成とデータの改善を何度も繰り返すことがよくあります。あなたもご自身のケースで予測モデルを作成する際は、一度予測モデルを作って諦めるのではなくデータの改善にも取り組んでみましょう。
{{</ notice >}}
<link rel="stylesheet", href="../../../../../static/css/help.css">
<a href="../p10/index.html" class="nav nav-tutorial-next">「『2 データを用意する』をやり直す」にすすむ</a>
{{% /div_slide %}}
