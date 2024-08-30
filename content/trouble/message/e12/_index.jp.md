---
title: "ダウンロードに失敗しました。ネットワーク接続に問題があります。"
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
  is_desktop_only: true
  hide_on_dist_type: ["RDC"]
# 検索でヒットする文字列の指定
keywords: ["接続できない", "アップデート"]
keywordsForRDC: [""]
---

{{% dist_type_only "SNC" %}}

{{% h4_error_cause %}}
ネットワークに接続していない・プロキシ環境下にある場合など、何等かの理由でダウンロードが完了しなかった場合、このメッセージが表示されます。

{{% h4_error_avoid %}}
ネットワークの接続をご確認ください。
また、プロキシ環境下の場合は以下のページもご参照ください。

{{% a_in "../../start_application/update_proxy/" "プロキシ環境下でアップデートを確認する/アップデートの通知を受けるには、どのように設定すればよいのか？" %}}

{{% /dist_type_only %}}
