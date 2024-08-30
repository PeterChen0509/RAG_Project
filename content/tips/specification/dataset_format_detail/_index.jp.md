---
title: "データセットのより詳細な仕様"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 2
draft: false
# metaタグのパラメータ
meta:
  description: "Prediction Oneで使用できるデータのフォーマットや欠損値の扱いについて説明します。"
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: false
# 検索でヒットする文字列の指定
keywords:
  ["データセット", "タイムスタンプ", "フォーマット", "yymmdd", "サイズ", "上限"]
---

### 二値分類・多値分類用データセット作成時の注意点

Prediction One では、ファイルの先頭{{% t_read_row_num %}}行を読み込んで予測したい項目の値が何種類あるのかを判定します(上記の例だと「継続」と「退会」の 2 種類) 。予測したい項目が文字列の場合、判定されたユニーク数によって二値分類か多値分類かの判定を行います。
二値分類を実行したい場合、<u>先頭{{% t_read_row_num %}}行に予測したい項目の値が 2 種類出現するようにしてください</u>。多値分類を実行したい場合、先頭{{% t_read_row_num %}}行に予測したい項目の値が３種類以上出現するように並び替えておいてください。また、<u>{{% t_mul_max_class %}}種類を超える分類には対応していません</u>のでご注意ください。

### 欠損値の扱い

欠損値とは、<u>記録が取れていないデータ</u>を指します。
欠損値がある場合は、空文字を利用してください。

### 学習用データのサイズ

100 行～ 100 万行、2 列～ 999 列の学習用データを用意してください。時系列予測モードの場合は、20 行～ 1 万行、2 列～ 200 列の学習用データを用意してください。データ結合を利用する場合は、学習用データと関連データの合計の列数が 200 列以内になるように学習用データを用意して下さい。

行数や列数が増えるほど、学習にかかる時間・メモリ使用量は増加します。メモリ使用量がお使いの PC の容量を超えるとソフトウェアが終了する場合があります。

{{% a_id "timestamp-format" %}}

### 日時フォーマット

データタイプが日時の項目は以下のフォーマットで用意してください。日時は 1970 年 1 月 1 日 0 時 0 分から 3999 年 12 月 31 日 23 時 59 分までが利用可能です。秒のデータはあってもよいですが、Prediction One では利用されません。(y=年, M=月, d=日, H=時, m=分, s=秒)

- `yyyy-MM-dd HH:mm:ss`
- `yyyy-MM-dd HH:mm`
- `yyyy-MM-dd H:mm:ss`
- `yyyy-MM-dd H:mm`
- `yyyy-MM-dd`
- `yyyy-MM-d HH:mm:ss`
- `yyyy-MM-d HH:mm`
- `yyyy-MM-d H:mm:ss`
- `yyyy-MM-d H:mm`
- `yyyy-MM-d`
- `yyyy-M-dd HH:mm:ss`
- `yyyy-M-dd HH:mm`
- `yyyy-M-dd H:mm:ss`
- `yyyy-M-dd H:mm`
- `yyyy-M-dd`
- `yyyy-M-d HH:mm:ss`
- `yyyy-M-d HH:mm`
- `yyyy-M-d H:mm:ss`
- `yyyy-M-d H:mm`
- `yyyy-M-d yyyy/MM/dd HH:mm:ss`
- `yyyy/MM/dd HH:mm`
- `yyyy/MM/dd H:mm:ss`
- `yyyy/MM/dd H:mm`
- `yyyy/MM/dd`
- `yyyy/MM/d HH:mm:ss`
- `yyyy/MM/d HH:mm`
- `yyyy/MM/d H:mm:ss`
- `yyyy/MM/d H:mm`
- `yyyy/MM/d`
- `yyyy/M/dd HH:mm:ss`
- `yyyy/M/dd HH:mm`
- `yyyy/M/dd H:mm:ss`
- `yyyy/M/dd H:mm`
- `yyyy/M/dd`
- `yyyy/M/d HH:mm:ss`
- `yyyy/M/d HH:mm`
- `yyyy/M/d H:mm:ss`
- `yyyy/M/d H:mm`
- `yyyy/M/d`
- `yyyy-MM`
- `yyyy-M`
- `yyyyMMdd`
- `yyyyMM`
- `dd-MM-yyyy`
- `dd-M-yyyy`
- `d-MM-yyyy`
- `d-M-yyyy`
- `yyyy`
- `mmm-yy` (`mmm`は月名が英語の省略形で表現される形式です。例えば、`Jan-21`は`2021年1月`を表します。この形式の場合、現在の年月が`yyyy年mm月`のとき、`(yyyy-80)年(mm+1)月～(yyyy+20)年(mm)月`以内、かつ、`1970年1月～3999年12月`以内、のデータのみ利用可能です。)
