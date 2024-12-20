---
title: "予測したい項目の外れ値を確認しましょう"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4
draft: false
# metaタグのパラメータ
meta:
  description: "予測分析ツールPrediction Oneが提案する精度改善のための改善ヒントについて説明するページです。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  ["ヒント","改善ヒント","tips","精度改善","外れ値"]
toc: true
---

### 説明

予測したい項目に、他とは大きく異なる外れ値があった場合、外れ値を含む行を除外して問題ないか検討しましょう。
業務で活用する際に、外れ値を含む行を除外しても問題がないのであれば、除外して予測モデルを再作成することで、精度改善が期待できます。

※アプリ内のN行目の表示は先頭の項目名の行を含めずにカウントした行数です。Excelで該当の行を確認する際は先頭の項目名も含めたN+1行目を確認してください。

![](../img/t_slide.png)

