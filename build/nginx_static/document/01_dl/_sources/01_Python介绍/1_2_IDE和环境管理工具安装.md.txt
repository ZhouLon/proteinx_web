# 1_2_IDE和环境管理工具安装

**作者**: ZhouLong<br>
**创建日期**: 2026 年 01 月 10 日<br>
**版本**: 1.0<br>

<div style="display: flex; justify-content: space-between; padding: 15px 0; margin: 20px 0; border-top: 1px solid #eaeaea; border-bottom: 1px solid #eaeaea;">
    <a href="./1_1_什么是Python.html" style="text-decoration: none; color: #0366d6; padding: 8px 15px; border: 1px solid #e1e4e8; border-radius: 5px;">👈 上一页</a>
    <a href="../index.html" style="text-decoration: none; color: #0366d6; padding: 8px 15px; border: 1px solid #e1e4e8; border-radius: 5px;">🏠 首页</a>
    <a href="./1_3_基础语法与数据类型.html" style="text-decoration: none; color: #0366d6; padding: 8px 15px; border: 1px solid #e1e4e8; border-radius: 5px;">下一页 👉</a>
</div>

## 1. 简介

欢迎来到Python安装篇！本篇会介绍 **Python解释器，IDE和环境管理工具**，最后手把手带你完成Python环境的搭建，让你的计算机真正具备运行Python程序的能力。

<div class="admonition tip">
<p class="admonition-title"><b>建议</b></p>
<p>注意后续安装任何程序，安装路径上不要出现中文</p>
</div>

### **为什么需要安装Python解释器？**
上一篇我们提到，Python是解释型语言，代码需要解释器逐行"翻译"成计算机能理解的指令才能执行。因此，安装Python解释器是我们学习Python的第一步。当前Python解释器其实有多种实现：
- **CPython（官方版本）**：使用C语言编写，是最广泛使用的版本，我们通常说的"Python"就是指它
- **PyPy**：使用Python自身实现，采用JIT（即时编译）技术，某些场景下速度更快
- **Jython**：运行在Java虚拟机上的Python
- **IronPython**：针对.NET平台的实现

<div class="admonition tip">
<p class="admonition-title"><b>建议</b></p>
<p>对于初学者，我们<b>强烈推荐使用官方的CPython</b>,也就是大家默认所谓的Python 。它最稳定、生态最完善、文档最齐全，几乎所有教程和第三方库都以它为基准。</p>
</div>

### **什么是IDE？为什么需要它？**
* 有了解释器，理论上我们就能运行Python代码了，但我们不可能直接使用记事本写代码，其效率太低。这时就需要**集成开发环境（IDE，Integrated Development Environment）**。
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/ides.png" 
         alt="IDE" 
         style="display: block; margin: 20px auto; width: 60%; max-width: 500px;">
</div>

上图是各种各样的IDE。使用IDE能让编程效率提升数倍，尤其对初学者来说，好的IDE能大大降低学习门槛。IDE就像程序员的工作台，它集成了：
- **代码编辑器**：提供语法高亮、智能提示、自动补全
- **调试工具****：让找bug变得像侦探破案一样直观
- **项目管理**：轻松管理多个文件和依赖
- **版本控制集成**：直接连接Git等工具
- **终端集成**：无需切换窗口就能运行命令

目前主流的Python IDE有：
- **IDLE（入门选手）**：Python自带的简易IDE，适合快速测试小段代码（不推荐使用）。
- **PyCharm（专业选手）**：JetBrains出品，功能极其强大。专业版收费；社区版免费，但一些专业功能被阉割。新手推荐使用。
- **VS Code（全能选手）**：微软出品，免费开源，通过插件可支持几乎所有编程语言。轻量快速，生态丰富。适合进阶选手。
- **Jupyter Notebook**：交互式笔记本，可以可视化交互地运行Python脚本。

<div class="admonition tip">
<p class="admonition-title"><b>建议</b></p>
<p>我们推荐从<b>VS Code</b>开始。VS Code有优秀的Python插件、完全免费、跨平台，而且学会使用它后，你未来学习其他语言（如JavaScript、Java、Go等）也无需更换工具，一举多得。</p>
</div>

### **为什么需要环境管理工具？**
Python的生态系统极其丰富，但这也带来了一个挑战：**依赖冲突**。想象一下，你正在开发项目A，需要Python 3.8和Pandas 1.5；同时，项目B则需要Python 3.11和Pandas 2.0。如果系统只有一个Python环境，这两个项目的要求就会“打架”，导致其中一个无法正常运行。

<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/env_mg.png" 
         alt="环境管理工具" 
         style="display: block; margin: 20px auto; width: 60%; max-width: 500px;">
</div>

上图展示了几个常见的环境管理工具。环境管理工具的核心价值是——**为每个项目创建独立、隔离的工作空间**。每个工作空间里，你可以安装指定版本的Python解释器和第三方库，而不会影响其他工作空间里项目。目前主流的工具包括：
- **venv / virtualenv**：Python官方或社区提供的轻量级环境管理工具，主要管理Python包（Pycharm IDE中常用）。
- **Conda / Miniconda**：**功能强大的环境与包管理器**，不仅能管理Python包，还能管理Python解释器本身以及R、C++库等非Python依赖。
- **Mamba**：Conda的C++重写版本，使用libsolv进行依赖解析，在安装和更新包时比原版Conda**快数倍**，命令与Conda完全兼容，适合处理复杂依赖关系的大型环境。
- **Poetry**：现代化的Python项目管理和打包工具，统一管理项目依赖、虚拟环境和打包发布，使用`pyproject.toml`替代传统的`requirements.txt`，解决依赖版本锁定问题。
- **uv**：由Astral团队（Ruff的创造者）开发的高性能Python包安装器和解析器，速度极快，兼容`pip`和`pip-tools`工作流，适合需要快速安装依赖的大型项目。
- **Pipenv**：曾被誉为“Python官方推荐的包管理器”，集成了虚拟环境和包管理功能，使用`Pipfile`和`Pipfile.lock`来管理依赖。


<div class="admonition tip">
<p class="admonition-title"><b>建议</b></p>
<p>我们推荐直接安装<b>Miniconda</b>它相比庞大的Anaconda更加轻量，但同样具备Conda的核心环境管理能力。其对于大多数场景已经够用。安装Miniconda后，你无需再去官网单独下载Python解释器。</p>
</div>

## 2. 安装流程

接下来，让我们进入实际操作环节。安装分为两大步：
1. **安装VS Code IDE** 
2. **安装Miniconda 环境管理工具**



### 2.1 安装VS Code IDE
该部分文档参考<a href="https://blog.csdn.net/weixin_60915103/article/details/131617196?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522217d3b942f0e576ea291137f1a92af39%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=217d3b942f0e576ea291137f1a92af39&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-131617196-null-null.142^v102^pc_search_result_base7&utm_term=vscode&spm=1018.2226.3001.4187" target="_blank" >《vscode安装+配置+使用+调试【保姆级教程】》</a>
#### 访问官网
首先进入到<a href="https://code.visualstudio.com/" target="_blank" >VScode</a>的官网，选择自己电脑适配的版本（例子中使用Windows版本），下载时可以使用梯子进行加速。
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/vs_home.png" 
         alt="vscode主页" 
         style="display: block; margin: 20px auto; width: 80%; max-width: 1000px;">
</div>
<div align="center"><b>vscode主页</b></div>

#### 运行安装exe
根据图片操作
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/vs_1.png" 
         alt="vs1" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

#### 选择安装路径
不要安装到C盘。<b>注意安装路径不能有中文</b>
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/vs_2.png" 
         alt="vs2" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

根据图片操作
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/vs_3.png" 
         alt="vs3" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

#### 选择附加服务
根据图片操作
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/vs_4.png" 
         alt="vs4" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

#### 重启
最后跳出安装完成的界面就说明安装的步骤全部结束！ <b>记得重启</b>
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/vs_5.png" 
         alt="vs5" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>



#### 创建工作区文件夹
**下面简单进行vscode的使用。**<br>
首先在Windows自带的文件资源管理器中创建一个总项目文件夹PyProjects（名字随意，<b>注意不能是中文</b>）。再在总项目文件夹下新建一个文件夹test（命名规则同），后续这个文件夹会作为一个项目，有关该项目的文件都放置在该文件夹下。
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/new_folder.png" 
         alt="new_folder" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

#### vscode界面展示
打开vscode（这里显示的是英文版，按照个人习惯可以改成中文）。Vscode的界面如下图，左侧栏是一些常见的工具栏，上车是一些设置选项。我们首先选择左侧工具栏的资源管理器，然后点击Open Folder（打开文件夹）。
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/vs_face.png" 
         alt="vs_face" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

#### 选择工作区
选择刚刚创建的test目录。
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/select_folder.png" 
         alt="select_folder" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

#### 创建终端
点击上方三个点的按钮，新建一个终端(Terminal)，看到vscode下方显示TERMINAL，其中显示 `PS D:\PyProjects\test>` 即代表终端创建成功（PS就是代表PowerShell的意思）。
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/open_terminal.png" 
         alt="open_terminal" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

**大功告成！**

### 2.2 安装Miniconda

Miniconda的下载官网<a href="https://www.anaconda.com/docs/getting-started/miniconda/install" target="_blank" >点击这里</a>。
#### 进入官网
跳转到Minicoda的官网，找到Basic install instruction，点开Windows installation的下载。
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/minconda_download.png" 
         alt="minconda_download" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

#### 新建下载目录
回到vscode中，在刚刚的test目录下新建一个名为Downloads的目录（目录就是文件夹的意思），方便下一步文件的下载。
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/mkdir_download.png" 
         alt="mkdir_download" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

#### 复制下载源码
在Minicoda的官网复制Windows中的powershell选项的下载代码。
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/copy_code.png" 
         alt="copy_code" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

把复制的下载代码输入到Terminal中。
```
Invoke-WebRequest -Uri "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -outfile ".\Downloads\Miniconda3-latest-Windows-x86_64.exe"
```
`nvoke-WebRequest`是Windows的PowerShell中的一个命令，主要用于发送 HTTP/HTTPS 请求，类似于 Linux 中的`curl`或`wget`。<br>
`-Uri `参数代表从后面的网址获取资源。<br>
`-outfile`是文件下载的指定路径。`.\Downloads\Miniconda3-latest-Windows-x86_64.exe`
代表在我们刚刚创建的`Downloads`下载文件并且命名为`Miniconda3-latest-Windows-x86_64.exe`

<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/input_ps.png" 
         alt="input_ps" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

#### 下载Minicoda
按回车Enter运行，可以看到正在下载文件到目标文件夹
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/downloading_minicoda.png" 
         alt="downloading_minicoda" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

无报错，则下载成功
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/downloaded_minicoda.png" 
         alt="downloaded_minicoda" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

你已经使用 `Invoke-WebRequest` **成功下载了** Miniconda 安装程序，接下来需要**运行安装程序**进行安装。

#### 安装
转到下载目录
```powershell
cd .\Downloads\
```

运行安装程序，/S 代表静默安装 /AddToPath=1 代表添加到系统路径 /RegisterPython=1 代表注册为系统默认Python /D=%USERPROFILE%\Miniconda3 代表指定安装目录
```powershell
.\Miniconda3-latest-Windows-x86_64.exe /S /InstallationType=JustMe /AddToPath=1 /RegisterPython=1 /D=%USERPROFILE%\Miniconda3
```

会出现如下
```powershell
PS D:\PyProjects\test\Downloads> .\Miniconda3-latest-Windows-x86_64.exe /S /InstallationType=JustMe /AddToPath=1 /RegisterPython=1 /D=%USERPROFILE%\Miniconda3        
PS D:\PyProjects\test\Downloads> Welcome to Miniconda3 py313_25.11.1-1
By continuing this installation you are accepting this license agreement:
C:\Users\xxx\miniconda3\EULA.txt
Please run the installer in GUI mode to read the details.
Miniconda3 will now be installed into this location:
C:\Users\xxx\miniconda3
Unpacking payload...
Setting up the package cache...
Setting up the base environment...
Installing packages for base, creating shortcuts if necessary...
Preparing transaction:
...working...
done
Executing transaction:
...working...
done
Adding C:\Users\xxx\miniconda3\Scripts & Library\bin to PATH...
Setting installation directory permissions...
#�ѳɹ����� 30489 ���ļ�; ���� 0 ���ļ�ʱʧ��
Done!
```

#### 初始化
按下`ctrl+c`中断，随后进入初始化脚本的目录
```
cd "$env:USERPROFILE\Miniconda3\Scripts"
```

输入初始化命令
```powershell
conda init powershell
```

#### 测试运行
新建一个终端，在PS前出现(base)，即代表安装成功！
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/base_appear.png" 
         alt="base_appear" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

输入`conda`测试是否可以正常运行
```powershell
#不需要复制运行，展示运作流程
(base) PS D:\PyProjects\test> conda
usage: conda-script.py [-h] [-v] [--no-plugins] [-V] COMMAND ...
conda is a tool for managing and deploying applications, environments and packages.
options:
  -h, --help            Show this help message and exit.
  -v, --verbose         Can be used multiple times. Once for detailed output,
                        twice for INFO logging, thrice for DEBUG logging, four
                        times for TRACE logging.
  --no-plugins          Disable all plugins that are not built into conda.
  -V, --version         Show the conda version number and exit.
................
#过多行不展示，出现上述内容，代表conda正常运行
```

#### 创建虚拟环境
接下来创建一个名为test的，python版本为3.10的虚拟环境
```powershell
conda create -n test python=3.10
```

```powershell
#不需要复制运行，展示注意下面的选项都选择接受(a)
Do you accept the Terms of Service (ToS) for https://repo.anaconda.com/pkgs/main? 
[(a)ccept/(r)eject/(v)iew]:a
```
#### 激活虚拟环境
激活创建好的虚拟环境
```powershell
conda activate test
```

出现test前缀成功进入了名为test虚拟环境
```powershell
#不需要复制运行，展示前缀发生变化
(base) PS D:\PyProjects\test> conda activate test
(test) PS D:\PyProjects\test>
```

#### 在虚拟环境中运行python代码
接下来测试是否能在虚拟环境中执行python代码。<br>
删除刚刚的Downloads目录，然后在test目录下新建一个名为test.py的python脚本文件,打开后，编写代码.
```python
print("hello world")
```
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/code_test.png" 
         alt="code_test" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

ctrl+s保存文件，然后在终端中复制运行下述代码，得到结果如图
```python
python .\test.py
```
<div style="margin: 20px 0; text-align: center;">
    <img src="../_static/figures/1/hello_world.png" 
         alt="hello_world" 
         style="display: block; margin: 20px auto; width: 90%; max-width: 1000px;">
</div>

**出现hello world代表大功告成！！！**


<div style="display: flex; justify-content: space-between; padding: 15px 0; margin: 20px 0; border-top: 1px solid #eaeaea; border-bottom: 1px solid #eaeaea;">
    <a href="./1_1_什么是Python.html" style="text-decoration: none; color: #0366d6; padding: 8px 15px; border: 1px solid #e1e4e8; border-radius: 5px;">👈 上一页</a>
    <a href="../index.html" style="text-decoration: none; color: #0366d6; padding: 8px 15px; border: 1px solid #e1e4e8; border-radius: 5px;">🏠 首页</a>
    <a href="./1_3_基础语法与数据类型.html" style="text-decoration: none; color: #0366d6; padding: 8px 15px; border: 1px solid #e1e4e8; border-radius: 5px;">下一页 👉</a>
</div>
