---
title: "プロキシ環境下でアップデートを確認する/アップデートの通知を受けるには、どのように設定すればいいですか？"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 1
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
keywords: [""]
---

{{% dist_type_only "SNC" %}}

Internet Explorer のプロキシ設定、もしくは環境変数が設定されている必要があります。
環境変数に設定する場合は、`HTTP_PROXY` と `HTTPS_PROXY` に以下を設定してください。

> http://{username}:{password}@{proxy.server}:{port}

※( {username}:{password}@ は省略可能 )

{{% /dist_type_only %}}
