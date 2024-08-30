---
title: "Why does character corruption occur even though the character code of the data file is Shift_JIS?"
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
keywords: ["Garbled text", "Shift-JIS"]
---

Prediction One reads the first 1,000 bytes of the file to determine the character code. Therefore, if there is no information that can determine the character code in the first 1,000 bytes, misjudgment may occur.
In this case, please convert the data file to UTF-8 (with BOM).
