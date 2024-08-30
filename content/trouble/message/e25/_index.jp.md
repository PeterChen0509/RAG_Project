---
title: "同じ名前の項目が複数あるため、データを読み込めません"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 100
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["同じ名前", "重複"]
---

{{% h4_error_cause %}}
予測モデル作成(学習)用データに含まれる項目はすべて異なる名前である必要があります。

{{% h4_error_avoid %}}
予測モデル作成(学習)用データ・評価用データに含まれる項目に重複が無いように編集してください。
項目名が空白の列が複数存在する場合にもこのエラーが表示されます。その場合、空白の列にそれぞれ別の名前を付けるか、空白の列を削除してください。