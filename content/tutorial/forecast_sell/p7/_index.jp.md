---
title: "予測モデルの作成"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 7
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: [""]
tutorial_page:
  is_next_exists: true
---

{{% div_slide "ステップ1" normal first-page %}}

![](../img/t_slide4.png)

メイン画面が表示されますが、まだ予測モデルは作成されていないので、空の状態です。「予測モデルの新規作成」をクリックしてください。
{{% /div_slide %}}

{{% div_slide "ステップ2" normal %}}
![](../img/t_slide5.png)

予測モデル作成(学習)用データである `1_販売台数.csv` を指定してください。<br/>
{{% desktop_only %}}
データはウィンドウへのドラッグ&ドロップか 「ファイルを指定する」で読み込むことができます。<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
サンプルデータは、「アップロード済みのデータから選択」をクリックし、「サンプル」タブのデータ一覧から選択してください。
{{% /cloud_only %}}
{{% tutorial_file_location "/ja-JP/doc/sample_dataset/use_case/製造管理_販売台数予測による製造計画の改善" %}}
{{% /div_slide %}}

{{% div_slide "ステップ3" normal %}}
![](../img/t_slide6.png)

データ読み込みが完了すると、この画面が表示されます。<br/>
予測したい項目を 1 つ選択してください。
このチュートリアルでは、「販売台数（予測対象）」という項目を選択してください。
選択後、「次へ」ボタンをクリックしてください。<br/>
{{% /div_slide %}}

{{% div_slide "ステップ4" normal %}}
![](../img/t_slide7.png)

今回のチュートリアルでは、2019 年 3 月までの月ごとの販売台数と日経平均株価から、その先にどれくらいの販売が見込まれるかを予測します。
「時系列予測モードを使用する」をクリックし、「次へ」をクリックしてください。
{{% /div_slide %}}

{{% div_slide "ステップ5" normal %}}
![](../img/t_slide8.png)

この画面ではいつの「販売台数」を予測したいかを設定します。

データは 2019 年 3 月まで存在しており、今は 2019 年 4 月から 2020 年 3 月までの販売台数を予測したいとします。予測期間に「1 か月先」から「12 カ月先」まで予測するように指定します。

図から、どの期間の予測を行うモデルを作成するかを確認できます。「2019/04/01」～「2020/03/01」になっていることを確認できたら「予測モデルを作成」をクリックしてください。

![](../img/t_slide22.png)

予測したい項目以外の項目という設定もありますが、ここでは「自動で設定」のまま進みます。

{{< notice note >}}
こちらの設定の詳細については、{{% a_in "../../../tips/new_features/timeseries_features/" "予測したい項目以外の項目" %}}をご確認ください。<br/>
「個別に設定」を使用するチュートリアルは、{{% a_in "../../forecast_the_number_of_visitors/" "こちら" %}}です。
{{</ notice >}}

{{% /div_slide %}}

{{% div_slide "ステップ6" normal %}}
![](../img/t_slide9.png)

学習が開始されますので、完了までお待ちください。前処理 → 予測モデル学習 → 精度評価の処理が実行されます。<br/>
待ち時間の見積もりが上部に表示されます。データ量が多いほど時間がかかります。<br/>
学習完了後、完了ボタンをクリックしてください。<br/>
{{% /div_slide %}}