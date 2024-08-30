---
title: "コマンドライン機能"
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
keywords: ["コマンドライン", "プロンプト", "bash", "cui", "実行コマンド"]
---

Prediction One は GUI ツールですが、一部の機能はコマンドライン機能を利用することで、GUI を使わずに実行することが可能です。

#### 学習 (learn) コマンド仕様


学習データから予測モデルを生成するコマンドです。

`PredictionOneCmd.exe learn [-md model_dir_path] [-od output_dir_path] [-lf learning_data_file_path] [-tc target_column_name] [-tt task_type] (-tv target_value) (-ef evaluation_data_file_path) (-ci column_info_file_path) (-cv cross_validation_k_fold) (-im imbalanced_data_flag) (-tsm time_series_forecast_model_flag) (-tsu time_series_forecast_time_unit) (-tsc time_series_forecast_time_column_name) (-tsi time_series_forecast_time_unit_interval) (- tsf time_series_forecast_from) (-tst time_series_forecast_to) (-tsa time_series_forecast_analysis_flag) (-tsin time_series_forecast_other_column_flag) (-tsine time_series_forecast_other_column_exception)`

<div class="command-line">

| オプション名 | オプションの説明                                                                                                                                                                                                                                                                                                             |
| :----------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-md`     | モデルディレクトリのパス。実行するとモデルファイル群が生成される。                                                                                                                                                                                                                                                           |
|    `-od`     | アウトプットディレクトリのパス。ディレクトリ内に出力されるファイル一覧については「学習 (learn) 時にアウトプットディレクトリに出力されるファイルについて」を参照。                                                                                                                                                            |
|    `-lf`     | 予測モデル作成(学習)用データ(CSV/TSV)の入力パス。                                                                                                                                                                                                                                                                                            |
|    `-tc`     | 予測したい項目(予測ターゲット)として使用する項目の名前。                                                                                                                                                                                                                                                                     |
|    `-tt`     | 予測タイプ。二値分類なら`binary_classification`、多値分類なら`multi_classification`、数値予測なら`regression`を指定する。                                                                                                                                                                                                    |
|    `-tv`     | 予測値。予測タイプで二値分類を指定した場合は必須。それ以外は指定なし。                                                                                                                                                                                                                                                       |
|    `-ef`     | 評価用データ(CSV/TSV)の入力パス。省略した場合、学習データから自動抽出。                                                                                                                                                                                                                                                      |
|    `-er`     | 評価用データに対する予測結果ファイルをアウトプットディレクトリに出力するかどうか。出力する場合は`true`、出力しない場合は`false`を指定する。省略した場合は`false`と同じ。                                                                                                                                                     |
|    `-ci`     | 項目情報ファイル(CSV)の入出力パス。省略した場合、学習データの先頭 1000 行から自動で判定される。項目情報ファイルのフォーマットは、項目情報生成コマンドの仕様 (-ci の説明部分) を参照。                                                                                                                                        |
|    `-cv`     | k 分割交差検証の分割数。`0`を指定すると学習データに基づき、交差検証を行うかどうかとその分割数を自動決定する。`-1`を指定すると交差検証は必ず行うが、その分割数は学習データに基づき自動決定する。`1`を指定すると交差検証を行わない。`2`以上を指定すると、指定された数 k で k 分割交差検証を行う。省略した場合は`0`指定と同じ。 |
|    `-im`     | 予測したい項目の値の偏りを補正するかどうか。予測タイプが分類のときのみ設定可能。補正する場合は`true`、補正しない場合は`false`を指定。省略した場合は`false`と同じ。                                                                                                                                                           |
|    `-tsm`    | 時系列予測モードを使用するかどうか。時系列予測モードを使用する場合は`true`を指定、使用しない場合は`false`を指定する。省略した場合は`false`と同じ。時系列予測モードが使用できるのは予測タイプ(-tt)が数値予測(regression)のときのみ。                                                                                          |
|    `-tsu`    | 時系列予測の時間単位。年の場合`year`、月の場合`month`、日の場合`day`、時間の場合`hour`、分の場合`minute`、月末日の場合`eom`を指定する。自動判定の場合は、本オプション(`-tsu`)を指定しない。                                                                                                                                  |
|    `-tsc`    | 時系列予測の予測したい項目(予測ターゲット)の時間情報項目。時系列予測モードを使用する(-tsm true)場合は必須。                                                                                                                                                                                                                  |
|    `-tsi`    | 時系列予測の時間間隔。整数を指定する。時間単位は-tsu で指定したものが使用される。たとえば 2 ヶ月間隔の場合、-tsu month -tsi 2 と指定する。自動判定の場合は、本オプション(-tsi)を指定しないか、0 を指定する。                                                                                                                   |
|    `-tsf`    | 時系列予測の予測期間の開始時期。時系列予測モードを使用する(-tsm true)の場合必須。1 以上の整数を指定する。時間単位は-tsu で指定したものが使用される。たとえば、予測期間が「2 ヶ月後から 4 ヶ月後まで」の場合、-tsu month -tsf 2 -tst 4 と指定する。                                                                           |
|    `-tst`    | 時系列予測の予測期間の終了時期。時系列予測モードを使用する(-tsm true)の場合必須。-tsf で指定した値以上の整数を指定する。時間単位は-tsu で指定したものが使用される。たとえば、予測期間が「2 ヶ月後から 4 ヶ月後まで」の場合、-tsu month -tsf 2 -tst 4 と指定する。                                                            |
|    `-tss`    | 時系列予測の系列項目。系列項目がある場合のみ指定する。                                                                                                                                                                                                                                                                       |
|    `-tsa`    | 時系列予測時に寄与度分析を行うかどうか。寄与度分析を行う場合は true を指定、行わない場合は false を指定する。省略した場合は true と同じ。                                                                                                                                                                                    |
|    `-tsin`   | 時系列予測の予測期間について、予測したい項目以外の項目が手に入るかどうか。全ての項目が手に入る場合は`true`、全て手に入らない場合は`false`を指定する。省略した場合は`false`と同じ。手に入る項目、手に入らない項目が混在する場合は次の`-tsine`で例外を指定する。<br/>(v3.0以前と同じ学習を行いたい場合は、`true`を指定する。詳細は、{{% a_in "../../tips/new_features/timeseries_features/" "予測したい項目以外の項目" %}}を参照)                                                                                                                                                                                    |
|    `-tsine`   | 時系列予測の予測期間について、予測したい項目以外の項目が手に入るかどうか、例外項目を指定する。`-tsin`が`true`の場合は、予測期間について値が手に入らない項目を指定する。`-tsin`が`false`の場合は、予測期間について値が手に入る項目を指定する。複数の項目を指定したい場合は、`-tsine {項目名1} -tsine {項目名2} …`のように複数回用いる。                                                                                                                                                                                    |

</div>


{{< notice warning >}}
【時系列予測モードの予測モデル作成に関する注意】<br/>
v3.0 (2022年5月) 以前から Prediction One を使用されている方は、`-tsin`を`true`にしないと、
今まで通りの予測モデル作成ができない仕様変更になっております。<br/>
今までと同じように予測モデルの作成を行いたい場合はご注意ください。また、仕様の詳細については、{{% a_in "../../tips/new_features/timeseries_features/" "予測したい項目以外の項目" %}}をご確認ください。
{{</ notice >}}

##### 学習 (learn) 時にアウトプットディレクトリに出力されるファイルについて

- `metrics.csv`：評価データに対する評価結果。評価指標名と評価値。
- `analysis_summary.csv`：評価データに対する項目の寄与度。
- `evaluation_raw_data.csv`：評価用データに対する予測結果ファイル。

##### コマンド実行例

**コマンドの例 (二値分類)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" learn -md %Temp%\model -od %Temp%\output -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\二値分類_故障予測.csv" -tc 状態(予測対象) -tt binary_classification -tv 故障

**コマンドの例 (数値予測：時系列予測モード)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" learn -md %Temp%\model_ts -od %Temp%\output_ts -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\数値予測_需要予測.csv" -tc 出荷数(予測対象) -tt regression -tsm true -tsc 日付 -tsf 1 -tst 180

#### 予測 (predict) コマンド仕様

予測モデルを予測データに適用し、予測結果を生成するコマンドです。

`PredictionOneCmd.exe predict [-md model_dir_path] [-od output_dir_path] [-pf prediction_data_file_path] (-ar add_reason_flag) (-ad add_prediction_data_flag) (-nc no_classification_result_flag) (-nr no_row_number_flag) (-th threshold_for_classification_result)`

<div class="command-line">

| オプション名 | オプションの説明                                                                                                                                                                                                                                                                                                                                          |
| :----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-md`     | モデルディレクトリのパス。学習コマンドで生成されたモデルファイル群を含むディレクトリを指定する必要がある。                                                                                                                                                                                                                                                |
|    `-od`     | アウトプットディレクトリのパス。ディレクトリ内に以下のファイルの内容については「予測 (predict) 時にアウトプットディレクトリに出力されるファイルについて」を参照。                                                                                                                                                                                         |
|    `-pf`     | 予測用データ(CSV/TSV)のパス。数値予測の時系列予測モードで、予測したい項目(予測ターゲット)項目と時間情報項目と系列項目以外を学習に使用していない場合は、本オプション(-pf)は省略可能。その場合、予測データは自動生成され、すべての予測可能な期間・系列に関して予測が出力される。                                                                            |
|    `-ar`     | 予測理由の算出を行う(prediction_analysis.csv を出力する)かどうか。予測理由が必要な場合は`true`を指定する。予測理由が不要で処理時間を短縮したい場合は`false`を指定する。省略した場合は`true`と同じ。                                                                                                                                                       |
|    `-ad`     | 予測用データを出力に追加するかどうか。追加する場合は`true`を指定する。省略した場合は`false`と同じ。                                                                                                                                                                                                                                                       |
|    `-nc`     | 二値分類・多値分類時に、(予測確率に加えて)分類結果を出力しないかどうか。分類結果が不要な場合は`true`を指定する。分類結果が必要な場合は`false`。省略した場合は`true`と同じ。                                                                                                                                                                               |
|    `-nr`     | 予測結果に行番号を出力しないかどうか。行番号が不要な場合`true`を指定する。行番号が必要な場合は`false`を指定する。省略した場合は`false`と同じ。                                                                                                                                                                                                            |
|    `-th`     | 二値分類の予測において `-nc false` と指定した際に出力される分類結果について、分類を行う際の閾値を指定する。`-th` で閾値が指定されている場合、予測モデルが出力した予測確率と指定された閾値を比較し、閾値を超えたかどうかを分類結果として出力する。閾値として `-1.0` を指定した場合、評価データにおいて正解率が最大となる閾値を使用して分類結果を出力する。 |

</div>

##### 予測 (predict) 時にアウトプットディレクトリに出力されるファイルについて

- `prediction_valid.csv`：正常に予測された行の行番号と予測結果。
- `prediction_analysis.csv`：正常に予測された行の行番号と予測結果と予測理由。
- `prediction_skip.csv`：予測がスキップされた行の行番号。(列数が異なるなど)
- `prediction_invalid.csv` ：予測に失敗した行の行番号。(モデルとの不整合など)

##### コマンド実行例

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" predict -md %Temp%\model -od %Temp%\output -pf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\二値分類_故障予測（予測用）.csv"

#### 項目情報生成(mkcolinfo)コマンド仕様

学習時に利用する項目情報ファイルを自動生成するコマンドです。自分で項目情報ファイルを生成
する際は実行する必要はありません。

`PredictionOneCmd.exe mkcolinfo [-lf learning_data_file_path] [-ci column_info_output_file_path] (-tc target_column_name)`

<div class="command-line">

| オプション名 | オプションの説明                                                                                                                                                                                                                           |
| :----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-lf`     | 予測モデル作成(学習)用データ(CSV/TSV)の入力パス。                                                                                                                                                                                                          |
|    `-ci`     | 項目情報ファイル(CSV)の出力パス。                                                                                                                                                                                                          |
|    `-tc`     | 予測したい項目(予測ターゲット)として使用する項目の名前。省略した場合、項目の型(integer/float/string/text/date)判定結果のみをそのまま出力する。指定した場合は、項目の型判定に加えて使用しない項目(ignore)の判定までを行った結果を出力する。 |

</div>

**コマンド実行例**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" mkcolinfo -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\二値分類_故障予測.csv" -ci %Temp%\column_info.csv -tc 状態(予測対象)

#### モデル更新の学習 (mu_learn) コマンド仕様

前回の学習済みモデルを更新して最新のモデルを作成します。 
前回の学習済みモデル、最新の予測モデル作成(学習)用データ、評価用データを入力して
最新の学習済みモデルと精度の比較結果を生成できます。

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

| オプション名 | オプションの説明                                                                                                                                                                                                                                                                                                             |
| :----------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-md`     | モデルディレクトリのパス。実行するとモデルファイル群が生成される。                                                                                                                                                                                                                                                           |
|    `-od`     | アウトプットディレクトリのパス。ディレクトリ内に出力されるファイル一覧については「モデル更新(mu_learn) 時にアウトプットディレクトリに出力されるファイルについて」を参照。                                                                                                                                                            |
|    `-lf`     | 最新の予測モデル作成(学習)用データ(CSV/TSV)の入力パス。                                                                                                                                                                                                                                                                                            |
|    `-ef_type`     | 評価用データを指定する方法。ファイルを指定する場合は `file`、項目の条件で指定する場合は`column_range`。                                                                                                                                                                                                                                                                                            |
|    `-ef`     | (optional) 前回と今回のモデルを比較するための評価用データ。評価用データが eval.csv のときは -ef_type file -ef eval.csv と指定する。ef_type が file のときに必須。                                                                                                                                                                                                                                                                                            |
|    `-ef_auto_col`     | (optional) 項目で評価用データの条件を指定時、基準として用いる項目名。項目「顧客ID」で予測モデル作成(学習)用データと評価用データを分割する際には、-ef_auto_col 顧客ID と指定する。ef_type が column_range のときに使用。                                                                                                                                                                                                                                                                                            |
|    `-ef_auto_thres`     | (optional) 項目で評価用データの条件を指定時、基準として用いる数値の閾値。項目が数値の場合に使用し、たとえば「顧客ID」が10000以降のデータを評価用データとする際には、-ef_auto_thres 10000 と指定する。ef_type が column_range のときに使用。                                                                                                                                                                                                                                                                                            |
|    `-ef_auto_thres_dt`     | (optional) 項目で評価用データの条件を指定時、基準として用いる日付文字列の閾値。項目が日付文字列の場合に使用し、たとえば「入会日」が2018年8月25日以降のデータを評価用データとする際には、-ef_auto_thres_dt 2018/08/25 と指定する。ef_type が column_range のときに使用。                                                                                                                                                                                                                                                                                            |
|    `-ef_auto_op`     | (optional) 項目で評価用データの条件を指定時、範囲を指定するための基準。「より大きい」の場合は`GT`, 「より小さい」の場合は`LT`, 「以上」の場合は`GE`, 「以下」の場合は`LE`を指定する。項目「入会日」が2018/08/25以降のデータを評価用データとする際には、-ef_type column_range -ef_auto_col 入会日 -ef_auto_thres_dt 2018/08/25 -ef_auto_op GE と指定する。ef_type が column_range のときに使用。省略した場合は`GE`と同じ。                                                                                                                                                                                                                                                                                         |
|    `-olm`     | (optional) 学習済みの前回のモデルのパス。-omd を使用しない場合には必須。                                                                                                                                                                                                                                                                                            |
|    `-olf`     | (optional) 学習済みの前回の予測モデル作成(学習)用データのパス。前回の予測モデル作成(学習)用データも今回の学習に含める(後述の -use_olf が`true`)場合、もしくは項目で評価用データの条件を指定時にこの引数を与えることで、前回のモデルが評価用データの情報を学習に使用している際に警告を表示することが出来る。                                                                                                                                                                                                                                                                                            |
|    `-oef`     | (optional) 学習済みの前回の評価用データのパス。前回の評価用データも今回の学習に含める(後述の -use_oef が`true`)場合に指定する。                                                                                                                                                                                                                                                                                            |
|    `-omd`     | (optional) 前回の学習済みモデルディレクトリのパス。GUI版で学習した際のモデルディレクトリを入力することを想定。指定されたモデルと最新のデータを用いて作成したモデルの比較を行う。-olm -olf -oef を使用しない場合には必須。                                                                                                                                                                                                                                                                                             |
|    `-use_olf`     | (optional) 前回の予測モデル作成(学習)用データを今回の予測モデル作成(学習)用データに結合して使用するかどうか。使用する場合は`true`、使用しない場合は`false`を指定する。省略した場合は`false`と同じ。                                                                                                                                                                                                                                                                                            |
|    `-use_oef`     | (optional) 前回の評価用データを今回の予測モデル作成(学習)用データに結合して使用するかどうか。使用する場合は`true`、使用しない場合は`false`を指定する。省略した場合は`false`と同じ。                                                                                                                                                                                                                                                                                            |
|    `-er`     | (optional) 評価用データに対する予測結果を保存する際に使用する。保存する場合は`true`、そうでない場合は`false`を指定する。省略した場合は`false`と同じ。                                                                                                                                                                                                                                                                                            |
|    `-rf_out`     | (optional) 学習処理の入力データを出力するかどうか。出力する場合は`true`、そうでない場合は`false`を指定する。省略した場合は`false`と同じ。                                                                                                                                                                                                                                                                                            |
|    `-ci`     | (optional) 項目情報ファイル。学習に使用する項目の設定を指定する際に使用する。                                                                                                                                                                                                                                                                                            |
|    `-pk`     | (optional) プライマリキーに指定する項目。-olf を指定し -use_olf が`true`のとき、もしくは `-oef` を指定時、前回のデータと指定した項目名が重複した行を今回の予測モデル作成(学習)用データから取り除く。                                                                                                                                                                                                                                                                                            |

</div>

##### モデル更新 (mu_learn) 時にアウトプットディレクトリに出力されるファイルについて

- `analysis_summary.csv`：今回のモデルの評価用データに対する項目の寄与度。
- `analysis_summary_previous_model.csv`：前回のモデルの評価用データに対する項目の寄与度。
- `confusion_matrix.csv`：今回のモデルの混同行列。
- `confusion_matrix_previous_model.csv`：前回のモデルの混同行列。
- `evaluation_raw_data.csv`：今回のモデルと前回のモデルの評価用データに対する予測結果ファイル。
- `metrics.csv`：今回のモデルの評価用データに対する評価結果。評価指標名と評価値。
- `metrics_comparison.csv`：今回のモデルと前回のモデルの評価用データに対する評価指標と評価値。
- `evaluation_results_comparison.csv`：前回と今回のモデルの予測結果の傾向の比較。
- `model_update_all.csv`：今回のモデルの作成に用いた予測モデル作成(学習)用データと評価用データを結合した全ファイル(rf_out 指定時かつ項目で条件を指定時に出力される)。
- `model_update_learn.csv`：今回のモデルの作成に用いた予測モデル作成(学習)用データ(rf_out 指定時に出力される)。
- `model_update_eval.csv`：今回のモデルの作成に用いた評価用データ(rf_out 指定時に出力される)。

##### コマンド実行例

**コマンドの例 (二値分類)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" learn -md %Temp%\model -od %Temp%\output -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\モデル更新_プレミアムサービス購入.csv" -tc プレミアムサービス(予測対象) -tt binary_classification -tv 購入あり
    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" mu_learn -md %Temp%\mu_model -od %Temp%\mu_output -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\モデル更新_最新_プレミアムサービス購入.csv" -ef_type file -olm %Temp%\model\LearningModel.dat -ef "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\モデル更新_最新_プレミアムサービス購入（評価用）.csv"


#### 項目情報生成(mu_mkcolinfo)コマンド仕様

モデル更新用の項目情報ファイルを自動生成するコマンドです。
学習済みのモデル、最新の予測モデル作成(学習)用データを入力することで
モデル更新後の項目情報ファイルを自動生成できます。

`PredictionOneCmd.exe mu_mkcolinfo
[-lf learning_data_file_path] [-ci column_info_output_file_path] (-olm old_model_file_path) (-olf old_learning_data_file_path)  (-omd old_model_dir_path)`

<div class="command-line">

| オプション名 | オプションの説明                                                                                                                                                                                                                           |
| :----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-lf`     | 最新の予測モデル作成(学習)用データ(CSV/TSV)の入力パス。                                                                                                                                                                                                          |
|    `-ci`     | 項目情報ファイル(CSV)の出力パス。                                                                                                                                                                                                                                                                                           |
|    `-olm`     | (optional) 学習済みの前回のモデルのパス。-omd を使用しない場合に必須。                                                                                                                                                                                                                                                                                            |
|    `-olf`     | (optional) 学習済みの前回の予測モデル作成(学習)用データ。-omd を使用しない場合に必須。                                                                                                                                                                                                                                                                                            |
|    `-omd`     | (optional)学習済みの前回のモデルディレクトリのパス。前回の学習時のデータや設定を参照するために使用する。-olm -olf を使用しない場合に必須。                                                                                                                                                                                                                                                                                             |

</div>

**コマンド実行例**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" mu_mkcolinfo -lf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\モデル更新_最新_プレミアムサービス購入.csv" -ci %Temp%\column_info.csv -olm %Temp%\model\LearningModel.dat -olf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\モデル更新_プレミアムサービス購入.csv"

#### 予測結果の比較 (compare_predict) コマンド仕様

予測に用いるモデルと、比較対象のモデルを用いてそれぞれの予測結果を出力するコマンドです。
予測に用いるモデル、比較対象のモデル、予測用データを入力して
予測結果を出力します。

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

| オプション名 | オプションの説明                                                                                                                                                                                                                                                                                                                                          |
| :----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-md`     | 予測に用いるモデルディレクトリのパス。学習コマンドで生成されたモデルファイル群を含むディレクトリを指定する必要がある。                                                                                                                                                                                                                                                |
|    `-od`     | アウトプットディレクトリのパス。ディレクトリ内に以下のファイルの内容については「予測結果の比較 (compare_predict) 時にアウトプットディレクトリに出力されるファイルについて」を参照。                                                                                                                                                                                         |
|    `-pf`     | 予測用データのパス。                                                                                                                                                                                                                                                       |
|    `-olm`     | (optional) 比較対象となる学習済みのモデルのパス。-omd を使用しない場合に必須。                                                                                                                                                                                                                                                                                            |
|    `-omd`     | (optional) 比較対象となる学習済みのモデルディレクトリのパス。-olm を使用しない場合に必須。                                                                                                                                                                                                                                                                                             |
|    `-ar`     | (optional) 予測理由の算出を行う(prediction_analysis.csv を出力する)かどうか。予測理由が必要な場合は`true`を指定する。予測理由が不要で処理時間を短縮したい場合は`false`を指定する。省略した場合は`true`と同じ。                                                                                                                                                       |
|    `-ad`     | (optional) 予測用データを出力に追加するかどうか。追加する場合は`true`を指定する。省略した場合は`false`と同じ。                                                                                                                                                                                                                                                       |
|    `-nc`     | (optional) 二値分類・多値分類時に、(予測確率に加えて)分類結果を出力しないかどうか。分類結果が不要な場合は`true`を指定する。分類結果が必要な場合は`false`。省略した場合は`true`と同じ。                                                                                                                                                                               |
|    `-pc`     | (optional) 予測結果の左端に付与する項目の名前。行番号の代わりに指定した項目を付与する際に使用する。 |
|    `-nr`     | (optional) 予測結果に行番号を出力しないかどうか。行番号が不要な場合`true`を指定する。行番号が必要な場合は`false`を指定する。省略した場合は`false`と同じ。                                                                                                                                                                                                            |
|    `-th`     | (optional) 二値分類の予測において `-nc false` と指定した際に出力される分類結果について、分類を行う際の閾値を指定する。`-th` で閾値が指定されている場合、予測モデルが出力した予測確率と指定された閾値を比較し、閾値を超えたかどうかを分類結果として出力する。閾値として `-1.0` を指定した場合、評価データにおいて正解率が最大となる閾値を使用して分類結果を出力する。 |

</div>

##### 予測結果の比較 (compare_predict) 時にアウトプットディレクトリに出力されるファイルについて

- `prediction_valid.csv`：正常に予測された行の行番号と予測結果。
- `prediction_analysis.csv`：正常に予測された行の行番号と予測結果と予測理由。
- `prediction_skip.csv`：予測がスキップされた行の行番号。(列数が異なるなど)
- `prediction_invalid.csv` ：予測に失敗した行の行番号。(モデルとの不整合など)

**コマンド実行例**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" compare_predict -md %Temp%\mu_model -od %Temp%\output_pred -pf "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\モデル更新_最新_プレミアムサービス購入（予測用）.csv" -olm %Temp%\model\LearningModel.dat

#### 評価結果の比較 (compare_eval) コマンド仕様

学習済みのモデルと比較対象のモデルそれぞれで評価結果を出力するコマンドです。
学習済みのモデル、比較対象のモデル、評価用データを入力して
評価結果を出力します。
作成済みの２つの予測モデルを評価データを用いて比較するコマンドです。

`PredictionOneCmd.exe compare_eval [-md model_dir_path] [-od output_dir_path]
[-ef prediction_data_file_path]
(-olm old_model_file_path) (-omd old_model_dir_path) (-er save_evaluation_results)`

<div class="command-line">

| オプション名 | オプションの説明                                                                                                                                                                                                                                                                                                                                          |
| :----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-md`     | 学習済みのモデルディレクトリのパス。学習コマンドで生成されたモデルファイル群を含むディレクトリを指定する必要がある。                                                                                                                                                                                                                                                |
|    `-od`     | アウトプットディレクトリのパス。                                                                                                                                                                                         |
|    `-ef`     | 評価用データ(CSV/TSV)のパス。                                                                            |
|    `-olm`     | (optional) 比較対象となる学習済みの前回のモデルのパス。-omd を使用しない場合に必須。                                                                                                                                                                                                                                                                                            |
|    `-omd`     | (optional) 比較対象となる学習済みのディレクトリのパス。-olm を使用しない場合に必須。                                                                                                                                                                                                                                                                                             |
|    `-er`     | (optional) 評価用データに対する予測結果を保存する際に使用する。保存する場合は`true`、そうでない場合は`false`を指定する。省略した場合は`false`と同じ。                                                                                                                                                                                                                                                                                            |

**コマンド実行例**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" compare_eval -md %Temp%\mu_model -od %Temp%\output_eval -ef "{{< preone_home_path_bs >}}\ja-JP\doc\sample_dataset\モデル更新_最新_プレミアムサービス購入（評価用）.csv" -olm %Temp%\model\LearningModel.dat

</div>

{{% dist_type_only "SNC" %}}

#### ライセンス(license)コマンド仕様

ラインセス管理を行うコマンドです。ライセンスの登録や解除など、複数のオペレーションがあります。

`PredictionOneCmd.exe license [-op <operation>] (-proxy <hostURL|mode>) (-pu <username>) (-pp <passwd>)`

<div class="command-line">

| オプション名 | オプションの説明                                                                                                                                                                     |
| :----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-op`     | ライセンス登録や解除などのオペレーションを指定する。オペレーションによってさらに追加のパラメータが必要となる場合がある。各オペレーションの仕様は下記の表を参照。                     |
|   `-proxy`   | プロキシのホスト名またはモードを指定する。モードは、`auto`だとシステム設定を利用、`env`だと環境変数 HTTPS_PROXY を参照、`none`だとプロキシを使用しない。省略した場合は`auto`と同じ。 |
|    `-pu`     | プロキシのユーザ名。必要な場合のみ指定する。                                                                                                                                         |
|    `-pp`     | プロキシのパスワード。必要な場合のみ指定する。                                                                                                                                       |

</div>

<div class="command-line operation-list">

|                            オペレーション名                            | オペレーションの説明                                                                                                                             |
| :--------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                  `network_install [-eid license_id]`                   | (インターネット接続あり) ネットワーク経由でライセンスを登録する。`-eid`オプションでライセンス ID を指定する。                                    |
|                     `network_revoke (-target [cui                      | gui]                                                                                                                                             | -eid <license_id>)` | (インターネット接続あり) ネットワーク経由でライセンスを解除する。`-target`オプションで`cui`か`gui`を指定するか、`-eid`オプションでライセンス ID を指定する。省略した場合は現在使用中のコマンドライン(cui)版のライセンスを解除する。 |
|                     `network_update (-target [cui                      | gui]                                                                                                                                             | -eid <license_id>)` | (インターネット接続あり) ネットワーク経由でライセンスを更新する。`-target`オプションで`cui`か`gui`を指定するか、`-eid`オプションでライセンス ID を指定する。省略した場合は現在使用中のコマンドライン(cui)版のライセンスを更新する。 |
|                     `network_update_all (-target [cui|gui])` | (インターネット接続あり) ネットワーク経由でライセンスを全て更新する。`-target`オプションで`cui`か`gui`を指定する。省略した場合はコマンドライン(cui)版のライセンスを全て更新する。 |
|                `footprint [-file footprint_file_path]`                 | (インターネット接続なし) PC 識別ファイルを生成する。`-file`オプションで PC 識別ファイルの出力先を指定する。                                      |
|                  `install [-file license_file_path]`                   | (インターネット接続なし) ライセンスファイルをインストールする。`-file`オプションでインストールしたいライセンスファイルを指定する。               |
| `revoke [-ticket revocation_file_path] [-proof revocation_proof_path]` | (インターネット接続なし) `-ticket`オプションでライセンス解除ファイルを指定し、`-proof`オプションでライセンス解除完了ファイルの出力先を指定する。 |

</div>

##### コマンド実行例

**コマンドの例 1 (インターネット接続ありでライセンス登録)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op network_install -eid abcdef01-2345-6789-abcd-ef0123456789

**コマンドの例 2 (インターネット接続ありでライセンス解除)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op network_revoke

**コマンドの例 3 (インターネット接続ありでライセンス更新)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op network_update

**コマンドの例 4 (インターネット接続なしで PC 識別ファイル生成)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op footprint -file %Temp%\PC識別ファイル.txt

**コマンドの例 5 (インターネット接続なしでライセンスファイル登録)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op install -file %Temp%\ライセンスファイル.txt

**コマンドの例 6 (インターネット接続なしでライセンス解除ファイル入力＋ライセンス解除＋ライセンス解除完了ファイル出力)**

    "{{< preone_home_path_bs >}}\PredictionOneCmd.exe" license -op revoke -ticket %Temp%\ライセンス解除ファイル.txt -proof %Temp%\ライセンス解除完了ファイル.txt

{{% /dist_type_only %}}
