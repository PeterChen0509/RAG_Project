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

![](../img/t_slide7.png)

メイン画面が表示されますが、まだ予測モデルは作成されていないので、空の状態です。「予測モデルの新規作成」をクリックしてください。
{{% /div_slide %}}

{{% div_slide "ステップ2" normal %}}
![](../img/t_slide8.png)

予測モデル作成(学習)用データである`1_サービス成約.csv`を指定してください。<br/>
{{% desktop_only %}}
データはウィンドウへのドラッグ&ドロップか 「ファイルを指定する」で読み込むことができます。<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
サンプルデータは、「アップロード済みのデータから選択」をクリックし、「サンプル」タブのデータ一覧から選択してください。
{{% /cloud_only %}}

{{% tutorial_file_location "/ja-JP/doc/sample_dataset/use_case/営業_成約予測による有望顧客絞り込み" %}}
{{% /div_slide %}}

{{% div_slide "ステップ3" normal %}}
![](../img/t_slide9.png)

データ読み込みが完了すると、この画面が表示されます。<br/>
予測したい項目を 1 つ選択してください。(このチュートリアルでは、「成約有無(予測対象)」という項目を選択してください)選択後、「予測モデルを作成」ボタンをクリックしてください。<br/>
{{% /div_slide %}}

{{% div_slide "ステップ4" normal %}}
![](../img/t_slide10.png)

学習が開始されますので、完了までお待ちください。前処理 → 予測モデル学習 → 精度評価 → 予測寄与度分析の４つの処理が実行されます。<br/>
待ち時間の見積もりが上部に表示されます。データ量が多いほど時間がかかります。<br/>
学習完了後、完了ボタンをクリックしてください。<br/>
{{% /div_slide %}}
