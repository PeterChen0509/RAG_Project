---
title: "予測分析の流れ"
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

<link rel="stylesheet", href="../../../static/css/help.css">

Prediction Oneでは過去の実績データを学習し将来の値を予測する「予測モデル」の作成が行えます。<br/>
予測モデルを活用することで、今まで属人的に予測を行っていた業務を自動化したり高精度化できますが、良い予測分析を行うには予測モデルの作成以外にも様々なステップがあります。<br/>
正しいステップを踏まないと、データの用意の仕方がイマイチでポテンシャル未満の予測精度しか出なかったり、精度の高い予測モデルはできたけどよく考えるとそのモデルの予測結果を業務に活用できる場面がなかったり、予測分析がその技術を最大限発揮できなくなってしまいます。<br/>
予測分析を使って業務で成果を出すためには正しいステップを踏むと効率的です。ここでは良い予測分析の流れを説明します。予測分析で使われる機械学習の技術に関して知りたい方は「<b>{{% a_in "../knowledge_of_predictive_analytics/" "予測分析の基礎知識" %}}</b>」を参考にしてみてください。<br/>

{{< notice note >}}
ここで紹介する予測分析の流れに沿った進行をサポートする機能として、「<b>{{% a_in "../../tips/new_features/procedure_guide/" "進め方ガイド" %}}</b>」があります。
{{</ notice >}}

{{% div_slide "1 課題を設定する" normal first-page %}}
まずはどんな問題をPrediction Oneで解きたいのか課題設定をします。解決したい課題をPrediction Oneで解ける形にしたり、業務に活用できる予測結果を考える必要があります。<br/>
<a href="./setting_theme/index.html" class="nav nav-tutorial-next">「1 課題を設定する」を詳しく見る</a>
{{% /div_slide %}}

{{% div_slide "2 データを用意する" normal %}}
解きたい課題を設定出来たらその課題に必要なデータを用意します。良い予測モデルを作成するためにデータを収集したり、手元のデータを予測分析に利用できる形に整えたりします。<br/>
課題にあったデータが入手できないとわかった場合は、課題設定をやり直すこともあります。
<a href="./prepare_data/index.html" class="nav nav-tutorial-next">「2 データを用意する」を詳しく見る</a>
{{% /div_slide %}}

{{% div_slide "3 予測モデルの作成をする" normal %}}
データが用意出来たら予測モデルの作成をします。本来だと適切なアルゴリズムの選定やパラメータ調整が必要ですが、Prediction Oneが自動で行うため簡単に予測モデルの作成が完了します。
<a href="./create_model/index.html" class="nav nav-tutorial-next">「3 予測モデルの作成をする」を詳しく見る</a>
{{% /div_slide %}}

{{% div_slide "4 精度を確かめる" normal %}}
出来上がった予測モデルの良し悪しを確認します。精度が不十分であれば前のいずれかのステップに戻ります。ある程度精度が出たら精度を突き詰めるのではなく次に進むことも重要です。
<a href="./check_model/index.html" class="nav nav-tutorial-next">「4 精度を確かめる」を詳しく見る</a>
{{% /div_slide %}}

{{% div_slide "5 予測をする/寄与度を活用する（業務への適用）" normal %}}
最後は予測結果を用いて実際にアクションを起こすステップです。予測分析の効果を確認するために、今までのプロセスとPrediction Oneを使ったプロセスでどのような違いが生まれたか計測します。
<a href="./apply_to_work/index.html" class="nav nav-tutorial-next">「5 予測をする/寄与度を活用する（業務への適用）」を詳しく見る</a>
{{% /div_slide %}}