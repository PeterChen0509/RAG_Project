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
{{% /div_slide %}}

{{% div_slide "ステップ2" normal %}}
![](../img/t_slide12.png)

「精度」を選択すると、さらに詳細な評価を見ることができます。
さまざまな観点での予測精度の評価値や、予測精度に関する表やグラフが生成されます。下にスクロールすることで、閲覧できます。
{{% /div_slide %}}

{{% div_slide "ステップ3" normal %}}
![](../img/t_slide13.png)

予測精度の値はわかりました。では、「寄与度」をクリックしてください。
{{% /div_slide %}}

{{% div_slide "ステップ4" normal %}}
![](../img/t_slide14.png)

今回作成した予測モデルでは、「収縮期血圧(mmHg)」を有効な項目として捉えており、さらに右側の内容から
「収縮期血圧(mmHg)の数値が高い場合」だと、モデルが罹患確率をより高く予測する傾向にあること等がわかります。
次に「予測する」をクリックしてください。
{{% /div_slide %}}
