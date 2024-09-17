---
title: "評価結果の閲覧"
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
keywords: [""]
tutorial_page:
  is_next_exists: true
---

{{% div_slide "ステップ1" normal first-page %}}

![](../img/t_slide11.png)

予測モデルの学習後、予測精度の評価までを自動で行います。この画面ではモデルのサマリを確認できます。

予測精度は作成した予測モデルの予測結果と実際の結果を比較することで算出されます。
予測精度レベルの星の数から、良い精度でサービスの購入を予測できる事がわかりました！
{{% /div_slide %}}

{{% div_slide "ステップ2" normal %}}
![](../img/t_slide12.png)

「精度」を選択すると、さらに詳細な評価を見ることができます。
さまざまな観点での予測精度の評価値や、予測精度に関する表やグラフが生成されます。下にスクロールすることで、閲覧できます。
{{% /div_slide %}}

{{% div_slide "ステップ3" normal %}}
![](../img/t_slide13.png)

予測精度が高いことはわかりました。では、なぜ予測精度が高いのでしょうか。
「寄与度」をクリックしてください。
{{% /div_slide %}}

{{% div_slide "ステップ4" normal %}}
![](../img/t_slide14.png)

「顧客ランク」が有効で、さらに右側の内容から
「プラチナ」だと購入しやすい等がわかります。
次に「予測する」をクリックしてください。
{{% /div_slide %}}
