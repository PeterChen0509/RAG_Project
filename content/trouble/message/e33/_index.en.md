---
title: "You cannot join files that have already been joined."
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
# 検索でヒットする文字列の指定
keywords: ["joined"]
---

{{% h4_error_cause %}}
This message is displayed when a file that has already been imported is imported again on the data join screen.
When joining data, you cannot join files that have already been joined.

{{% h4_error_avoid %}}
If you plan to use vertical joins to create more data for your model, write the data you want to add to a separate file, and then join it vertically.
You cannot join multiple files that are the same as files that have already been imported.
