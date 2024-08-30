---
title: "予測"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 11
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
![](../img/t_slide21.png)

作成した予測モデルを利用して、将来１週間（2019/09/16 ～ 09/22）の来店数を予測します。
本チュートリアルでは、事前に準備した、予測用のサンプルデータを利用します。

{{% tutorial_file_location "/ja-JP/doc/sample_dataset/use_case/店舗管理_来客数予測による仕入れ量決定3" %}}
{{% /div_slide %}}

{{% div_slide "ステップ2" normal%}}
![](../img/t_slide18.png)

では、この予測モデルで予測してみましょう。

{{% desktop_only %}}
予測用データである `2_来店数（予測用）.csv`を指定してください。<br/>
データはウィンドウへのドラッグ&ドロップか 「ファイルを指定する」で読み込むことができます。<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
予測用データである `2_来店数（予測用）.csv`を指定してください。<br/>
サンプルデータは、「アップロード済みのデータから選択」をクリックし、「サンプル」タブのデータ一覧から選択してください。
{{% /cloud_only %}}
{{% /div_slide %}}

{{% div_slide "ステップ3" normal %}}
![](../img/t_slide19.png)

{{% desktop_only %}}
読み込んだ予測用データ `2_来店数（予測用）.csv` をプレビューしています。
{{% /desktop_only %}}
{{% cloud_only %}}
読み込んだ予測用データ `2_来店数（予測用）.csv` をプレビューしています。
{{% /cloud_only %}}
今から「？」となっている来店数(予測対象)を予測します。

{{% desktop_only %}}
「予測結果プレビュー」をクリックしてください。
{{% /desktop_only %}}
{{% cloud_only %}}
「予測結果プレビュー」をクリックしてください。予測結果のプレビュー画面が表示されるまで、しばらくお待ちください。
{{% /cloud_only %}}
{{% /div_slide %}}

{{% div_slide "ステップ4" normal %}}
![](../img/t_slide20.png)

{{% desktop_only %}}
予測する準備ができました。「予測して保存」をクリックし、予測を実行します。
予測結果を保存するファイル名を指定した後、予測を行います。
{{% /desktop_only %}}
{{% cloud_only %}}
「予測結果を保存」をクリックし、「ファイル名」を入力し、「保存」をクリックしてください。
{{% /cloud_only %}}
{{% /div_slide %}}


{{% div_slide "ステップ5" normal %}}
予測が完了すると以下の画面が表示され、指定したファイルに予測結果が保存されています。

![](../img/t_slide22.png)
{{% /div_slide %}}

{{% div_slide "ステップ6" normal %}}

予測結果は以下のような形式で出力されます（オプション設定によっては違う形式になります）。
各日付に対して、予測来店数が書かれています。

![](../img/t_slide23.png)
{{% /div_slide %}}
