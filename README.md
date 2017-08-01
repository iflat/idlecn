IDLE是一个Python自带的集成开发环境和学习环境. 它相对于  
标准IDE环境来说相对简单，但一个IDE必备的功能已基本具备，  
它支持语法高亮、自动完成、调用方法提示及基本的代码调试。  
这对于Python的初学者来说足以，为便于初学者使用，用了一  
下午时间将主要部分进行了汉化，并在GitHub分享一下。  

以下内容来自IDLE自身的说明文档，主要是对各个文件的内容做  
了简要的介绍和说明。本说明文档是为IDLE开发人员和那些充满  
好奇心的用户准备的.更详细的说明可在IDLE中使用「帮助」--  
「IDLE 帮助」进行查看.  

IDLELIB模块文件列表以字母排序分类，并有简短说明.

本文件是一个描述性的说明，而不是详细的规范文档，文件中可  
能存在错误和疏漏，模块文件中可能有更详细的说明.

IDLELIB模块文件  
与菜单项目没有关联的实现模块文件在列表中有标记(nim).  
相对独立的文件和对象在列表的末尾单独列出.

启动文件  
————————————  
__init__.py  # 完成导入工作, 其它什么也没做  
__main__.py  # -m, 启动IDLE  
idle.bat  
idle.py  
idle.pyw

功能实现  
————————————  
autocomplete.py   # 属性名和文件名的自动完成.    
autocomplete_w.py # 自动完成功能的显示部分.  
autoexpand.py     # 标识符自动完成.  
browser.py        # 模块浏览.  
calltip_w.py      # 显示调用提示.  
calltips.py       # 创建调用提示文本.  
codecontext.py    # 在顶部分割窗口显示上下文.  
colorizer.py      # 文字着色(nim)  
config.py         # 加载和保存配置(nim).  
configdialog.py   # 显示配置对话框.  
config_help.py    # 配置帮助源对话框.  
config_key.py     # 修改绑定的快捷键.  
dynoption.py      # 选项菜单内容动态修改(nim).  
debugobj.py       # 定义堆栈查看器中使用到的类.  
debugobj_r.py     # 代码对象和系统进程通信(nim).  
debugger.py       # 命令行和编辑界面的调试器; 显示调试窗口.  
debugger_r.py     # 远程调试功能模块.  
delegator.py      # 基本的类定义和托管模块(nim).  
editor.py         # 编辑器可相关功能模块.  
filelist.py       # 文件打开和文件窗口管理模块(nim).  
grep.py           # 多文件的查找和模式匹配.  
help.py           # 显示IDLE HTML版帮助文档.  
help_about.py     # 显示IDLE关于对话框.  
history.py        # 用户输入或命令行命令历史管理(nim)  
hyperparser.py    # Parse code around a given index.  
iomenu.py         # 文件的打开, 读取, 保存  
macosx.py         # 在Macs中运行IDLE(nim).  
mainmenu.py       # 定义了主要的IDLE菜单.  
multicall.py      # 打包了tk 图形控件以允许在一个事件中能进行重复调用(nim).  
outwin.py         # 查找结果的输出窗口.  
paragraph.py      # Re-wrap multiline strings and comments.  
parenmatch.py     # 自动括号匹配: (), [], 和 {}.  
pathbrowser.py    # 创建浏览路径窗口.  
percolator.py     # 管理托管堆栈 (nim).  
pyparse.py        # 为代码缩进提供相关信息  
pyshell.py        # 启动IDLE, 管理命令行, 完成编辑窗口  
query.py          # Query user for information  
redirector.py     # 重定向控件操作(nim).  
replace.py        # 查找和替换功能.  
rpc.py            # idle和用户进程通信(nim).  
rstrip.py         # 删除冗余的空白字符.  
run.py            # 代码执行的子进程管理.  
runscript.py      # 检查和允许用户代码.  
scrolledlist.py   # 定义IDLE中的滚动条控件 (nim).  
search.py         # 文本查找和匹配.  
searchbase.py     # 查找、替换和匹配对话框的基本控件定义.  
searchengine.py   # 搜索功能.  
stackviewer.py    # 堆栈查看器.  
statusbar.py      # 窗口状态栏定义(nim).  
tabbedpages.py    # 窗口标签页定义(nim).  
textview.py       # 定义只读文本控件(nim).  
tree.py           # 定义在浏览窗口中使用的树形控件(nim).  
undo.py           # 管理撤销操作堆栈.  
windows.py        # 管理顶层窗口和窗口列表.  
zoomheight.py     # 放大窗口到屏幕最大高度.  

配置文件  
————————————  
config-extensions.def # 扩展模块配置定义  
config-highlight.def  # 色彩高亮配置定义  
config-keys.def       # 快捷键绑定定义  
config-main.def       # 字体及默认值定义  

文本文件  
————————————  
CREDITS.txt  # 在关于对话框中显示的贡献者文档  
HISTORY.txt  # 2001以前的更新历史文件  
NEWS.txt     # 版本更新文档  
README.txt   # 本说明文件  
TODO.txt     # TODO文档  
extend.txt   # 关于IDLE扩展功能模块  
help.html    # Python文档的idle.html拷贝, 可以在IDLE帮助菜单中显示  

其它目录  
————————————  
Icons        # 图标图像文件  
idle_test    # 人工和自动测试文件  

未使用和临时文件 (nim)  
————————————  
tooltip.py # 未使用


代码风格 -- PEP8  