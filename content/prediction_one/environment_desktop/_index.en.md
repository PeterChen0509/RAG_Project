---
title: "Operating Environment (Desktop version)"
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
    "Environment",
    "Spec",
    "NET",
    "OS",
    "Spec",
    "User permission",
    "Administrative permission",
    "Cannot install",
    "As an administrator",
    "Workspace",
  ]
---

### OS

Prediction One has the following system requirements:

- Windows 10 (64-bit)
- Windows 11 (64-bit)
- Windows Server 2019

The OS must have the latest Windows updates, the OS must be within its support period, and the system time must be set correctly.

Prediction One requires administrator privileges only when installing. We recommend that you start with user permissions. (It is also available with administrator privileges, but there may be restrictions such as not being able to drag and drop, not being able to take over the workspace/license, etc.)

You also need to have either PowerShell 5.1 or later (when using Windows 11 or Windows Server 2019) or PowerShell 5.0 or later (when using Windows 10) installed and be able to execute the PowerShell script (.ps1) with the administrator privileges used when installing Prediction One.

In addition, you must install the following software. If you have already installed it, you do not need to install it again.

- Microsoft Visual C++ Redistributable Package for Visual Studio 2019
- Microsoft .NET Framework 4.7.2

Microsoft Visual C++ Redistributable Package for Visual Studio 2019 is included with the Prediction One installer and will be installed at the same time if it is not already installed.

You may need to download and install "Microsoft.NET Framework 4.7.2" from the link below.

{{% a_out "https://support.microsoft.com/ja-jp/help/4054530/microsoft-net-framework-4-7-2-offline-installer-for-windows" "Microsoft .NET Framework 4.7.2 Offline Installer for Windows" %}}

### Recommended Computer Specifications

The recommended environments for Prediction One are:

- Memory: 8GB RAM
- CPU: 3.0GHz
- HDD・SSD: At least 50GB free

### File Placement

The files and workspaces of Prediction One are located in the following folders:

<table>
    <tr>
        <td>File Types</td>
        <td>Path</td>
    </tr>
    <tr>
        <td>Executable File (GUI)</td>
        <td>{{< preone_home_path_abs_bs >}}\PredictionOne.exe</td>
    </tr>
    <tr>
        <td>Executable (Command Line)</td>
        <td>{{< preone_home_path_abs_bs >}}\PredictionOneCmd.exe</td>
    </tr>
    <tr>
        <td>Manual</td>
        <td>C:\Users\[User Name]\AppData\Local\Sony Corporation\Prediction One\Doc\index.html</td>
    </tr>
    <tr>
        <td>Workspace</td>
        <td>C:\Users[User Name]\AppData\Local\Sony Corporation\Prediction One\WorkSpace</td>
    </tr>
    <tr>
        <td>Sample Data</td>
        <td>{{< preone_home_path_abs_bs >}}\en-US\doc\sample_dataset\use_case\</td>
    </tr>
</table>
