---
title: "Text Handling"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4400
draft: false
# metaタグのパラメータ
meta:
  description: "For example, the data collected in the form of sentences such as the free description column of the questionnaire is called Text. Prediction One sets the data type to \"Text\" when it determines that the data is text."
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["Text", "Sentence", "Text mining", "String", "English"]
---

For example, the data collected in the form of sentences such as the free description column of the questionnaire is called **Text**. Prediction One sets the data type to "Text" when it determines that the data is text. Variables that have a data type of "Text Type" and are processed specifically for the Text data type.

### Text Handling in Prediction One

Prediction One can also use data containing Japanese and English sentences as training data.

For example, the "Post content" variable in the dataset used in the {{% a_in "../../tutorial/crm_automate_voice_of_the_customer_labeling/" "Automated labeling of customer feedback"%}} tutorial contains Japanese text. If the text contains verbs, nouns, adjectives, or other words related to the variable you want to predict, you can see them in the details of contribution.

![](../img_en/t_slide34.png)

{{% div_relitem contents-bottom %}}

- {{% a_in "../string/" "String Handling" %}}
  {{% /div_relitem %}}
