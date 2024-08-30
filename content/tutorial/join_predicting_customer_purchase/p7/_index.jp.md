---
title: "予測モデルの作成1 : 予測モデル作成(学習)用データの入力"
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

予測モデル作成(学習)用データである`1_有料会員登録情報.csv`を指定してください。<br/>
{{% desktop_only %}}
データはウィンドウへのドラッグ&ドロップか 「ファイルを指定する」で読み込むことができます。<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
サンプルデータは、「アップロード済みのデータから選択」をクリックし、「サンプル」タブのデータ一覧から選択してください。
{{% /cloud_only %}}

{{% tutorial_file_location "/ja-JP/doc/sample_dataset/use_case/マーケティング_有料会員登録予測に基づく営業施策の決定" %}}
{{% /div_slide %}}

{{% div_slide "ステップ3" normal %}}
![](../img/t_slide9.png)

データ読み込みが完了すると、この画面が表示されます。<br/>
予測したい項目を 1 つ選択してください。(このチュートリアルでは、「有料会員登録(予測対象)」という項目を選択してください)<br/>
選択後、右上にある**詳細設定**のチェックボックスをクリックし、詳細設定モードに入ります。<br/>

![](../img/t_slide10.png)
詳細設定モード画面右下の **「データ結合」ボタン**をクリックしてください。<br/>
{{% /div_slide %}}
