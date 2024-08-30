---
title: "TIPS・仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
description: "データセットの作り方や予測精度の概要などのTIPSや各機能の仕様についてまとめています"
type: "docs"
weight: 3
---

「TIPS」では、Prediction Oneを使用する上で役に立つ情報やヒントをまとめています。

## データセットの作り方
データセットの作成方法について。
- {{% a_in "./how_to_create_dataset/" "データセットの作り方" %}}

## 新機能の紹介
バージョンアップにて追加された機能について。

- {{% a_in "./new_features/contribution_csv/" "予測寄与度のcsv出力" %}}
- {{% a_in "./new_features/timeseries/" "時系列予測" %}}
 - {{% a_in "./new_features/timeseries_features/" "時系列予測モード：予測したい項目以外の項目" %}}
- {{% a_in "./new_features/join_dataset/" "データ結合" %}}
- {{% a_in "./new_features/model_update/" "モデルの更新" %}}
- {{% a_in "./new_features/model_monitor/" "モデルの監視" %}}
- {{% a_in "./new_features/dataprep_custom/" "データ準備機能" %}}
- {{% a_in "./new_features/score/" "関連度スコア" %}}
- {{% a_in "./new_features/advice/" "ヒント機能" %}}
- {{% a_in "./new_features/help/" "アプリ内ヘルプ機能" %}}
- {{% a_in "./new_features/quick_guide/" "クイックガイド" %}}
- {{% a_in "./new_features/prediction_interval/" "上振れ下振れ予測" %}}
- {{% a_in "./new_features/data_connector/" "データコネクタ機能" %}}
- {{% a_in "./new_features/create_slide/" "説明資料生成機能" %}}


## 予測精度と予測寄与度の概要と活用
予測精度と予測寄与度の概要と活用について。

- {{% a_in "./result/eval_bin/" "予測精度の概要 (二値分類)" %}}
- {{% a_in "./result/eval_mul/" "予測精度の概要 (多値分類)" %}}
- {{% a_in "./result/eval_reg/" "予測精度の概要 (数値予測)" %}}
- {{% a_in "./result/contribution/" "予測寄与度の概要" %}}
- {{% a_in "./result/contribution_bin/" "予測寄与度の読み解き方と活用方法 (二値分類)" %}}
- {{% a_in "./result/contribution_mul/" "予測寄与度の読み解き方と活用方法 (多値分類)" %}}
- {{% a_in "./result/contribution_timeseries/" "予測寄与度の読み解き方と活用方法 (時系列予測)" %}}
- {{% a_in "./result/improve_model/" "予測精度を上げるには" %}}
- {{% a_in "./result/use_result/" "予測結果の活用例" %}}
- {{% a_in "./result/use_business/" "作成したモデルを業務に導入するには" %}}

## ヒントの活用
精度改善のための各種ヒントについて。

- {{% a_in "./advice/" "ヒントの一覧" %}}

## 仕様の詳細
Prediction Oneの各機能の仕様について。

- {{% a_in "./specification/dataset_format/" "データセットのフォーマット" %}}
- {{% a_in "./specification/dataset_for_timeseries/" "時系列予測モード用のデータセット" %}}
- {{% a_in "./specification/custom/" "データ準備機能の各加工について" %}}
- {{% a_in "./specification/about_llm/" "LLM (大規模言語モデル) の利用について" %}}