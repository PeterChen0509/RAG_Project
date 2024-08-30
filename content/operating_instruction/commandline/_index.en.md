---
title: "Command Line Function"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
# 一般ユーザーは使用しないので下に表示
weight: 20
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords: ["Command Line", "Prompt", "bash", "cui", "Execution command"]
---

Prediction One is a GUI tool, but some functions can be performed without a GUI by using command line functions.

#### Learning (learn) Command Specifications


This command generates a prediction model from training data.

`PredictionOneCmd.exe learn [-md model_dir_path] [-od output_dir_path] [-lf learning_data_file_path] [-tc target_column_name] [-tt task_type] (-tv target_value) (-ef evaluation_data_file_path) (-ci column_info_file_path) (-cv cross_validation_k_fold) (-im imbalanced_data_flag) (-tsm time_series_forecast_model_flag) (-tsu time_series_forecast_time_unit) (-tsc time_series_forecast_time_column_name) (-tsi time_series_forecast_time_unit_interval) (- tsf time_series_forecast_from) (-tst time_series_forecast_to) (-tsa time_series_forecast_analysis_flag) (-tsin time_series_forecast_other_column_flag) (-tsine time_series_forecast_other_column_exception)`

<div class="command-line">

| Option Name | Option Description                                                                                                                                                                                                                                                                                                             |
| :----------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-md`     | Path of the model directory. When executed, a set of model files is generated.                                                                                                                                                                                                                                                           |
|    `-od`     | Path of the output directory. For a list of files output in the output directory, see "About Files Output to the Output Directory During Learning."                                                                                                                                                            |
|    `-lf`     | Input path for prediction model creation (training) data (CSV/TSV).                                                                                                                                                                                                                                                                                            |
|    `-tc`     | The name of the item used as the variable to be predicted (prediction target).                                                                                                                                                                                                                                                                     |
|    `-tt`     | The prediction type. Specify `binary_classification` for binary classification, `multi_classification` for multiclass classification, or `regression` for numerical prediction.                                                                                                                                                                                                    |
|    `-tv`     | The prediction value. Required if the prediction type specifies binary classification. Otherwise not specified.                                                                                                                                                                                                                                                       |
|    `-ef`     | Input path of evaluation data (CSV/TSV). If omitted, it is automatically extracted from the training data.                                                                                                                                                                                                                                                      |
|    `-er`     | Whether the prediction results files for the evaluation data are output to the output directory. Specify `true` to output or `false` to not output. Identical to `false` if omitted.                                                                                                                                                     |
|    `-ci`     | Input/output path of the variable information file (CSV). If omitted, it is automatically determined from the first 1,000 lines of training data. For the format of the variable information file, see the specification for the variable information generation command (the -ci description section).                                                                                                                                        |
|    `-cv`     |The division count for k division cross-validation. If `0` is specified, it will automatically determine, based on the training data, whether or not to perform cross-validation and the number of divisions. If `-1` is specified, cross-validation is always performed, but the division count is automatically determined based on the training data. If `1` is specified, cross-validation is not performed. If `2` or more is specified, k division cross-validation is performed with the specified number k. If omitted, the operation is the same as if `0` was specified. |
|    `-im`     | Whether to rebalance value bias in the variable to be predicted. Can only be set when Prediction Type is Classification. Specify `true` to rebalance, or `false` to not rebalance. Identical to `false` if omitted.                                                                                                                                                           |
|    `-tsm`    | Whether to use the time series prediction mode. Specify `true` to use the time series prediction mode, or `false` to not use the time series prediction mode. Identical to `false` if omitted. The time series prediction mode can only be used when the prediction type (-tt) is set to numerical prediction (regression).                                                                                          |
|    `-tsu`    |The time unit for time series prediction. Specify `year` for the year, `month` for the month, `day` for the day, `hour` for the hour, `minute` for the minute, or `eom` for the last day of the month. To automatically determine the unit, do not specify this option (`-tsu`).                                                                                                                                  |
|    `-tsc`    | The time information variable of the variable to predict (prediction target) for time series prediction. Required if using time series prediction mode (-tsm true).                                                                                                                                                                                                                  |
|    `-tsi`    |The time interval for time series prediction. Specify an integer. The time unit specified by -tsu is used. For example, for a 2-month interval, specify `-tsu month -tsi 2`. To automatically determine the interval, do not specify this option (-tsi), or specify `0`.                                                                                                                   |
|    `-tsf`    | The start of the prediction period for time series prediction. Required if using time series prediction mode (-tsm true). Specify an integer of 1 or greater. The time unit specified by -tsu is used. For example, to specify from two months ahead to four months ahead as the prediction period, specify `-tsu month -tsf 2 -tst 4`.                                                                           |
|    `-tst`    | The end of the prediction period for time series prediction. Required if using time series prediction mode (-tsm true). Specifies an integer greater than or equal to the value specified by -tsf. The time unit specified by -tsu is used. For example, to specify from two months ahead to four months ahead as the prediction period, specify `-tsu month -tsf 2 -tst 4`.                                                            |
|    `-tss`    | The time series variable for time series prediction. Only specify this when there is a time series variable.                                                                                                                                                                                                                                                                       |
|    `-tsa`    | Whether a contribution analysis is performed for a time series prediction. Specify true to perform contribution analysis; otherwise, specify false. Identical to true if omitted.                                                                                                                                                                                    |
|    `-tsin`   | Whether the prediction period for time series prediction obtains variables other than the variable to be predicted. Specify `true` to obtain all variables or `false` to not obtain all variables. Identical to `false` if omitted. If there are both variables to obtain and variables to not obtain, specify exceptions using the `-tsine` option indicated below.<br/>(To perform the same training as version 3.0 or earlier, specify `true`. For details, see "{{% a_in "../../tips/new_features/timeseries_features/" "Variables other than the variable to be predicted" %}}".)                                                                                                                                                                                   |
|    `-tsine`   | Specifies exceptions for whether to obtain variables other than the variable to be predicted, in the prediction period for time series prediction. When `true` is specified for the `-tsin` option, specifies variables to not obtain values for. When `false` is specified for the `-tsin` option, specifies variables to obtain values for. To specify multiple variables, use the -tsine option multiple times (like `-tsine {variable name 1} -tsine {variable name 2}`).                                                                                                                                                                                    |

</div>


{{< notice warning >}}
[Notes on creating a prediction model in time series prediction mode]<br/>
For users who have been using Prediction One since before version 3.0 (May 2022):
The specifications have been changed such that you will need to change `-tsin` to `true` to continue creating prediction models as before.<br/>
Please be aware of this if you wish to create a prediction model in the same way as before. For details of the specifications, see {{% a_in "../../tips/new_features/timeseries_features/" "Variables other than the variable to be predicted" %}}.
{{</ notice >}}

##### About Files Output to the Output Directory During Learning

- `metrics.csv`: Evaluation results for evaluation data. Evaluation metrics name and evaluation value.
- `analysis_summary.csv``: The contribution of the variable to the evaluation data.
- `evaluation_raw_data.csv`: Prediction results for evaluation.

##### Example of command execution

**Command Examples (Binary Classification)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" learn -md %Temp%\model -od %Temp%\output -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\binary_classification_failure prediction.csv" -tc State (prediction target) -tt binary_classification -tv failure

**Command Example (Regression: Time Series Prediction Mode)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe"  learn -md %Temp%\model_ts -od %Temp%\output_ts -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\regression_demand_prediction.csv" -tc Number of Shipments (prediction target) -tt regression -tsm true -tsc Date -tsf 1 -tst 180

#### Predict (predict) Command Specifications

A command that applies a prediction model to prediction data and generates prediction results.

`PredictionOneCmd.exe predict [-md model_dir_path] [-od output_dir_path] [-pf prediction_data_file_path] (-ar add_reason_flag) (-ad add_prediction_data_flag) (-nc no_classification_result_flag) (-nr no_row_number_flag) (-th threshold_for_classification_result)`

<div class="command-line">

| Option Name | Option Description                                                                                                                                                                                                                                                                                                                                          |
| :----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-md`     | Path of the model directory. The directory containing the set of model files generated by the learn command must be specified.                                                                                                                                                                                                                                                |
|    `-od`     | Path of the output directory. For the contents of the following files in the directory, see "About Files Output to the Output Directory During Prediction."                                                                                                                                                                                         |
|    `-pf`     | Path of prediction data (CSV/TSV). In the time series prediction mode of regression, this option (-pf) can be omitted if variables other than the variable to be predicted (prediction target) variable, time information variable and series variable are not used for learning. In this case, the prediction data is automatically generated and the prediction is output for all periods and series for which prediction can be performed.                                                                            |
|    `-ar`     | Whether to calculate the reason for the prediction (output prediction_analysis.csv). Specify `true` if a prediction reason is required. Specify `false` to reduce the processing time without requiring a prediction reason. Identical to `true` if omitted.                                                                                                                                                       |
|    `-ad`     | Whether to add prediction data to the output. Specify `true` to add it. Identical to `false` if omitted.                                                                                                                                                                                                                                                       |
|    `-nc`     | Whether to output the classification results (in addition to the predicted probabilities) during binary and multiclass classification. Specify `true` if the classification result is not required. `false` if classification results are required. Identical to `true` if omitted.                                                                                                                                                                               |
|    `-nr`     | Whether to output row numbers in the prediction results. Specify `true` if the line number is not required. If line numbers are required, specify `false`. Identical to `false` if omitted.                                                                                                                                                                                                            |
|    `-th`     | Specifies the threshold value for the classification results output when `-nc false` is specified for a binary classification prediction. If a threshold is specified with `-th`, the predicted probabilities output by the prediction model are compared to the specified threshold, and whether or not the threshold is exceeded is output as the classification result. If `-1.0` is specified as the threshold value, the threshold value that maximizes accuracy in the evaluation data is used to output the classification result. |

</div>

##### About Files Output to the Output Directory During Prediction

- `prediction_valid.csv`: The row number of the successfully predicted row and the predicted result.
- `prediction_analysis.csv`: The row number of the successfully predicted row and the predicted result and the prediction reason.
- `prediction_skip.csv`: Row number of the row for which the prediction was skipped. (for example, different number of columns)
- `prediction_invalid.csv`: Row number of the row for which the prediction failed. (for example, model inconsistency)

##### Example of command execution

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe"  predict -md %Temp%\model -od %Temp%\output -pf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\binary_classification_failure prediction(for prediction).csv"

#### Variable Information Generation (mkcolinfo) Command Specifications

This command automatically generates a variable information file to be used during learning. You do not need to execute this 
when generating the variable information file yourself.

`PredictionOneCmd.exe mkcolinfo [-lf learning_data_file_path] [-ci column_info_output_file_path] (-tc target_column_name)`

<div class="command-line">

| Option Name | Option Description                                                                                                                                                                                                                           |
| :----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-lf`     | Input path for prediction model creation (training) data (CSV/TSV).                                                                                                                                                                                                          |
|    `-ci`     | Output path of the variable information file (CSV).                                                                                                                                                                                                          |
|    `-tc`     | The name of the item used as the variable to be predicted (prediction target). If it is omitted, only the result of the judgment of the variable type (integer/float/string/text/date) is output. If specified, in addition to judgments of the variable type, results of judgments will also be output for variables that are not used (ignore). |

</div>

**Example of command execution**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" mkcolinfo -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\binary_classification_failure prediction.csv" -ci %Temp%\column_info.csv -tc State (prediction target)

#### Model Update Learning (mu_learn) Command Specifications

Updates the previously trained model to create an up-to-date model.
Input a previously trained model, the latest data for creating (training) a prediction model, and evaluation data
to generate an accuracy comparison with the up-to-date trained model. 

`PredictionOneCmd.exe mu_learn 
[-md model_dir_path]
[-od output_dir_path]
[-lf learning_data_file_path] 
[-ef_type evaluation_type]
(-ef evaluation_data_file_path)
(-ef_auto_col column_name_for_data_split) 
(-ef_auto_thres threshold_for_data_split)
(-ef_auto_thres_dt datetime_threshold_for_data_split) 
(-ef_auto_op operator_string_for_data_split)
(-olm old_model_file_path)
(-olf old_learning_data_file_path)
(-oef old_evaluation_data_file_path)
(-omd old_model_dir_path)
(-use_olf use_old_learning_file)
(-use_oef use_old_evaluation_file)
(-er save_evaluation_results)
(-rf_out save_result_files)
(-ci column_info_file_path)
(-pk primary_key)
` 

<div class="command-line">

| Option Name | Option Description                                                                                                                                                                                                                                                                                                             |
| :----------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-md`     | Path of the model directory. When executed, a set of model files is generated.                                                                                                                                                                                                                                                           |
|    `-od`     | Path of the output directory. For a list of files output in the output directory, see "About Files Output to the Output Directory During Model Update (mu_learn)."                                                                                                                                                            |
|    `-lf`     | Input path of data (CSV/TSV) for up-to-date prediction model creation (learning).                                                                                                                                                                                                                                                                                            |
|    `-ef_type`     | A method for specifying evaluation data. Use `file` to specify a file, or `column_range` to specify by variable condition.                                                                                                                                                                                                                                                                                            |
|    `-ef`     | (optional) Evaluation data for comparing the previous and current models. If the data for evaluation is eval.csv, specify -ef_type file -ef eval.csv. Required when ef_type is a file.                                                                                                                                                                                                                                                                                            |
|    `-ef_auto_col`     | (optional) The name of the variable used as a criterion when using a variable to specify conditions for the evaluation data. When using the variable "Customer ID" to split data for creating (training) a prediction model and evaluation data, specify -ef_auto_col Customer_ID. Use when ef_type is a column_range.                                                                                                                                                                                                                                                                                            |
|    `-ef_auto_thres`     | (optional) The numerical threshold value to be used as a criterion when using a variable to specify conditions for the evaluation data. This is used when the variable is a numeric value. For example, when using data with a "Customer ID" of 10000 or higher as the evaluation data, specify -ef_auto_thres 10000. Use when ef_type is a column_range.                                                                                                                                                                                                                                                                                            |
|    `-ef_auto_thres_dt`     | (optional) The date string threshold value to be used as a criterion when specifying conditions for the evaluation data with a variable. This is used when the variable is a date string. For example, when using data with an "Entry Date" of 25 August 2018 or later as the evaluation data, specify -ef_auto_thres_dt 2018/08/25. Use when ef_type is a column_range.                                                                                                                                                                                                                                                                                            |
|    `-ef_auto_op`     | (optional) Criteria for specifying a range when using a variable to specify conditions for the evaluation data. Specify `GT` for "greater than", `LT` for "less than", `GE` for "greater than or equal to", and `LE` for "less than or equal to". For example, when using data with an "Entry Date" of 25 August 2018 or later as the evaluation data, specify -ef_type column_range -ef_auto_col Entry Date -ef_auto_thres_dt 2018/08/25 -ef_auto_op GE. Use when ef_type is a column_range. Identical to `GE` if omitted.                                                                                                                                                                                                                                                                                         |
|    `-olm`     | (optional) Path of the previous trained model. Required if not using -omd.                                                                                                                                                                                                                                                                                            |
|    `-olf`     | (optional) Path of the data used to create (train) the previous trained prediction model. If including the data used to create (train) the previous prediction model (-use_olf, described below, is `true`), or if using a variable to specify conditions for the evaluation data, supplying this argument allows a warning to be displayed when the previous model is using information from the evaluation data for training.                                                                                                                                                                                                                                                                                            |
|    `-oef`     | (optional) Path of the evaluation data of the previous trained prediction model. Specify to include the previous evaluation data in the current training (-use_oef, described below, is `true`).                                                                                                                                                                                                                                                                                            |
|    `-omd`     | (optional) Path of the directory of the previous trained model. Assumes input of the model directory from training performed in the GUI version. Compares the specified model with a model created using the most recent data. Required if -olm -olf -oef is not used.                                                                                                                                                                                                                                                                                             |
|    `-use_olf`     | (optional) Whether the data for creating (training) the previous prediction model should be combined with the data for creating (training) the current prediction model. Specify `true` to use or `false` to not use. Identical to `false` if omitted.                                                                                                                                                                                                                                                                                            |
|    `-use_oef`     | (optional) Whether the previous evaluation data should be combined with the data for creating (training) the current prediction model. Specify `true` to use or `false` to not use. Identical to `false` if omitted.                                                                                                                                                                                                                                                                                            |
|    `-er`     | (optional) Used to save prediction results for evaluation data. Specify `true` to save or `false` to not save. Identical to `false` if omitted.                                                                                                                                                                                                                                                                                            |
|    `-rf_out`     | (optional) Whether to output the input data for the learning process. Specify `true` to output; otherwise, specify `false`. Identical to `false` if omitted.                                                                                                                                                                                                                                                                                            |
|    `-ci`     | (optional) Variable information file. Used to specify the settings of the variables to be used for training.                                                                                                                                                                                                                                                                                            |
|    `-pk`     | (optional) Variable to be specified as the primary key. When -olf is specified and -use_olf is `true`, or when `-oef` is specified, rows where the specified variable name overlaps with the previous data are removed from the data used to create (train) the current prediction model.                                                                                                                                                                                                                                                                                            |

</div>

##### About Files Output to the Output Directory During Model Update (mu_learn)

- `analysis_summary.csv`: The contribution of the variable to the evaluation data for the current model.
- `analysis_summary_previous_model.csv`: The contribution of the variable to the evaluation data for the previous model.
- `confusion_matrix.csv`: Confusion matrix for the current model.
- `confusion_matrix_previous_model.csv`: Confusion matrix for the previous model.
- `evaluation_raw_data.csv`: Prediction results files for the evaluation data for the current model and the previous model.
- `metrics.csv`: Evaluation results for the current model’s evaluation data. Evaluation metrics name and evaluation value.
- `metrics_comparison.csv`: Evaluation metrics and evaluation values for the evaluation data for the current model and the previous model.
- `evaluation_results_comparison.csv`: Comparison of trends in prediction results between the previous and current models.
- `model_update_all.csv`: All files combining the prediction model creation (training) data and the evaluation data used to create the current model (output when rf_out is specified and a variable is used to specify a condition).
- `model_update_learn.csv`: The prediction model creation (training) data used to create the current model (output when rf_out is specified).
- `model_update_eval.csv`: The evaluation data used to create the current model (output when rf_out is specified).

##### Example of command execution

**Command Examples (Binary Classification)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe"  mu_learn -md %Temp%\mu_model -od %Temp%\mu_output -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\Model Update_Latest_Premium Service Purchase.csv" -ef_type file -olm %Temp%\model\LearningModel.dat -ef "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\Model Update_Latest_Premium Service Purchase (evaluation).csv"

#### Variable Information Generation (mu_mkcolinfo) Command Specifications

This command automatically generates a variable information file to be used for model update.
Input a previously trained model and the latest data for creating (training) a prediction model
to automatically generate a variable information file after model update.

`PredictionOneCmd.exe mu_mkcolinfo
[-lf learning_data_file_path] [-ci column_info_output_file_path] (-olm old_model_file_path) (-olf old_learning_data_file_path)  (-omd old_model_dir_path)`

<div class="command-line">

| Option Name | Option Description                                                                                                                                                                                                                           |
| :----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-lf`     | Input path of data (CSV/TSV) for up-to-date prediction model creation (learning).                                                                                                                                                                                                          |
|    `-ci`     | Output path of the variable information file (CSV).                                                                                                                                                                                                                                                                                           |
|    `-olm`     | (optional) Path of the previous trained model. Required if not using -omd.                                                                                                                                                                                                                                                                                            |
|    `-olf`     | (optional) Creation (training) data for the previous trained prediction model. Required if not using -omd.                                                                                                                                                                                                                                                                                            |
|    `-omd`     | (optional) Path of the directory of the previous trained model. Used to refer to data and settings from the previous training. Required if not using -olm -olf.                                                                                                                                                                                                                                                                                             |

</div>

**Example of command execution**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe"  mu_mkcolinfo -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\Model Update_Latest_Premium Service Purchase.csv" -ci %Temp%\column_info.csv -olm %Temp%\model\LearningModel.dat -olf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\Model Update_Premium Service Purchase.csv"

#### Compare Prediction Results (compare_predict) Command Specifications

This command outputs the results of a prediction using the model used for prediction and the model used for comparison, respectively.
Input the model used for prediction, the model used for comparison, and the prediction data
to output the prediction results.

`PredictionOneCmd.exe compare_predict [-md model_dir_path] [-od output_dir_path]
[-pf prediction_data_file_path]
(-olm old_model_file_path)
(-omd old_model_dir_path)
(-ar add_reason_flag) (-ad add_prediction_data_flag) 
(-nc no_classification_result_flag)
(-pc primary_column)
(-nr no_row_number_flag)
(-th threshold)
`

<div class="command-line">

| Option Name | Option Description                                                                                                                                                                                                                                                                                                                                          |
| :----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-md`     | Path of the directory of the model used for prediction. The directory containing the set of model files generated by the learn command must be specified.                                                                                                                                                                                                                                                |
|    `-od`     | Path of the output directory. For the contents of the following files in the directory, see "About Files Output to the Output Directory During Prediction Result Comparison (compare_predict)."                                                                                                                                                                                         |
|    `-pf`     | Path of the prediction data.                                                                                                                                                                                                                                                       |
|    `-olm`     | (optional) Path of the trained model to be used for comparison. Required if not using -omd.                                                                                                                                                                                                                                                                                            |
|    `-omd`     | (optional) Directory path of the trained model to be used for comparison. Required if not using -olm.                                                                                                                                                                                                                                                                                             |
|    `-ar`     | (optional) Whether to calculate the reason for the prediction (output prediction_analysis.csv). Specify `true` if a prediction reason is required. Specify `false` to reduce the processing time without requiring a prediction reason. Identical to `true` if omitted.                                                                                                                                                       |
|    `-ad`     | (optional) Whether the prediction data should be added to the output. Specify `true` to add it. Identical to `false` if omitted.                                                                                                                                                                                                                                                       |
|    `-nc`     | (optional) Whether to output the classification results (in addition to the predicted probabilities) during binary and multiclass classification. Specify `true` if the classification result is not required. `false` if classification results are required. Identical to `true` if omitted.                                                                                                                                                                               |
|    `-pc`     | (optional) Name of the variable to be attached to the left end of the prediction result. Used to assign the specified variable in place of a row number. |
|    `-nr`     | (optional) Whether to output row numbers in the prediction results. Specify `true` if the line number is not required. If line numbers are required, specify `false`. Identical to `false` if omitted.                                                                                                                                                                                                            |
|    `-th`     | (optional) Specifies the threshold value for the classification results output when `-nc false` is specified for a binary classification prediction. If a threshold is specified with `-th`, the predicted probabilities output by the prediction model are compared to the specified threshold, and whether or not the threshold is exceeded is output as the classification result. If `-1.0` is specified as the threshold value, the threshold value that maximizes accuracy in the evaluation data is used to output the classification result. |

</div>

##### About Files Output to the Output Directory During Prediction Result Comparison (compare_predict)

- `prediction_valid.csv`: The row number of the successfully predicted row and the predicted result.
- `prediction_analysis.csv`: The row number of the successfully predicted row and the predicted result and the prediction reason.
- `prediction_skip.csv`: Row number of the row for which the prediction was skipped. (for example, different number of columns)
- `prediction_invalid.csv`: Row number of the row for which the prediction failed. (for example, model inconsistency)

**Example of command execution**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" compare_predict -md %Temp%\mu_model -od %Temp%\output_pred -pf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\Model Update_Latest_Premium Service Purchase (prediction).csv" -olm %Temp%\model\LearningModel.dat

#### Compare Evaluation Results (compare_eval) Command Specifications

This command outputs evaluation results for a trained model and the model used for comparison, respectively.
Input the trained model, the model used for comparison, and the evaluation data
to output the evaluation results.
This command compares two previously created prediction models using the evaluation data.

`PredictionOneCmd.exe compare_eval [-md model_dir_path] [-od output_dir_path]
[-ef prediction_data_file_path]
(-olm old_model_file_path) (-omd old_model_dir_path) (-er save_evaluation_results)`

<div class="command-line">

| Option Name | Option Description                                                                                                                                                                                                                                                                                                                                          |
| :----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-md`     | Path of the trained model directory. The directory containing the set of model files generated by the learn command must be specified.                                                                                                                                                                                                                                                |
|    `-od`     | Path of the output directory.                                                                                                                                                                                         |
|    `-ef`     |Path of evaluation data (CSV/TSV).                                                                            |
|    `-olm`     |(optional) Path of the previous trained model to be used for comparison. Required if not using -omd.                                                                                                                                                                                                                                                                                            |
|    `-omd`     | (optional) Directory path of the trained model to be used for comparison. Required if not using -olm.                                                                                                                                                                                                                                                                                             |
|    `-er`     | (optional) Used to save prediction results for evaluation data. Specify `true` to save or `false` to not save. Identical to `false` if omitted.                                                                                                                                                                                                                                                                                            |

**Example of command execution**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" compare_eval -md %Temp%\mu_model -od %Temp%\output_eval -ef "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\Model Update_Latest_Premium Service Purchase (evaluation).csv" -olm %Temp%\model\LearningModel.dat

</div>

{{% dist_type_only "SNC" %}}

#### License (license) Command Specifications

This command performs license control. There are several operations, such as registering and releasing licenses.

`PredictionOneCmd.exe license [-op <operation>] (-proxy <hostURL|mode>) (-pu <username>) (-pp <passwd>)`

<div class="command-line">

| Option Name | Option Description                                                                                                                                                                     |
| :----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-op`     | Specifies operations such as registering and releasing licenses. Some operations may require additional parameters. See the table below for specifications of each operation.                     |
|   `-proxy`   | Specifies the hostname or mode of the proxy. The mode is `auto` which uses the system settings, `env` which references the environment variable HTTPS_PROXY, and `none` which does not use a proxy. Identical to `auto` if omitted. |
|    `-pu`     |  Specify only when necessary.                                                                                                                                         |
|    `-pp`     | Proxy password. Specify only when necessary.                                                                                                                                       |

</div>

<div class="command-line operation-list">

|                            Operation Name                            | Operation Description                                                                                                                             |
| :--------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                  `network_install [-eid license_id]`                   | (With internet connection) Registers a license over the network. Specify the license ID with the `-eid` option.                                    |
|                     `network_revoke (-target [cui                      | gui]                                                                                                                                             | -eid <license_id>)` |(With internet connection) Releases a license over the network. Specify `cui` or `gui` with the `-target` option, or specify a license ID with the `-eid` option. If omitted, releases the license of the command line (cui) version currently in use. |
|                     `network_update (-target [cui                      | gui]                                                                                                                                             | -eid <license_id>)` | (With internet connection) Updates a license over the network. Specify `cui` or `gui` with the `-target` option, or specify a license ID with the `-eid` option. If omitted, updates the license of the command line (cui) version currently in use. |
|                     `network_update_all (-target [cui|gui])` | (With internet connection) Updates all licenses over the network. Specify `cui` or `gui` with the `-target` option. If omitted, updates the licenses of all command line (cui) versions. |
|                `footprint [-file footprint_file_path]`                 | (Without internet connection) Generates a PC identification file. Specify the output destination of the PC identification file with the `-file` option.                                     |
|                  `install [-file license_file_path]`                   | (Without internet connection) Installs a license file. Specify the license file you want to install with the `-file` option.               |
| `revoke [-ticket revocation_file_path] [-proof revocation_proof_path]` |(Without internet connection) Specify a license release file with the `-ticket` option, and specify the output destination for the license release completion file with the `-proof` option. |

</div>

##### Example of command execution

**Command Example 1 (License Registration with Internet Connection)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op network_install -eid abcdef01-2345-6789-abcd-ef0123456789

**Command Example 2 (License Release with Internet Connection)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op network_revoke

**Command Example 3 (License Update with Internet Connection)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op network_update

**Command Example 4 (PC Identification File Generation Without Internet Connection)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op footprint -file %Temp%\PC identification file.txt

**Command Example 5 (Register License File Without Internet Connection)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op install -file %Temp%\license file.txt

**Command Example 6 (License Release File Input + License Release + License Release Complete File Output Without Internet Connection)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op revoke -ticket %Temp%\license release file.txt -proof %Temp%\license release completion file.txt

{{% /dist_type_only %}}
