---
title: "目標精度を検討しましょう"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 4
draft: false
# metaタグのパラメータ
meta:
  description: "予測分析ツールPrediction Oneが提案する精度改善のための改善ヒントについて説明するページです。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  ["ヒント","改善ヒント","tips","精度改善"]
toc: true
---

### 説明

通常、予測モデルの精度を100%まで高めることは非常に困難です。予測結果をご自身の業務に活用するには、どの程度の精度が必要なのかを検討し、目標精度を決めましょう。
予測精度は高ければ高いほど良いですが、予測精度が低くても業務に活用する方法はあります。いくつか例を挙げます。

(1) 電話をかける候補者リストの並び替え
「過去に問い合わせを受けたお客様のデータを抽出し候補者リストを作成し、適当な順番に電話をかけて新規サービスを案内し注文を受けたいが、担当者が少ないので1日に100件しか電話できない」というユースケースを考えます。このような場合、現在は適当な順番で電話しているので、この順番がわずかにでも改善すれば、注文を受けられる確率も改善するはずです。この例では、注文を受けられるかどうかの予測精度が60%だったとしても、業務改善につながる可能性があります。

(2) 故障情報を人間が分類する際の補助
「過去のお客様からの修理に関する問い合わせ情報に基づき、現在は人間が故障情報を分類して、適切な部署に修理依頼を割り当てている」というユースケースを考えます。このような場合、故障情報の分類精度が75%程度だったとしても、AIによる分類結果を人間に提示し、人間が誤っているデータを修正する、という方法にすることで、人間の分類の手間を省力化することができます。また、人間が修正した正解データを加えて予測モデルを再作成することで、精度を徐々に改善していくことも可能です。
### 関連資料

- {{% a_in "./../../../tips/result/use_result/" "予測結果の活用例" %}}
- {{% a_in "./../../../tutorial/find_promising_customers/" "成約予測による有望顧客の絞り込み" %}}
- {{% a_in "./../../../tutorial/classification_of_fault_information/" "故障情報の自動分類" %}}


