---
title: "動作環境（デスクトップ版）"
date: 2018-12-29T11:02:05+06:00
lastmod: 2020-01-05T10:42:26+06:00
weight: 900 # 下から2番目に表示する
draft: false
# metaタグのパラメータ
meta:
  description: ""
# クラウド・デスクトップ限定ページの場合は片方のみtrueにする
visible:
  is_cloud_only: false
  is_desktop_only: true
# 検索でヒットする文字列の指定
keywords:
  [
    "Windows",
    "Mac",
    "環境",
    "スペック",
    "NET",
    "OS",
    "スペック",
    "ユーザー権限",
    "管理者権限",
    "インストールできない",
    "管理者として",
    "ワークスペース",
  ]
---

### OS

Prediction One の動作環境は以下の通りです。

- Windows 10 (64 ビット版)
- Windows 11 (64 ビット版)
- Windows Server 2019

OS は最新の Windows Update が適用されていて、OS 自体がサポート期限内であり、システム時刻が正しく設定されている必要があります。

Prediction One はインストール時のみ管理者権限が必要です。利用時はユーザー権限での起動を推奨します。(管理者権限でも利用可能ですが、ドラッグ&ドロップができない・{{< dist_type_select "SNC" "ワークスペース/ライセンス" "ワークスペース">}}が引き継げない、などの制約が発生することがあります。)

また、PowerShell 5.1以降(Windows 11/Windows Server 2019の場合)またはPowerShell 5.0以降(Windows 10の場合)がインストールされていて、Prediction Oneをインストールするときの管理者権限でPowerShell スクリプト(.ps1)が実行できる必要があります。

さらに、以下のソフトウェアをインストールする必要があります。すでにインストール済みの場合はインストール不要です。

- Visual Studio 2019 の Microsoft Visual C++再頒布可能パッケージ
- Microsoft .NET Framework 4.7.2

「Visual Studio 2019 の Microsoft Visual C++ 再頒布可能パッケージ」については、Prediction One のインストーラーに同封されており、インストールされていない場合は同時にインストールされます。

「Microsoft .NET Framework 4.7.2」については、以下のリンク先からダウンロードおよびインストールが必要な場合があります。

{{% a_out "https://support.microsoft.com/ja-jp/help/4054530/microsoft-net-framework-4-7-2-offline-installer-for-windows" "Windows 用の Microsoft .NET Framework 4.7.2 オフライン インストーラー" %}}

### 推奨スペック

Prediction One の推奨環境は以下の通りです。

- メモリ：8GB 以上
- CPU：3.0GHz 以上
- HDD・SSD：50GB 以上の空き

### ファイル配置

Prediction One の各種ファイル、ワークスペースは以下のフォルダーに配置されています。

<table>
    <tr>
        <td>ファイルの種類</td>
        <td>パス</td>
    </tr>
    <tr>
        <td>実行ファイル (GUI)</td>
        <td>{{< preone_home_path_abs_bs >}}\PredictionOne.exe</td>
    </tr>
    <tr>
        <td>実行ファイル (コマンドライン)</td>
        <td>{{< preone_home_path_abs_bs >}}\PredictionOneCmd.exe</td>
    </tr>
    <tr>
        <td>マニュアル</td>
        <td>C:\Users\[ユーザー名]\AppData\Local\Sony Corporation\Prediction One\Doc\index.html</td>
    </tr>
    <tr>
        <td>ワークスペース</td>
        <td>C:\Users\[ユーザー名]\AppData\Local\Sony Corporation\Prediction One\WorkSpace</td>
    </tr>
    <tr>
        <td>サンプルデータ</td>
        <td>{{< preone_home_path_abs_bs >}}\ja-JP\doc\sample_dataset\use_case\</td>
    </tr>
</table>
