---
title: "I got a [The working folder and temporary folder are not the same drive and cannot be started] error during startup, how can I start it?"
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
keywords: ["working folder"]
---

Prediction One cannot be started unless the working folder (current directory) and temporary folder are on the same drive. Depending on your environment, you may need to change the working folder.

{{% step_n 1 "Check the path of the temporary folder" %}}

Start a command prompt, type  `echo %Temp%` , and press Enter to display the temporary folder path. The following is an example of the display.

> D:\Users\PreOneUser\AppData\Local\Temp

{{% step_n 2 "Change the working folder for a shortcut" %}}

Right-click the Prediction One shortcut and click "Properties".
Enter the path of the temporary folder confirmed in (1) in the column of the working folder, then click "OK". The following is an example of a change.

![an example of a change](../../img_en/t_slide4.png)
