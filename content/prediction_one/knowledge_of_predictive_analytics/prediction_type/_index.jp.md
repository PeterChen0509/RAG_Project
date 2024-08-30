---
title: "9 教師あり学習の予測タイプ"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 9
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["予測分析", "機械学習", "AI", "予測", "データサイエンス", "基礎"]
---

<style>
  summary {
    position: relative;
    display: block; /* 矢印を消す */
    padding: 10px;
    padding-left: 25px;
    cursor: pointer;
    background-color: #E7F2FA;
    transition: 0.0s;
  }
  summary:hover {
    background-color: #E7F2FA;
  }
  summary::-webkit-details-marker {
    display: none;
  }
  /* 疑似要素でアイコンを表示 */
  summary::before,
  summary::after {
    content: "";
    margin: auto;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
  }
  summary::before {
    width: 20px;
    height: 20px;
    border-radius: 50em;
    background-color: #6AB0DE;
  }
  summary::after {
    left: 8px;
    width: 0;
    height: 0;
    border-style: solid;
    border-width: 4px 0 4px 8px;
    border-color: transparent transparent transparent #fff;
    box-sizing: border-box;
    transition: 0.0s;
  }
  /* オープン時 */
  details {
    padding: 5px;
  }
  details[open] {
    background-color: #F9F9F9;
  }
  details[open] summary {
    background-color: #E7F2FA;
  }
  details[open] summary::after {
    transform: rotate(90deg);
    left: 6px;
    top: 2px;
  }
</style>

<!-- 参考資料 -->
<!-- https://www.stat.go.jp/teacher/dl/pdf/c4learn/materials/fourth/dai1.pdf -->

機械学習は教師あり学習と教師なし学習に大別されること、Prediction Oneは表形式データに対する教師あり学習に対応していることを説明してきました。また、教師あり学習には分類問題と回帰問題があると説明しました（詳しくは「<b>{{% a_in "../about_ml/" "4 機械学習とは" %}}</b>」）。<br/>
Prediction Oneではこれらをさらに分けて「<b>二値分類</b>」、「<b>多値分類</b>」、「<b>数値予測</b>」、「<b>数値予測（時系列予測）</b>」の4つの予測タイプが用意されています。これからそれぞれどのような特徴を持っていてどういった場面で選択すべきかについて説明します。<br/>
 <br/>
![](../img/t_slide44.png)
 <br/>

### 二値分類

二値分類は目的変数が二種類の値しか持たない場合に該当する予測タイプです。例えば、プレミアムサービスの「購入あり/購入なし」、機器の故障における「故障/正常」などです。<br/>
 <br/>
![](../img/t_slide18.png)
 <br/>
二値分類の特徴として予測モデルがどちらになる確率がどの程度かといった確率を出力する点があります。なのでこの確率をもとに、例えば購入の確率が高い顧客順に何か施策を行う、といった活用が可能です。詳しくは二値分類のチュートリアルを参考にしてみてください。<br/>
 <br/>
![](../img/t_slide19.png)
 <br/>

<details>
<summary style="font-weight:bold">二値分類のチュートリアル</summary>

- {{% a_in "../../../tutorial/credit_card_fraud_detection/" "クレジットカード不正取引検知" %}}
- {{% a_in "../../../tutorial/predicting_dm_response/" "DMへの反応予測" %}}
- {{% a_in "../../../tutorial/targeting_based_on_predictive_customer_behavior/" "顧客行動予測に基づいたターゲティング" %}}
- {{% a_in "../../../tutorial/crm_predict_unsubscribe/" "退会予測による退会の削減" %}}
- {{% a_in "../../../tutorial/find_promising_customers/" "成約予測による有望顧客絞り込み" %}}
- {{% a_in "../../../tutorial/predicting_equipment_failures/" "機器の故障予測による故障の未然防止" %}}
- {{% a_in "../../../tutorial/forecast_behavior/" "行動予測による施策の効率化" %}}
- {{% a_in "../../../tutorial/predicting_bad_debts/" "貸し倒れ予測による査定の効率化" %}}

</details>

### 多値分類

多値分類は目的変数が3種類以上の値を持ち、かつ数値でない場合に該当する予測タイプです。例えば、お問い合わせの自動分類、修理依頼の各担当者への自動振り分け、などが挙げられます。<br/>
 <br/>
![](../img/t_slide20.png)
 <br/>
多値分類も二値分類と同様にどのクラスに振り分けられるのかの確率が出力されるため、これを活用することも可能です。<br/>
 <br/>
![](../img/t_slide21.png)
 <br/>

<details>
<summary style="font-weight:bold">多値分類のチュートリアル</summary>

- {{% a_in "../../../tutorial/classification_of_fault_information/" "故障情報の自動分類" %}}
- {{% a_in "../../../tutorial/crm_automate_voice_of_the_customer_labeling/" "顧客の声のラベリング自動化" %}}

</details>

### 数値予測

数値予測は目的変数が大小関係に意味を持つ数値（分類を表すような番号ではないという意味）である場合に該当する予測タイプです。例えば、不動産の成約価格予測、化学材料の物性値予測、などが挙げられます。<br/>
 <br/>
![](../img/t_slide22.png)
 <br/>
数値予測の予測結果は数値になります。業務に導入する際は、この数値の予測結果を使った活用方法を考える必要があります。<br/>
 <br/>
![](../img/t_slide23.png)
 <br/>

<details>
<summary style="font-weight:bold">数値予測のチュートリアル</summary>

- {{% a_in "../../../tutorial/determining_the_number_of_operators/" "入電予測によるオペレータ人数決定" %}}
- {{% a_in "../../../tutorial/predicting_characteristics/" "特性予測による開発の効率化" %}}
- {{% a_in "../../../tutorial/demand_forecast_new_product/" "新商品の需要予測" %}}
- {{% a_in "../../../tutorial/real_estate_price_forecast/" "成約価格の予測" %}}

</details>

### 数値予測（時系列予測）

時系列予測は、目的変数が大小関係に意味を持つ数値（分類を表すような番号ではないという意味）であり、かつ時間に沿って並べた場合に前後に関係が見られる（前後関係に意味がある）場合に該当する予測タイプです。例えば、店舗における来店数予測、製品の出荷数予測、などが挙げられます。<br/>
 <br/>
![](../img/t_slide24.png)
 <br/>
時系列予測の予測結果も数値になります。時系列予測では予測よりも、上振れたとしてどの程度まで上振れそうか、下振れたとしてどの程度まで下振れそうか、といった値も出力でき、上の例の来店数や出荷数の見積もりに活用できます。<br/>
 <br/>
![](../img/t_slide25.png)
 <br/>

<details>
<summary style="font-weight:bold">数値予測（時系列予測）のチュートリアル</summary>

- {{% a_in "../../../tutorial/forecast_the_number_of_visitors/" "来店数予測による仕入れ量決定" %}}
- {{% a_in "../../../tutorial/forecast_demand/" "出荷数予測による生産計画の精度向上" %}}
- {{% a_in "../../../tutorial/forecast_sell/" "販売台数予測による製造計画の改善" %}}
- {{% a_in "../../../tutorial/forecast_order/" "注文数予測による過剰在庫と欠品の防止" %}}

</details>

### 予測タイプの使い分け

#### 二値分類と多値分類

予測したい項目（目的変数）に入っている情報が分類を表すものである場合は二値分類か多値分類が適切です（分類の種類が2つのみの場合は二値分類で3つ以上の場合は多値分類）。<br/>
多値分類の場合は、目的変数のユニーク数、つまり分類（カテゴリ）の数に注意が必要です。例えばデータ数が500行しかないのにユニーク数は200ある場合、1つのカテゴリには大体2～3行分のデータしか存在しないことになります。機械学習モデルはデータを数値で表現する関係上、すべてのカテゴリを全く違うものと認識して学習を行います（詳しくは「<b>{{% a_in "../one_hot_encoding/" "6 ダミー変数・One-Hotエンコーディング" %}}</b>」）。仮に200のカテゴリの部分部分に意味的に近いものがあった場合でも、機械学習モデルにとってそれは全く異なるものであるため（ダミー変数の表現では意味合いの近さを捉えられないため）、1つのカテゴリの傾向を把握するためのサンプルが2～3しか存在せず、ルールやパターンを見い出すのが非常に難しくなってしまいます。こういった場合は意味的に近いカテゴリを1つにまとめてユニーク数を減らす必要があります。<br/>
どの程度までユニーク数を減らす必要があるかは要求される精度やデータの質・量に依存してきてしまうため実際に予測モデルを作成してみて確かめていく必要があります。データ上はユニーク数が3以上でも、多値分類のように細かい分類が必要ない場合は、大まかな分類として二値分類まで粒度を落として予測モデルを作成した方が良い精度が出やすいです。

#### 数値予測と時系列予測

予測したい項目（目的変数）に入っている情報が大小に意味のある数値である場合は数値予測が適切です。数値予測には通常の数値予測と時系列予測モードの2つがあります。時系列予測モードを使用すると、過去の出荷数や時間情報（季節・曜日・午前や午後などの時間からわかる情報）を利用した予測をするようになります。 データを時間に沿って並べてみたとき、予測したい項目の並びに時間的な関係がある場合、時系列予測モードをご利用ください。<br/>
 <br/>
![](../img/t_slide26.png)
