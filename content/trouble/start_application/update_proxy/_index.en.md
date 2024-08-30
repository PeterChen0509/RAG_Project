---
title: "How do I check for and receive updates in a proxy environment?"
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
# 検索でヒットする文字列の指定
keywords: [""]
---

Internet Explorer proxy settings or environment variables must be set.
To set environment variables, set the following in `HTTP_PROXY` and `HTTPS_PROXY`.

> http://{username}:{password}@{proxy.server}:{port}

※({username}:{password}@ is optional)
