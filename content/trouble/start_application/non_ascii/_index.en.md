---
title: "I get a [The temporary folder path contains non-ASCII characters (Kanji, hiragana, katakana, etc.), which can cause problems with the prediction model creation process. Change the temporary folder and restart Prediction One.]error during startup, but how can I change the temporary folder?"
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
keywords: ["working folder", "ASCII", "kanji", "hiragana", "katakana"]
---

Prediction One can cause problems with the prediction model creation process if the temporary folder path contains non-ASCII characters (Kanji, hiragana, katakana, etc.). Follow the procedure below to change the temporary folder.

{{% step_n 1 "Launch the Edit Environment Variables window" %}}

On the Windows Start menu, search for "environment variable", and then click "Editing Environment Variables".
![Editing Environment Variables](../../img_en/t_slide18.png)

{{% step_n 2 "Add New Environment Variable" %}}

Click "New" for the user environment variable.

![Add New Environment Variable](../../img_en/t_slide19.png)

{{% step_n 3 "Set environment variable "TEMP_PREDICTION_ONE"" %}}

In the new user variable, name the variable "TEMP_PREDICTION_ONE" and specify the path to the new temporary folder as the variable value.
Specify a location where the temporary folder path consists of only ASCII characters, such as single-byte alphanumeric characters, and has write permissions.
Click "OK" after specifying.
![Setting Environment Variables](../../img_en/t_slide20.png)

The following is an example of the display after the setting. Click "OK".
![Example of display after setting](../../img_en/t_slide21.png)

After setting, restart Prediction One.
