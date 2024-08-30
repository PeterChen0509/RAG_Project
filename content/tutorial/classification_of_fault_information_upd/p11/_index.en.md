---
title: "Prediction"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 11
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
tutorial_page:
  is_next_exists: true
---

{{% div_slide "Step 1" normal first-page %}}
![](../img_en/t_slide27.png)

Select the prediction dataset on this screen. Input the prediction data from the folder of this tutorial by dragging and dropping it.
{{% tutorial_file_location_en "/en-US/doc/sample_dataset/use_case/Information management_Automatic classification of the latest failure information" %}}
{{% /div_slide %}}

{{% div_slide "Step 2" normal %}}
![](../img_en/t_slide28.png)

The content of the prediction file input in step 1 is similar to that shown above.
Prediction type, which is the correct data used as the prediction target this time, is not required.
But information on failure, which was the variable used for training, must be specified.

{{% /div_slide %}}

{{% div_slide "Step 3" normal %}}
![](../img_en/t_slide16.png)

The failure type is predicted for failure information that has not yet been classified using the prediction model created.

{{% /div_slide %}}


{{% div_slide "Step 4" normal %}}
![](../img_en/t_slide17.png)

On the prediction results preview screen, you can specify several options for the prediction file to output.
For example, if you select [Add prediction results of previous model], the prediction results file that is output
will include the prediction values of the previous model, in addition to those for the current model.

You can also select the [Add prediction reasons] option to output the prediction reason for both the current model and previous model.

{{% /div_slide %}}

{{% div_slide "Step 5" normal %}}
![](../img_en/t_slide36.png)

By classifying the failure type with the highest probability from the predicted probability for all failure information, the failure type can be classified automatically.
A particular feature of the current model is that it has performed prediction based on the information of failures that have occurred recently.

By taking a look at the output file, we can see that the prediction type differs for ID10003 between the current model and previous model.
The above figure only includes the prediction probabilities for "Other" and "Display", but the actual file will include the various prediction probabilities and prediction reasons for both the current model and previous model.

Checking the changes in trends and prediction results in the actual data is important for using prediction results in actual business.

{{% /div_slide %}}


