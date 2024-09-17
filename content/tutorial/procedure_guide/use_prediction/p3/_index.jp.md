---
title: "予測分析プロジェクトの始まり"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 3
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

{{% div_slide "予測分析の進め方の把握" normal first-page %}}
「{{% a_in "../../../../prediction_one/process_of_predictive_analytics/" "予測分析の流れ" %}}」を読んでみると、予測分析は「課題を設定する→データを用意する→データを前処理する→予測モデルを作成する→精度を確かめる→予測をする」の順番で進むらしい…。<br/>
 <br/>
![](../img/t_slide4.png)
{{% /div_slide %}}

{{% div_slide "知らない単語を「予測分析の基礎知識」で調べる" normal %}}
ところで予測分析ってなんだ？どうやら機械学習の一種みたいなんだが…。と思ったら、「{{% a_in "../../../../prediction_one/knowledge_of_predictive_analytics/" "予測分析の基礎知識" %}}」というリンクがある。クリック。<br/>
ふむふむ、「{{% a_in "../../../../prediction_one/knowledge_of_predictive_analytics/ai_ml_dl/" "AIと機械学習と深層学習" %}}」によると予測分析は機械学習と深層学習を組み合わせたものらしい。そもそも今までAIとか機械学習とかディープラーニングとか何となく単語だけは知っていて区別がついていなかったが、厳密には違う意味なのか…。<br/>
 <br/>
![](../img/t_slide5.png)
 <br/>
それに「{{% a_in "../../../../prediction_one/knowledge_of_predictive_analytics/about_ml/" "機械学習とは" %}}」によると、予測分析は機械学習の中でも表形式データを対象にした教師あり学習のことらしい…。ちょっとAIについてわかってきた気がするぞ…！<br/>
 <br/>
![](../img/t_slide6.png)
{{% /div_slide %}}

{{% div_slide "最初にやるべきタスクの把握" normal %}}
ひとまず予測分析をするにあたって最初は「課題を設定する」んだな！<br/>
 <br/>
![](../img/t_slide7.png)
{{% /div_slide %}}


{{% div_slide "まとめ" summary %}}
- 予測分析はおおまかに「課題を設定する→データを用意する→データを前処理する→予測モデルを作成する→精度を確かめる→予測をする」の順番で進みます。これからそれぞれのタスクについて詳しく見ていきます。
- 予測分析プロジェクトを進めていくうえでぜひ知っておいてほしいことを「{{% a_in "../../../../prediction_one/knowledge_of_predictive_analytics/" "予測分析の基礎知識" %}}」にまとめています(難しい数式を使った説明はありません)。わからないことがあったら是非確認してみてください。先にこのコンテンツを全て読んでしまうのもおすすめです。
- タケシさんが「{{% a_in "../../../../prediction_one/process_of_predictive_analytics/" "予測分析の流れ" %}}」や「{{% a_in "../../../../prediction_one/knowledge_of_predictive_analytics/" "予測分析の基礎知識" %}}」のどこを読んで作業を進めたのか、実際に同じページを確認してみましょう。
<link rel="stylesheet", href="../../../../../static/css/help.css">
<a href="../p4/index.html" class="nav nav-tutorial-next">「『1.1 予測分析が最適なソリューションなのか確認する』に取り組む」にすすむ</a>
{{% /div_slide %}}
