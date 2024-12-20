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
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: [""]
tutorial_page:
  is_next_exists: true
---

{{% div_slide "ステップ1" normal first-page %}}

![](../img/t_slide7.png)

今回更新を行いたいモデルに対し、「モデルの更新」ボタンをクリックすることで新しいモデルを作成できます。
ファイルの入力が終わったら次へボタンを押して、次の画面へ進むことができます。
{{% /div_slide %}}

{{% div_slide "ステップ2" normal %}}
![](../img/t_slide8.png)

予測モデル作成(学習)用データである`最新データ_プレミアムサービス購入.csv`を指定してください。<br/>
{{% desktop_only %}}
データはウィンドウへのドラッグ&ドロップか 「ファイルを指定」で読み込むことができます。<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
サンプルデータは、「アップロード済みのデータから選択」をクリックし、「サンプル」タブのデータ一覧から選択してください。
{{% /cloud_only %}}

{{% tutorial_file_location "/ja-JP/doc/sample_dataset/use_case/マーケティング_最新の顧客行動に基づくターゲティング" %}}
{{% /div_slide %}}

{{% div_slide "ステップ3" normal %}}
![](../img/t_slide9.png)

データ読み込みが完了すると、この画面が表示されます。<br/>
予測したい項目は前回学習時に使用したものと同様です。現在の項目の設定が正しいかを確認した後、 「次へ」ボタンをクリックしてください。<br/>
{{% /div_slide %}}

{{% div_slide "ステップ4" normal %}}
![](../img/t_slide10.png)

更新前のモデルと更新後のモデルを比較するための評価用データを指定します。
評価用データをファイルから指定する場合は、「ファイルを指定」ボタンをクリックします。
{{% /div_slide %}}

{{% div_slide "ステップ5" normal %}}
![](../img/t_slide11.png)

学習の時と同様に、「ファイルを開く」ボタン、もしくはドラッグ&ドロップにより評価用データを入力します。
今回のチュートリアルではサンプルデータの`最新データ_プレミアムサービス購入（評価用）.csv`を評価用データに使用します。

{{% /div_slide %}}


{{% div_slide "ステップ6" normal %}}
![](../img/t_slide12.png)

「予測モデルを作成」ボタンをクリックすることで学習が開始されますので、完了までお待ちください。前処理 → 予測モデル学習 → 精度評価 → 予測寄与度分析の４つの処理が実行されます。<br/>
待ち時間の見積もりが上部に表示されます。データ量が多いほど時間がかかります。<br/>
学習完了後、完了ボタンをクリックしてください。<br/>
{{% /div_slide %}}

