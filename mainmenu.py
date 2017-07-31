"""Define the menu contents, hotkeys, and event bindings.

There is additional configuration information in the EditorWindow class (and
subclasses): the menus are created there based on the menu_specs (class)
variable, and menus not created are silently skipped in the code here.  This
makes it possible, for example, to define a Debug menu which is only present in
the PythonShell window, and a Format menu which is only present in the Editor
windows.

"""
from importlib.util import find_spec

from idlelib.config import idleConf

#   Warning: menudefs is altered in macosx.overrideRootMenu()
#   after it is determined that an OS X Aqua Tk is in use,
#   which cannot be done until after Tk() is first called.
#   Do not alter the 'file', 'options', or 'help' cascades here
#   without altering overrideRootMenu() as well.
#       TODO: Make this more robust

menudefs = [
 # underscore prefixes character to underscore
 ('file', [
   ('新建(_N)', '<<open-new-window>>'),
   ('打开(_O)...', '<<open-window-from-file>>'),
   ('打开模块(_M)...', '<<open-module>>'),
   ('查看类(_B)', '<<open-class-browser>>'),
   ('查看路径(_P)', '<<open-path-browser>>'),
   None,
   ('保存(_S)', '<<save-window>>'),
   ('另存为(_A)...', '<<save-window-as-file>>'),
   ('剪贴板另存为(_y)...', '<<save-copy-of-window-as-file>>'),
   None,
   ('打印(_t)', '<<print-window>>'),
   None,
   ('关闭(_C)', '<<close-window>>'),
   ('退出(_x)', '<<close-all-windows>>'),
  ]),
 ('edit', [
   ('撤销(_U)', '<<undo>>'),
   ('重做(_R)', '<<redo>>'),
   None,
   ('剪切(_t)', '<<cut>>'),
   ('复制(_C)', '<<copy>>'),
   ('粘贴(_P)', '<<paste>>'),
   ('全选(_A)', '<<select-all>>'),
   None,
   ('查找(_F)...', '<<find>>'),
   ('重新查找(_g)', '<<find-again>>'),
   ('查找选中(_S)', '<<find-selection>>'),
   ('在文件中查找...', '<<find-in-files>>'),
   ('替换(_e)...', '<<replace>>'),
   ('转到(_L)', '<<goto-line>>'),
  ]),
('format', [
   ('增加缩进(_I)', '<<indent-region>>'),
   ('减少缩进(_D)', '<<dedent-region>>'),
   ('整体注释(_O)', '<<comment-region>>'),
   ('取消注释(_n)', '<<uncomment-region>>'),
   ('空格转换为Tab', '<<tabify-region>>'),
   ('Tab转换为空格', '<<untabify-region>>'),
   ('设置Tabs转换', '<<toggle-tabs>>'),
   ('设置缩进宽度', '<<change-indentwidth>>'),
   ]),
 ('run', [
   ('Python命令行', '<<open-python-shell>>'),
   ]),
 ('shell', [
   ('查看最后结果(_V)', '<<view-restart>>'),
   ('重启命令行(_R)', '<<restart-shell>>'),
   None,
   ('中断执行(_I)', '<<interrupt-execution>>'),
   ]),
 ('debug', [
   ('转到错误行(_G)', '<<goto-file-line>>'),
   ('!调试(_D)', '<<toggle-debugger>>'),
   ('查看堆栈(_S)', '<<open-stack-viewer>>'),
   ('!自动打开堆栈(_A)', '<<toggle-jit-stack-viewer>>'),
   ]),
 ('options', [
   ('配置IDLE(_I)', '<<open-config-dialog>>'),
   None,
   ]),
 ('help', [
   ('关于IDLE(_A)', '<<about-idle>>'),
   None,
   ('IDLE帮助(_I)', '<<help>>'),
   ('Python文档(_D)', '<<python-docs>>'),
   ]),
]

if find_spec('turtledemo'):
    menudefs[-1][1].append(('示例演示', '<<open-turtle-demo>>'))

default_keydefs = idleConf.GetCurrentKeySet()
