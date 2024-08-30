---
title: "Data Join Screen"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 5
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

Clicking the Data Join button from the Model Settings screen will take you to this screen.
Use this screen to add additional data files related with the training data you have entered.

![](../../img_en/t_slide59.png)

{{% div_method_area "Add related data" %}}
{{% step_n_area2 1 "Drag and drop the file into the central data area." %}}
You can specify a file by dragging and dropping it into an area in the center window. Alternatively, you can click the Add Related Data button and specify it from the File Browser. The file formats are CSV (comma separated values) and TSV (tab separated values).
If there are multiple related data files, they can be added together by drag and drop.
{{% /step_n_area2 %}}
{{% step_n_area2 2 "Check the join relation of the added data" %}}
![](../../img_en/t_slide60.png)

Depending on the format of the added file, the join relation to the training data is displayed.

- Vertical Join - If the variable group matches the training data exactly, it is displayed below the training data.
- Horizontal Join - When training data and related data are associated through a join key variable, they appear to the right of the training data.

Refer to Tips "{{% a_in "../../../tips/join_dataset/" "Model creation method using data join"%}}" for a detailed explanation of the join relation.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Review Tips for Data Join" %}}
{{% step_n2 1 "Click [What is Data Join?]." %}}
{{% /div_method_area %}}

{{% div_method_area "Change the join key variable for related data" %}}
{{% step_n2 1 "Click [Change Join Key Variable Pull-down]." %}}

![](../../img_en/t_slide61.png)

{{% step_n_area2 2 "Click the new variable in the list of possible join keys." %}}
![](../../img_en/t_slide62.png)
If the join keys are likely to be unmatched, a "warning icon: Check Variable" appears.
It is recommended that you verify the join key variables are correct. You can ignore the warning and go straight to learning.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

![](../../img_en/t_slide63.png)

{{% div_method_area "Delete related data" %}}
{{% step_n2 1 "Click the Delete File button." %}}
{{% /div_method_area %}}

{{% div_method_area "Check joined data in tabular format" %}}
{{% step_n2 1 "Click the [Tabular Format] button." %}}
{{% step_n_area2 2 "In the Preview Joined Data screen, check the joined table format." %}}

- Displays the name of the joined data variables and the file name of the source file.
  Displays the training data variables entered in the training data input screen and additional variables generated from related data.
- Some of the additional variables displayed in the Preview Joined Data screen are actually used for learning.
  This is because additional variables with too many uniqueness values are excluded from the training data after the joined data is created.

![](../../img_en/t_slide64.png)

{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Review additional variables by data join" %}}
{{% step_n_area2 1 "Click the [Check Additional Variables] button." %}}
This button appears when there is more than one join key variable for training data in the join key variable value of the related data being horizontally joined.

- Some of the additional variables displayed in the dialog are actually used for learning.
  This is because additional variables with too many uniqueness values are excluded from the training data after the joined data is created.
  {{% /step_n_area2 %}}
  {{% /div_method_area %}}
