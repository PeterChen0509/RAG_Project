---
title: "Are empty string and zeros treated the same for numeric variables?"
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
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Missing value"]
---

No, they are not treated the same.

Zero is treated as a value. The empty string is treated as special non-numeric information. If a non-empty string is used for a numeric variable, the variable may be judged as string type.
