---
title: "予測寄与度の読み解き方と活用方法（多値分類）"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 6
draft: false
# metaタグのパラメータ
meta:
  description: "予測分析ツールPrediction Oneでは、何が予測結果に影響しているかを簡単に見ることができます。ここでは、Prediction Oneで見ることができる予測寄与度の概要について説明しています。（多値分類）"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords: ["寄与度", "予測寄与度", "意味", "見方", "重要度", "importance", "多値分類"]
---

{{% div_slide "はじめに" normal first-page %}}
予測寄与度を正しく読むことができると、予測モデルの改善や業務施策の立案に活用することができます。

ここでは、多値分類の寄与度の読み解き方のポイントや活用方法を紹介します。
{{% /div_slide %}}

{{% div_slide "使用するデータ" normal %}}
レビュー文に対してどの苦情タイプを割り当てればよいかを予測するためのデータセットを元に、予測寄与度の読み解き方とその活用方法を説明します。<br/>
このサンプルデータセットは、「データ」→「サンプル」タブのデータ一覧から取得可能です。<br/>

![](img/t_slide2.png)
{{% /div_slide %}}

{{% div_slide "ステップ１: 寄与度の項目を確認する" normal %}}
まず、寄与度の合計の大きい順に、項目を確認しましょう。<br/>
「ご自身の考える項目の影響の強さと寄与度の大きさが一致するか」「想定外のところはあるか」をポイントに確認します。<br/>

![](img/t_slide3.png)
{{% /div_slide %}}

{{% div_slide "ステップ２：寄与度の構成する要素を確認する" normal %}}
それぞれの寄与度の項目をクリックして、寄与度を構成する要素を確認していきます。<br/>

![](img/t_slide4.png)

気になる項目をクリックすると、各クラス（苦情タイプ）が選べるようになっており、それぞれのクラスに寄与する項目内容（この場合、テキストに含まれる単語）を見ることができます。<br/>
これが、ご自身の経験や直感と合っているかを確認しましょう。<br/>

確率を上げている項目・下げている項目は以下の□部分で確認できます。<br/>

![](img/t_slide5.png)

また、右上のフィルターボタンを押すことで、そのクラスに絞った項目内容を確認できます。「並び替え」のプルダウンからも同じ絞り込み操作が可能です。

![](img/t_slide6.png)

ここで、ご自身が寄与が高いと思っていた項目が低かったり、逆に、寄与が低いと思っていた項目が高い場合は、使用すべきデータを間違ってしまっている可能性があります。まずデータを見直してみましょう。<br/>
データを見直し、間違っていなかった場合、以下のような気付きが考えられます。<br/>
・思わぬ項目が予測へ寄与している<br/>
・思っていた項目が予測へ寄与していない<br/>
ここから、ビジネス上に重要なインサイトが得られる可能性があります。<br/>
{{% /div_slide %}}

{{% div_slide "ステップ３：インサイトから施策が打てるか検討する" normal %}}
今回の、顧客の声のラベリングを行う分類モデルを作成したときに明らかになった寄与度を用いて、施策立案を行った場合は以下のような例が考えられます。<br/>

例えば「(a)外見」に寄与する単語の一つに「通販」があります。仮に、この製品が店舗と通販サイトの両方で販売されていた場合、通販サイト経由での販売時に外見に関する苦情が相対的に発生しやすくなるのではないかと推測されます。<br/>
![](img/t_slide7.png)

そこで、「(a)外見」に関する苦情を減らすための施策を検討するときに、通販サイトで販売される商品の梱包、配送などの手順を見直すといったことが効果的なのではないか、と考えることができます。<br/>

また、「(c)バッテリー」の寄与度に注目する場合、最も寄与度の大きい単語は「無くなる」となっています。
![](img/t_slide8.png)

これは、バッテリーに関する意見の中でも、バッテリー切れの場合に課題を抱えているユーザが多いことを示唆しています。<br/>
バッテリーに関するネガティブな意見を減らすためのアクションとして、バッテリー切れ時の対応をマニュアル内の顧客の目の付きやすい場所に分かりやすく記載したり、次期製品開発時にバッテリー消費を抑える仕組みを検討したりする、といったものが挙げられます。<br/>
以上の例のように、予測結果をラベリング自動化に用いるだけでなく、寄与度を将来のビジネスに繋がる施策立案に活用することができます。<br/>
{{% /div_slide %}}
