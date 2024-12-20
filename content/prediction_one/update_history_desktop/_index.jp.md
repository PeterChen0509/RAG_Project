---
title: "ソフトウェア更新履歴（デスクトップ版）"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1000 # 一番下に表示する
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords:
  [
    "アップデート内容",
    "差分",
    "前回",
    "前回バージョン",
    "バージョン",
    "前との",
    "新機能",
    "追加",
    "update",
  ]
---

過去バージョンのマニュアル・ソフトウェアの更新履歴です。

{{% dist_type_only "SNC" %}}

{{% notice tip "../../operating_instruction/setting/feedback/index.html" "フィードバックの送信方法について" %}}
Prediction One の機能に関してお気に入りの点・ご不満点・改善のご提案などがございましたらフィードバック送信画面よりメッセージをお送りください。今後の製品開発に活用いたします。
{{% /notice %}}

{{% /dist_type_only %}}

### version 3.6 (2024/07)

- {{% a_in "../../operating_instruction/manual/manual/" "チュートリアル" %}} を業務タイプや予測タイプごとに参照できるようになりました。  
- マニュアルの {{% a_in "../../trouble/message/" "各メッセージの詳細と対応方法" %}} への記載を拡充しました。  

### version 3.5 (2024/04)

- {{% a_in "../../tips/new_features/create_slide/" "説明資料生成機能" %}}を追加しました。
- {{% a_in "../../operating_instruction/manual/manual/" "チュートリアル" %}}を追加/整理しました。
- {{% a_in "../../operating_instruction/setting/setting/" "初回起動時に利用に役立つ情報" %}}が表示されるようになりました。(設定の「初回説明を再表示」の再表示をクリックし再度アプリを起動すると表示されます)

### version 3.4 (2024/01)

- {{% a_in "../../operating_instruction/manual/manual/" "チュートリアル" %}}の構成をよりわかりやすく見直しました。
- ユーザーマニュアルが{{% a_in "../../operating_instruction/help/" "ヘルプボタン" %}}からアクセスできるようになりました。​
- {{% a_in "../../operating_instruction/result/mainresult/" "評価結果画面" %}}のタブの名称や構成を改善しました。
- UI や操作性の改善を行いました。

### version 3.3 (2023/10)

- {{% a_in "../../operating_instruction/result/advice/" "ヒント機能" %}}で表示されるヒントを拡充しました。
- {{% a_in "../../operating_instruction/result/mainresult/" "サマリ画面" %}}と{{% a_in "../../operating_instruction/result/importance/" "寄与度画面" %}}のUIを改善しました。
- 時系列予測に{{% a_in "../../tips/new_features/prediction_interval/" "上振れ下振れ予測" %}}を追加しました。
- 時系列予測の最大同時学習系列数を20系列から200系列に緩和しました。
- UI や操作性の改善を行いました。

### version 3.2 (2023/01)

- {{% a_in "../../tips/new_features/help/" "アプリ内ヘルプ機能" %}}を追加しました。
- {{% a_in "../../tips/new_features/advice/" "ヒント機能" %}}を追加しました。

### version 3.1 (2022/10)

- お気に入り機能を追加しました。
  - {{% a_in "../../operating_instruction/result/model_list/" "モデル一覧画面" %}}にてお気に入りボタンを押すと、そのモデルを上位に固定して表示します。
- {{% a_in "../../operating_instruction/result/importance/" "寄与度をCSVファイルに出力" %}}できるようになりました。
- {{% a_in "../../tips/specification/custom/" "データ準備機能" %}}にて加工方法を追加しました。
  - 文字列に「その他」を追加：出現回数の少ない文字列を置換します。
  - 文字列の一部を置換：文字列中の一部のみを置換します。
  - 類似した文字列を統一：類似した表記の文字列をひとつに統一します。
  - 文字列を分割：文字列を指定した記号・文字で分割します。
  - 項目を結合：ふたつの項目を連結してひとつの項目にします。
  - 相関の低い項目を削除：相関係数をもとに項目を削除します。
  - 条件にあてはまる行を削除：指定した条件の行を削除します。
  - 欠損が含まれる行を削除：欠損が含まれる行を削除します。
  - 重複した行を削除：重複している行を１つだけ残して削除します。
- 予測モデル作成画面にて、{{% a_in "../../tips/new_features/score/" "関連度" %}}が表示されるようになりました。
- {{% a_in "../../tips/new_features/timeseries_features/" "時系列予測にて、予測したい項目以外の項目" %}}をどのように予測に使うか指定できるようになりました。
- エラーメッセージ表示画面からマニュアルを開くことができるようになりました。
- UI や操作性の改善を行いました。  

### version 3.0 (2022/05)

- データ準備機能を追加しました。{{% a_in "../../tips/new_features/dataprep_custom/" "データ準備機能" %}}では、ユーザーがデータの加工方法を自由に組合わせることができます。  
- UIや操作性の改善を行いました。  

### version 2.3 (2021/11)

- 予測モデルの{{% a_in "../../operating_instruction/result/model_list/" "エクスポート/インポート" %}}ができるようになりました。
- {{% a_in "../../tips/new_features/model_update/" "モデルの更新" %}}機能により、最新データでモデルを更新して現在のモデルと比較ができるようになりました。
- 項目の条件で評価データを指定する機能を追加しました（指定した数値や日時の範囲による予測モデル作成(学習)用データと評価用データの分割）。
- 多値分類で最大200種類の分類ができるようになりました。（従来は最大20種類）
- 多値分類の評価結果の詳細で、{{% a_in "../../operating_instruction/result/details/" "多値分類の混同行列をCSV形式で保存する" %}}ことができるようになりました。
- メモリ使用量を削減しました。
- UI や操作性の改善を行いました。

### version 2.2 (2021/03)

- 複数のファイルに分かれた{{% a_in "../../tips/new_features/join_dataset/" "データを結合" %}}して予測モデルを作成することができるようになりました。
- {{% a_in "../..//operating_instruction/create_model/select_target_detail/" "予測したい項目の偏りを補正する" "imbalanced-data" %}}ことができるようになりました。
- 時系列モードにおいて寄与度を表示できるようになりました。
- UI や操作性の改善を行いました。

### version 2.1 (2020/11)

- 交差検証の分割数の指定ができるようになりました。
- {{% a_in "../../operating_instruction/result/model_list/" "評価用データに対する予測結果を出力" "output-result" %}}して、どのデータを評価に用いたかを確認できるようになりました。

### version 2.0 (2020/08)

- UI や操作性の改善のため、デザインを刷新しました。
- より簡単に予測モデルを作成することができるようになりました。
- 予測画面での出力の指定方法を改善しました。
- プロジェクト一覧表示がモデル・フォルダー一覧表示へと変更になりました。

### version 1.4 (2020/04)

- 時系列予測モードの改善（複数系列対応、評価結果グラフ追加）を行いました。
- 学習/予測時の残り時間表示の改善しました。
- 数値予測について、予測モデルの作成が高速になるような改善を行いました。
- UI や操作性の改善を行いました。

### version 1.3 (2020/01)

- 数値予測に時系列予測モードを追加しました。
- より多くのタイムスタンプのフォーマットに対応しました。{{% a_in "../../tips/specification/dataset_format/" "データセットのより詳細な仕様" "timestamp-format" %}}にて対応フォーマットをご確認いただけます。
- 数値予測・二値分類・多値分類の性能を向上させるための改善を行いました。
- UI や操作性の改善を行いました。

### version 1.2 (2019/09)

- 表示内容を画像で保存する機能を追加しました。
- チュートリアル/ヒントをプロジェクト一覧画面に追加しました。
- 多値分類の寄与度の構成/理由あり予測を追加しました。
- 日本語・英語のテキストの処理の改善を行いました。
- UI や操作性の改善を行いました。

### version 1.1 (2019/06)

- 初回リリースを行いました。
