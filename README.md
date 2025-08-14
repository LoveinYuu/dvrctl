# dvrctl - DaVinci Resolve Control Package

[![PyPI](https://img.shields.io/pypi/v/dvrctl.svg)](https://pypi.org/project/dvrctl/)
[![Python](https://img.shields.io/pypi/pyversions/dvrctl.svg)](https://pypi.org/project/dvrctl/)
[![Downloads](https://img.shields.io/pypi/dm/dvrctl.svg)](https://pypi.org/project/dvrctl/)
[![GitHub stars](https://img.shields.io/github/stars/LoveinYuu/dvrctl.svg?style=social)](https://github.com/LoveinYuu/dvrctl)
[![License: All Rights Reserved](https://img.shields.io/badge/License-All%20Rights%20Reserved-red.svg)](LICENSE)

> 一个用于控制和自动化 DaVinci Resolve 的 Python 库。

---
## 快速开始

```bash
pip install dvrctl
```

```python
import dvrctl

# 连接到本地运行的 DaVinci Resolve
dvr = dvrctl.GetResolve()

# 示例：切换到导出页面并退出
dvr.OpenPage('Deliver')  # 官方 API 方法
dvr.Quit()               # 官方 API 方法
```

---

## 功能概览
获取项目管理、项目操作、媒体存储、媒体池、时间线、通用工具、渲染输出等功能模块。

| 模块                  | 示例方法            | 说明       |
|---------------------|-----------------|----------|
| **Project Manager** | `dvr.pjm()`     | 获取项目管理器  |
| **Project**         | `dvr.pj()`      | 获取项目     |
| **Media Storage**   | `dvr.mds()`     | 获取媒体存储   |
| **Media Pool**      | `dvr.mdp()`     | 获取媒体池    |
| **Timeline**        | `dvr.tl()`      | 获取时间线    |
| **General**         | `dvr.general()` | 使用通用工具   |
| **Deliver**         | `dvr.deliver()` | 使用渲染输出功能 |
其他方法示例

| 模块                  | 示例方法                                       | 说明           |
|---------------------|--------------------------------------------|--------------|
| **Project Manager** | `pjm.CreateProject("MyProj")`              | 创建新项目        |
| **Project**         | `pj.save_project()`                        | 保存当前项目（自建方法） |
| **Media Storage**   | `mds.GetMountedVolumeList()`               | 获取挂载卷        |
| **Media Pool**      | `mdp.GetRootFolder()`                      | 获取根文件夹       |
| **Timeline**        | `tl.lock_track('video', 1, True)`          | 锁定轨道（自建方法）   |
| **General**         | `general.frames2tc(86400)`                 | 帧数转时间码（自建方法） |
| **Deliver**         | `deliver.add_to_render("Preset1", "/out")` | 添加渲染任务（自建方法） |

---

## 安装要求

* Python **3.5+**
* DaVinci Resolve **19+**（建议 19.1 及以上，需 Studio 版本）
* 确保设置了 DaVinci Resolve 的脚本环境变量

<details>
<summary>环境变量配置（点击展开）</summary>

**macOS**

```bash
export RESOLVE_SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
export RESOLVE_SCRIPT_LIB="/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
export PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"
```

**Windows**

```powershell
setx RESOLVE_SCRIPT_API "C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting"
setx RESOLVE_SCRIPT_LIB "C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll"
setx PYTHONPATH "%PYTHONPATH%;%RESOLVE_SCRIPT_API%\Modules\"
```

**Linux**

```bash
export RESOLVE_SCRIPT_API="/opt/resolve/Developer/Scripting"
export RESOLVE_SCRIPT_LIB="/opt/resolve/libs/Fusion/fusionscript.so"
export PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"
# 部分发行版路径可能需要改为 /home/resolve
```

</details>

---

## 使用示例

### 项目管理

```python
pjm = dvr.pjm()
pjm.CreateProject("projectName")  # 官方 API 方法
```

### 项目操作

```python
pj = dvr.pj()
pj.save_project()  # 自建方法
```

### 时间线

```python
tl = dvr.tl()
tl.GetName()                     # 官方API方法
tl.lock_track('video', 1, True)  # 自建方法
tl.lock_tracks('audio', True)    # 自建方法
tl.delete_track('video', 1, 5)   # 自建方法，删除1-5的轨道，最后参数可省略
tl.delete_tracks('video')        # 自建方法
tl.append_to_timeline(MediaPoolItem, media_type=1,
                                     track_index=1,
                                     start_tc='00:01:00:00',
                                     end_tc='00:02:00:00',
                                     record_tc='01:00:00:00', )  # 自建方法，除MediaPoolItem参数可省略
```

### 渲染输出

```python
dvr.deliver().add_to_render("Preset1", "/path/to/output")  # 自建方法
```

---

## 功能特性

* **面向对象接口**：简化 DaVinci Resolve API 调用
* **自动连接**：一行代码连接 Resolve
* **时间码工具**：帧数与时间码互转
* **轨道控制**：锁定/删除轨道更方便
* **媒体操作**：快速向时间线添加媒体
* **渲染管理**：简化渲染预设和任务添加

---

## 注意事项

* 使用此库前需确保 **DaVinci Resolve 正在运行**
* 需要 **Studio 版本** 才能使用脚本功能
* 部分功能依赖特定 DaVinci Resolve 版本

---

## 更新日志

### 0.1.0

* 重构项目结构
* 新增说明文档
* 简化代码

### 0.0.1

* 从个人项目发布为开源软件

---

## 版权说明
因还是测试阶段，请勿在不了解的情况下使用。

版权所有 © 2025 LoveinYuu
保留所有权利（All Rights Reserved）。


未经版权人明确书面许可，禁止复制、修改、分发、再授权或其他任何使用行为。

如需使用或获取许可，请联系：
**Email:** \[purewhite820@gmail.com]