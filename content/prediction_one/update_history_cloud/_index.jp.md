---
title: "ソフトウェア更新履歴（クラウド版）"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1000 # 一番下に表示する
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: true
  is_desktop_only: false
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

### version 1.13 (2024/07)

- {{% a_in "../../operating_instruction/manual/manual/" "チュートリアル" %}} を業務タイプや予測タイプごとに参照できるようになりました。  
- マニュアルの {{% a_in "../../trouble/message/" "各メッセージの詳細と対応方法" %}} への記載を拡充しました。

### version 1.12 (2024/04)

- {{% a_in "../../tips/new_features/create_slide/" "説明資料生成機能" %}}で生成される資料を拡充しました。
- {{% a_in "../../operating_instruction/manual/manual/" "チュートリアル" %}}を追加/整理しました。
- {{% a_in "../../operating_instruction/setting/setting_cloud/" "初回起動時に利用に役立つ情報" %}}が表示されるようになりました。(設定の「初回説明を再表示」の再表示をクリックし再度アプリを起動すると表示されます)
- {{% a_in "../../tips/new_features/data_connector/" "データコネクタ機能" %}}がGoole Cloud Platform(GCP)に対応しました。
- {{% a_in "../../operating_instruction/api/" "API" %}}を拡充しました。

### version 1.11 (2024/01)

- {{% a_in "../../operating_instruction/create_slide/" "説明資料生成機能" %}}を追加しました。
- 「{{% a_in "../../operating_instruction/result/importance/" "寄与度の読み解き方をガイド形式で学ぶ" %}}」ための機能を追加しました。
- {{% a_in "../../operating_instruction/manual/manual/" "チュートリアル" %}}の構成をよりわかりやすく見直しました。​
- ユーザーマニュアルが{{% a_in "../../operating_instruction/help/" "ヘルプボタン" %}}からアクセスできるようになりました。​
- {{% a_in "../../operating_instruction/result/mainresult/" "評価結果画面" %}}のタブの名称や構成を改善しました。
- UI や操作性の改善を行いました。

### version 1.10 (2023/10)

- {{% a_in "../../operating_instruction/result/advice/" "ヒント機能" %}}で表示されるヒントを拡充しました。
- {{% a_in "../../operating_instruction/result/mainresult/" "サマリ画面" %}}と{{% a_in "../../operating_instruction/result/importance/" "寄与度画面" %}}のUIを改善しました。
- UI や操作性の改善を行いました。

### version 1.9 (2023/07)

- {{% a_in "../../tips/new_features/data_connector/" "データコネクタ機能" %}}を追加しました
- {{% a_in "../../operating_instruction/train_api/" "学習API" %}}を追加しました
- 時系列予測に{{% a_in "../../tips/new_features/prediction_interval/" "上振れ下振れ予測" %}}を追加しました
- 時系列予測の最大同時学習系列数を20系列から200系列に緩和しました
- 項目の条件で評価用データを指定する機能を追加しました

### version 1.8 (2023/03)

- {{% a_in "../../tips/new_features/quick_guide/" "クイックガイド" %}}を追加しました
- {{% a_in "../../tips/new_features/timeseries_features/" "時系列予測にて、予測したい項目以外の項目" %}}をどのように予測に使うか指定できるようになりました
- 予測モデル作成画面にて、{{% a_in "../../tips/new_features/score/" "関連度" %}}が表示されるようになりました
- エラーメッセージ表示画面からマニュアルを開くことができるようになりました
- {{% a_in "../../tips/specification/custom/" "データ準備機能" %}}にて以下の加工方法を追加しました
  - 時系列予測用データの変換：特定フォーマットのファイルについて、時系列予測を実行できる形式に変換します
  - 数値をビンに分割：数値を指定した数の区間に分割します
  - 相関の低い項目を削除：相関係数をもとに項目を削除します

### version 1.7 (2022/12)

- {{% a_in "../../tips/new_features/dataprep_custom/" "データ準備機能" %}}を追加しました
- {{% a_in "../../tips/new_features/help/" "アプリ内ヘルプ機能" %}}、{{% a_in "../../tips/new_features/advice/" "ヒント機能" %}}を追加しました

### version 1.6 (2022/08)

- 次の機能を追加しました：交差検証の分割数指定、二値分類の評価・予測時の予測確率に対する閾値設定、評価用データのエクスポート、多値分類の分類数上限を200に変更、時系列予測モードの寄与度表示

### version 1.5 (2022/03)

- モデル監視機能を追加しました
- API管理タブ・使用状況ダイアログのデザインをアップデートしました

### version 1.4 (2021/12)

- API作成済モデルの再学習APIを追加しました
- デスクトップ版からのモデルインポート機能を追加しました

### version 1.3 (2021/09)

- 予測API及びAPI作成機能を追加しました

### version 1.2 (2021/05)

- 初回リリースを行いました
