README.txt: 这是idlelib模块文件的索引和IDLE 菜单的说明.

IDLE 是一个Python的集成开发环境和学习环境. 关于各个模块
文件的详细说明可在IDLE 中使用「帮助」--「IDLE 帮助」
进行查看.本说明文档是为IDLE开发人员和那些充满好奇心的用
户准备的.

IDLELIB模块文件列表以字母排序分类，并有简短说明.

IDLE 菜单显示菜单树形结构, 并说明了相关联的模块文件和实
现该菜单功能的相关模块对象.

本文件是一个描述性的说明，而不是详细的规范文档，文件中可
能存在错误和疏漏，模块文件中可能有更详细的说明.


IDLELIB模块文件
与菜单项目没有关联的实现模块文件在列表中有标记(nim).
相对独立的文件和对象在列表的末尾单独列出.

启动
-------
__init__.py  # 完成导入工作, 其它什么也没做
__main__.py  # -m, 启动IDLE
idle.bat
idle.py
idle.pyw

功能实现
--------------
autocomplete.py   # 属性名和文件名的自动完成.
autocomplete_w.py # 自动完成功能的显示部分.
autoexpand.py     # Expand word with previous word in file.
browser.py        # 模块浏览.
calltip_w.py      # 显示调用提示.
calltips.py       # 创建调用提示文本.
codecontext.py    # Show compound statement headers otherwise not visible.
colorizer.py      # 文字着色(nim)
config.py         # 加载和保存配置(nim).
configdialog.py   # 显示配置对话框.
config_help.py    # 配置帮助源对话框.
config_key.py     # 修改绑定的快捷键.
dynoption.py      # 选项菜单内容动态修改(nim).
debugobj.py       # 定义堆栈查看器中使用到的类.
debugobj_r.py     # Communicate objects between processes with rpc (nim).
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
redirector.py     # Intercept widget subcommands (for percolator) (nim).
replace.py        # 查找和替换功能.
rpc.py            # idle和用户进程通信(nim).
rstrip.py         # 删除冗余的空白字符.
run.py            # 代码执行的子进程管理.
runscript.py      # 检查和允许用户代码.
scrolledlist.py   # 定义IDLE中的滚动条控件 (nim).
search.py         # 文本查找和匹配.
searchbase.py     # 查找、替换和匹配对话框的基本控件定义.
searchengine.py   # Define engine for all 3 search dialogs.
stackviewer.py    # View stack after exception.
statusbar.py      # 窗口状态栏定义(nim).
tabbedpages.py    # 窗口标签页定义(nim).
textview.py       # 定义只读文本控件(nim).
tree.py           # 定义在浏览窗口中使用的树形控件(nim).
undo.py           # 管理撤销操作堆栈.
windows.py        # 管理顶层窗口和窗口列表.
zoomheight.py     # 放大窗口到屏幕最大高度.

配置文件
-------------
config-extensions.def # 扩展模块配置定义
config-highlight.def  # 色彩高亮配置定义
config-keys.def       # 快捷键绑定定义
config-main.def       # 字体及默认值定义

文本文件
----
CREDITS.txt  # 在关于对话框中显示的贡献者文档
HISTORY.txt  # 2001以前的更新历史文件
NEWS.txt     # 版本更新文档
README.txt   # 本说明文件
TODO.txt     # TODO文档
extend.txt   # 关于IDLE扩展功能模块
help.html    # Python文档的idle.html拷贝, 可以在IDLE帮助菜单中显示

其它目录
--------------
Icons        # 图标图像文件
idle_test    # 人工和自动测试文件

未使用和临时文件 (nim)
---------------------------------------------
tooltip.py # 未使用



IDLE 菜单
Top level items and most submenu items are defined in mainmenu.
Extenstions add submenu items when active.  The names given are
found, quoted, in one of these modules, paired with a '<<pseudoevent>>'.
Each pseudoevent is bound to an event handler.  Some event handlers
call another function that does the actual work.  The annotations below
are intended to at least give the module where the actual work is done.
'eEW' = editor.EditorWindow

File
  New File         # eEW.new_callback
  Open...          # iomenu.open
  Open Module      # eEw.open_module
  Recent Files
  Class Browser    # eEW.open_class_browser, browser.ClassBrowser
  Path Browser     # eEW.open_path_browser, pathbrowser
  ---
  Save             # iomenu.save
  Save As...       # iomenu.save_as
  Save Copy As...  # iomenu.save_a_copy
  ---
  Print Window     # iomenu.print_window
  ---
  Close            # eEW.close_event
  Exit             # flist.close_all_callback (bound in eEW)

Edit
  Undo             # undodelegator
  Redo             # undodelegator
  ---              # eEW.right_menu_event
  Cut              # eEW.cut
  Copy             # eEW.copy
  Paste            # eEW.past
  Select All       # eEW.select_all (+ see eEW.remove_selection)
  ---              # Next 5 items use searchengine; dialogs use searchbase
  Find             # eEW.find_event, search.SearchDialog.find
  Find Again       # eEW.find_again_event, sSD.find_again
  Find Selection   # eEW.find_selection_event, sSD.find_selection
  Find in Files... # eEW.find_in_files_event, grep
  Replace...       # eEW.replace_event, replace.ReplaceDialog.replace
  Go to Line       # eEW.goto_line_event
  Show Completions # autocomplete extension and autocompleteWidow (&HP)
  Expand Word      # autoexpand extension
  Show call tip    # Calltips extension and CalltipWindow (& Hyperparser)
  Show surrounding parens  # parenmatch (& Hyperparser)

Shell  # pyshell
  View Last Restart    # pyshell.PyShell.view_restart_mark
  Restart Shell        # pyshell.PyShell.restart_shell
  Interrupt Execution  # pyshell.PyShell.cancel_callback

Debug (Shell only)
  Go to File/Line
  debugger         # debugger, debugger_r, PyShell.toggle_debuger
  Stack Viewer     # stackviewer, PyShell.open_stack_viewer
  Auto-open Stack Viewer  # stackviewer

Format (Editor only)
  Indent Region    # eEW.indent_region_event
  Dedent Region    # eEW.dedent_region_event
  Comment Out Reg. # eEW.comment_region_event
  Uncomment Region # eEW.uncomment_region_event
  Tabify Region    # eEW.tabify_region_event
  Untabify Region  # eEW.untabify_region_event
  Toggle Tabs      # eEW.toggle_tabs_event
  New Indent Width # eEW.change_indentwidth_event
  Format Paragraph # paragraph extension
  ---
  Strip tailing whitespace  # rstrip extension

Run (Editor only)
  Python Shell     # pyshell
  ---
  Check Module     # runscript
  Run Module       # runscript

Options
  Configure IDLE   # eEW.config_dialog, configdialog
    (tabs in the dialog)
    Font tab       # config-main.def
    Highlight tab  # query, config-highlight.def
    Keys tab       # query, config_key, config_keys.def
    General tab    # config_help, config-main.def
    Extensions tab # config-extensions.def, corresponding .py
  ---
  Code Context (ed)# codecontext extension

Window
  Zoomheight       # zoomheight extension
  ---
  <open windows>   # windows

Help
  About IDLE       # eEW.about_dialog, help_about.AboutDialog 
  ---
  IDLE Help        # eEW.help_dialog, helpshow_idlehelp
  Python Doc       # eEW.python_docs
  Turtle Demo      # eEW.open_turtle_demo
  ---
  <other help sources>

<Context Menu> (right click)
  Defined in editor, PyShelpyshellut
    Cut
    Copy
    Paste
    ---
    Go to file/line (shell and output only)
    Set Breakpoint (editor only)
    Clear Breakpoint (editor only)
  Defined in debugger
    Go to source line
    Show stack frame

<No menu>
Center Insert      # eEW.center_insert_event

  
CODE STYLE -- Generally PEP 8.

import
------
Put import at the top, unless there is a good reason otherwise.
PEP 8 says to group stdlib, 3rd-party dependencies, and package imports.
For idlelib, the groups are general stdlib, tkinter, and idlelib.
Sort modules within each group, except that tkinter.ttk follows tkinter.
Sort 'from idlelib import mod1' and 'from idlelib.mod2 import object'
together by module, ignoring within module objects.
Put 'import __main__' after other idlelib imports.

Imports only needed for testing are put not at the top but in an
htest function def or "if __name__ == '__main__'" clause.

Within module imports like "from idlelib.mod import class" may cause
circular imports to deadlock.  Even without this, circular imports may
require at least one of the imports to be delayed until a function call.
