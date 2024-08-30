---
title: "Model List Screen"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
# 重要ではないので一番下に
weight: 10
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  [
    "Model List",
    "List of models",
    "Copy to create a new prediction model",
    "Output prediction results for evaluation data",
    "Export",
    "Import",
    "Export prediction model",
    "Import prediction model",
  ]
---

When Prediction One is started and multiple models have already been created, a list of model folders appears on the left.

![](../../img_en/t_slide48.png)
![](../../img_en/t_slide49.png)

{{% div_method_area "Create a new model" %}}
{{% step_n2 1 "Click the [Create a New Model] button." %}}
{{% /div_method_area %}}

{{% cloud_only %}}
{{% div_method_area "Sharing Models" %}}
Click the Model pull-down of the source model and click [Share]. It is copied to the shared space so that users of the same tenant can view and predict model details.
{{% /div_method_area %}}

{{% div_method_area "Review and use shared models" %}}
Click the [Share] tab in the Model List. Switches to the shared model list.
{{% /div_method_area %}}
{{% /cloud_only %}}

{{% div_method_area "Adding Models to Favorites" %}}
{{% step_n_area2 1 "Click the [Add to Favorites] button." %}}
Models added to favorites are displayed at the top of the model list.
You can click the [Add to Favorites] button again to remove a model from the favorites.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% desktop_only %}}
{{% div_method_area "import prediction model" %}}
{{% step_n2 1 "Click the [Create New Folder] button." %}}
{{% step_n2 2 "Click ‘Import the prediction model’." %}}
{{% step_n2 3 "Specify a model (ZIP file) exported in Prediction One." %}}
{{% /div_method_area %}}
{{% /desktop_only %}}

{{% div_method_area "Create a New Folder" %}}
{{% step_n2 1 Click "Create a new folder." %}}
{{% /div_method_area %}}

{{% div_method_area "Delete a folder" %}}
{{% step_n2 1 "Click the folder pull-down." %}}
{{% step_n_area2 2 "Click [Delete Folder]." %}}
<u>When you delete a folder, all models within the folder are deleted.</u>
This operation cannot be undone.
{{% /step_n_area2 %}}
{{% /div_method_area %}}

{{% div_method_area "Rename a folder" %}}
{{% step_n2 1 "Click a folder name and type a new folder name." %}}
{{% /div_method_area %}}

{{% div_method_area "Displaying Models Added to Favorites" %}}
{{% step_n2 1 "Click the [Display Favorites Only] button." %}}
{{% /div_method_area %}}

{{% div_method_area "Sorting the Model List" %}}
{{% step_n2 1 "Select a sort criteria indicator from the Model Sort drop-down." %}}
{{% /div_method_area %}}

{{% div_method_area "Operations for the model (for example, copy or delete)" %}}
![](../../img_en/t_slide50.png)

If you click the Model pull-down to the right of the model name, a menu similar to the one shown above appears.
From here, you can copy or delete the model.
{{% /div_method_area %}}

{{% div_method_area "To edit a created model and execute retraining" %}}
Click the Model pull-down of the source model and click [Copy and create a new model].
You can open the learning settings screen with the settings of the original model entered.
However, <u>this operation cannot be performed if the training data used to create the source model does not exist in the same location with the same file name.
Also, if you have changed the file contents of the training data after the creation of the original model, subsequent processing may not work correctly</u>.
{{% /div_method_area %}}

{{% desktop_only %}}
{{% a_id "output-result" %}}
{{% div_method_area "To output prediction results for evaluation data" %}}
Click the Model pull-down of the source model and click "Output Prediction Results for Evaluation Data".
You can output the evaluation data used to calculate various metrics on the [Accuracy Details] screen and the prediction results for it as a CSV file.

Normally, the data is output in the order of {prediction result column} → {evaluation data column}, but when the prediction model is created in the time series prediction mode, the data is output in the order of {forecast_before column} → {prediction result column} → {evaluation data column}.
(The {forecast_before column} indicates how far ahead you are evaluating the model. For example, if you evaluate a model that predicts 1, 4, 7, 9, and 12 months into the future, the {forecast_before column} will contain 1, 4, 7, 9, or 12.)
{{% /div_method_area %}}
{{% /desktop_only %}}


{{% desktop_only %}}
{{% div_method_area "To view prediction history" %}}
From the prediction history, you can check a list of file names for prediction data that you have predicted using this model in the past.
![](../../img_en/t_slide51.png)

You can also delete prediction history.
![](../../img_en/t_slide52.png)
Select the prediction data you want to delete and click Delete.
<u>This operation only deletes the history of the prediction data left in Prediction One, not the prediction data itself </u>.
{{% /div_method_area %}}
{{% /desktop_only %}}

{{% desktop_only %}}
{{% div_method_area "To export a prediction model" %}}
Click the Model pull-down of the source model and click [Export the prediction model].
You can save a prediction model and the files that the prediction file references (the data for prediction model creation (training), etc.) in a single ZIP file.
The exported model (ZIP file) can be copied to another PC and imported to migrate the model.
{{% /div_method_area %}}
{{% /desktop_only %}}


{{% div_method_area "To delete a model" %}}
{{% step_n2 1 "Click the model pull-down and click [Delete] from the menu that appears." %}}
{{% /div_method_area %}}

{{% div_method_area "To edit the model name and description of a model" %}}
{{% step_n2 1 "Click the model pull-down and click [Edit] from the menu that appears." %}}
{{% /div_method_area %}}

{{% div_method_area "Show or hide the model list" %}}
{{% step_n2 1 "Click the [Change Model List Display] button." %}}
{{% /div_method_area %}}
