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

![](../img/t_slide19.png)

この画面にて、予測用データを指定します。今回のチュートリアルで使用する予測用データの内容を確認しましょう。
{{% /div_slide %}}

{{% div_slide "ステップ2" normal %}}
![](../img/t_slide20.png)
![](../img/t_slide21.png)

作成した予測モデルを利用して、有料会員登録に至っていない顧客（約 100 名）に対して、登録確率を予測します。<br/>
本チュートリアルでは、事前に準備した、予測用のサンプルデータを利用します。
予測モデル作成(学習)用データとは違い、有料会員登録の項目は利用しません。

{{% tutorial_file_location "/ja-JP/doc/sample_dataset/use_case/マーケティング_有料会員登録予測に基づく営業施策の決定" %}}
{{% /div_slide %}}

{{% div_slide "ステップ3" normal %}}
![](../img/t_slide22.png)

予測用データである`3_有料会員登録情報（予測用）.csv`を指定してください。<br/>
{{% desktop_only %}}
データはウィンドウへのドラッグ&ドロップか 「ファイルを指定する」で読み込むことができます。<br/>
{{% /desktop_only %}}
{{% cloud_only %}}
サンプルデータは、「アップロード済みのデータから選択」をクリックし、「サンプル」タブのデータ一覧から選択してください。
{{% /cloud_only %}}

{{% tutorial_file_location "/ja-JP/doc/sample_dataset/use_case/マーケティング_有料会員登録予測に基づく営業施策の決定" %}}
{{% /div_slide %}}

{{% div_slide "ステップ4" normal %}}
![](../img/t_slide23.png)

続いて、関連データを指定します。
本チュートリアルの関連データには予測対象の顧客に関する関連情報も含まれているので、
「モデル作成時のデータを再利用」ボタンをクリックしてください。<br/>
関連データが追加され、予測用データと関連付けられました。

![](../img/t_slide24.png)

「次へ」をクリックしてください。

{{% /div_slide %}}

{{% div_slide "ステップ5" normal %}}
![](../img/t_slide25.png)
結合後の予測用データのプレビューが表示されます。
「年齢」「会社規模」などの情報から「？」と表示されている「有料会員登録（予測対象）」を予測します。

{{% desktop_only %}}
「予測結果プレビュー」をクリックしてください。
{{% /desktop_only %}}
{{% cloud_only %}}
「予測を実行」をクリックしてください。予測結果のプレビュー画面が表示されるまで、しばらくお待ちください。
{{% /cloud_only %}}
{{% /div_slide %}}

{{% div_slide "ステップ6" normal %}}
![](../img/t_slide26.png)

{{% desktop_only %}}
「以下の項目を左端に追加する」にて「顧客ID」を指定してください。

「予測して保存」をクリックしてください。
各行ごとに予測を行い、その結果を保存します。

「予測して保存」をクリックした後、名前を付けて保存するダイアログが表示されます。
ファイル名を指定して予測結果を保存してください。
{{% /desktop_only %}}
{{% cloud_only %}}
「以下の項目を左端に追加する」にて「顧客ID」を指定してください。
「予測結果を保存」をクリックし、「ファイル名」を入力し、「保存」をクリックしてください。
{{% /cloud_only %}}
{{% /div_slide %}}

{{% div_slide "ステップ7" normal %}}
予測が完了すると以下の画面が表示され、指定したファイルに予測結果が保存されています。

![](../img/t_slide27.png)

予測結果は以下のような形式で出力されます（オプション設定によっては違う形式になります）。
各顧客に対して、有料会員登録の予測確率が算出されています。

![](../img/t_slide28.png)
{{% /div_slide %}}