"""
Dialog for building Tkinter accelerator key bindings
"""
from tkinter import *
from tkinter.ttk import Scrollbar
import tkinter.messagebox as tkMessageBox
import string
import sys

class GetKeysDialog(Toplevel):
    def __init__(self, parent, title, action, currentKeySequences,
                 _htest=False, _utest=False):
        """
        action - string, the name of the virtual event these keys will be
                 mapped to
        currentKeys - list, a list of all key sequence lists currently mapped
                 to virtual events, for overlap checking
        _utest - bool, do not wait when running unittest
        _htest - bool, change box location when running htest
        """
        Toplevel.__init__(self, parent)
        self.withdraw() #hide while setting geometry
        self.configure(borderwidth=5)
        self.resizable(height=FALSE, width=FALSE)
        self.title(title)
        self.transient(parent)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.Cancel)
        self.parent = parent
        self.action=action
        self.currentKeySequences = currentKeySequences
        self.result = ''
        self.keyString = StringVar(self)
        self.keyString.set('')
        self.SetModifiersForPlatform() # set self.modifiers, self.modifier_label
        self.modifier_vars = []
        for modifier in self.modifiers:
            variable = StringVar(self)
            variable.set('')
            self.modifier_vars.append(variable)
        self.advanced = False
        self.CreateWidgets()
        self.LoadFinalKeyList()
        self.update_idletasks()
        self.geometry(
                "+%d+%d" % (
                    parent.winfo_rootx() +
                    (parent.winfo_width()/2 - self.winfo_reqwidth()/2),
                    parent.winfo_rooty() +
                    ((parent.winfo_height()/2 - self.winfo_reqheight()/2)
                    if not _htest else 150)
                ) )  #centre dialog over parent (or below htest box)
        if not _utest:
            self.deiconify() #geometry set, unhide
            self.wait_window()

    def CreateWidgets(self):
        frameMain = Frame(self,borderwidth=2,relief=SUNKEN)
        frameMain.pack(side=TOP,expand=TRUE,fill=BOTH)
        frameButtons=Frame(self)
        frameButtons.pack(side=BOTTOM,fill=X)
        self.buttonOK = Button(frameButtons,text='确定',
                width=8,command=self.OK)
        self.buttonOK.grid(row=0,column=0,padx=5,pady=5)
        self.buttonCancel = Button(frameButtons,text='取消',
                width=8,command=self.Cancel)
        self.buttonCancel.grid(row=0,column=1,padx=5,pady=5)
        self.frameKeySeqBasic = Frame(frameMain)
        self.frameKeySeqAdvanced = Frame(frameMain)
        self.frameControlsBasic = Frame(frameMain)
        self.frameHelpAdvanced = Frame(frameMain)
        self.frameKeySeqAdvanced.grid(row=0,column=0,sticky=NSEW,padx=5,pady=5)
        self.frameKeySeqBasic.grid(row=0,column=0,sticky=NSEW,padx=5,pady=5)
        self.frameKeySeqBasic.lift()
        self.frameHelpAdvanced.grid(row=1,column=0,sticky=NSEW,padx=5)
        self.frameControlsBasic.grid(row=1,column=0,sticky=NSEW,padx=5)
        self.frameControlsBasic.lift()
        self.buttonLevel = Button(frameMain,command=self.ToggleLevel,
                text='手动输入要绑定的按键 >>')
        self.buttonLevel.grid(row=2,column=0,stick=EW,padx=5,pady=5)
        labelTitleBasic = Label(self.frameKeySeqBasic,
                text="为你选择的  '"+self.action+"' 操作定义新的快捷键:")
        labelTitleBasic.pack(anchor=W)
        labelKeysBasic = Label(self.frameKeySeqBasic,justify=LEFT,
                textvariable=self.keyString,relief=GROOVE,borderwidth=2)
        labelKeysBasic.pack(ipadx=5,ipady=5,fill=X)
        self.modifier_checkbuttons = {}
        column = 0
        for modifier, variable in zip(self.modifiers, self.modifier_vars):
            label = self.modifier_label.get(modifier, modifier)
            check=Checkbutton(self.frameControlsBasic,
                command=self.BuildKeyString,
                text=label,variable=variable,onvalue=modifier,offvalue='')
            check.grid(row=0,column=column,padx=2,sticky=W)
            self.modifier_checkbuttons[modifier] = check
            column += 1
        labelFnAdvice=Label(self.frameControlsBasic,justify=LEFT,
                            text=\
                            "先点击选择要使用的功能键\n"+
                            "然后在右边列表中选择\n"+
                            "想要组合使用的相应键名.\n\n" +
                            "如果组合中使用了Shift按键\n" +
                            "当与其它键组合使用时.\n" +
                            "(所选择的键会自动转换.)")
        labelFnAdvice.grid(row=1,column=0,columnspan=4,padx=2,sticky=W)
        self.listKeysFinal=Listbox(self.frameControlsBasic,width=15,height=10,
                selectmode=SINGLE)
        self.listKeysFinal.bind('<ButtonRelease-1>',self.FinalKeySelected)
        self.listKeysFinal.grid(row=0,column=4,rowspan=4,sticky=NS)
        scrollKeysFinal=Scrollbar(self.frameControlsBasic,orient=VERTICAL,
                command=self.listKeysFinal.yview)
        self.listKeysFinal.config(yscrollcommand=scrollKeysFinal.set)
        scrollKeysFinal.grid(row=0,column=5,rowspan=4,sticky=NS)
        self.buttonClear=Button(self.frameControlsBasic,
                text='清除键值',command=self.ClearKeySeq)
        self.buttonClear.grid(row=2,column=0,columnspan=4)
        labelTitleAdvanced = Label(self.frameKeySeqAdvanced,justify=LEFT,
                text="为你选择的操作  '"+self.action+"' 输入新的快捷键:\n"+
                "(在这里输入的内容将不会被检测是否有键值冲突!)")
        labelTitleAdvanced.pack(anchor=W)
        self.entryKeysAdvanced=Entry(self.frameKeySeqAdvanced,
                textvariable=self.keyString)
        self.entryKeysAdvanced.pack(fill=X)
        labelHelpAdvanced=Label(self.frameHelpAdvanced,justify=LEFT,
            text="Tkinter图形库定义了一些系统默认快捷键，\n"+
                 "例如: <Control-f>, <Shift-F2>, <F12>,\n"
                 "<Control-space>, <Meta-less>, <Control-Alt-Shift-X>.\n"
                 "大写字母表示同时使用了 Shift 按键!\n\n" +
                 "'Emacs风格' 默认使用了多快捷键绑定\n" +
                 "例如:<Control-x><Control-y>,当第一个按下时\n" +
                 "所绑定的操作将不会执行，直到按下第二个快捷键.\n\n" +
                 "当要为一个操作绑定多个快捷键时，应使用空格\n"+
                 "将多个键值分开, 例如使用： <Alt-v> <Meta-v>." )
        labelHelpAdvanced.grid(row=0,column=0,sticky=NSEW)

    def SetModifiersForPlatform(self):
        """Determine list of names of key modifiers for this platform.

        The names are used to build Tk bindings -- it doesn't matter if the
        keyboard has these keys, it matters if Tk understands them. The
        order is also important: key binding equality depends on it, so
        config-keys.def must use the same ordering.
        """
        if sys.platform == "darwin":
            self.modifiers = ['Shift', 'Control', 'Option', 'Command']
        else:
            self.modifiers = ['Control', 'Alt', 'Shift']
        self.modifier_label = {'Control': 'Ctrl'} # short name

    def ToggleLevel(self):
        if  self.buttonLevel.cget('text')[:8]=='手动输入要绑定的':
            self.ClearKeySeq()
            self.buttonLevel.config(text='<< 基本自定义按键设置')
            self.frameKeySeqAdvanced.lift()
            self.frameHelpAdvanced.lift()
            self.entryKeysAdvanced.focus_set()
            self.advanced = True
        else:
            self.ClearKeySeq()
            self.buttonLevel.config(text='手动输入要绑定的按键 >>')
            self.frameKeySeqBasic.lift()
            self.frameControlsBasic.lift()
            self.advanced = False

    def FinalKeySelected(self,event):
        self.BuildKeyString()

    def BuildKeyString(self):
        keyList = modifiers = self.GetModifiers()
        finalKey = self.listKeysFinal.get(ANCHOR)
        if finalKey:
            finalKey = self.TranslateKey(finalKey, modifiers)
            keyList.append(finalKey)
        self.keyString.set('<' + '-'.join(keyList) + '>')

    def GetModifiers(self):
        modList = [variable.get() for variable in self.modifier_vars]
        return [mod for mod in modList if mod]

    def ClearKeySeq(self):
        self.listKeysFinal.select_clear(0,END)
        self.listKeysFinal.yview(MOVETO, '0.0')
        for variable in self.modifier_vars:
            variable.set('')
        self.keyString.set('')

    def LoadFinalKeyList(self):
        #these tuples are also available for use in validity checks
        self.functionKeys=('F1','F2','F2','F4','F5','F6','F7','F8','F9',
                'F10','F11','F12')
        self.alphanumKeys=tuple(string.ascii_lowercase+string.digits)
        self.punctuationKeys=tuple('~!@#%^&*()_-+={}[]|;:,.<>/?')
        self.whitespaceKeys=('Tab','Space','Return')
        self.editKeys=('BackSpace','Delete','Insert')
        self.moveKeys=('Home','End','Page Up','Page Down','Left Arrow',
                'Right Arrow','Up Arrow','Down Arrow')
        #make a tuple of most of the useful common 'final' keys
        keys=(self.alphanumKeys+self.punctuationKeys+self.functionKeys+
                self.whitespaceKeys+self.editKeys+self.moveKeys)
        self.listKeysFinal.insert(END, *keys)

    def TranslateKey(self, key, modifiers):
        "Translate from keycap symbol to the Tkinter keysym"
        translateDict = {'Space':'space',
                '~':'asciitilde','!':'exclam','@':'at','#':'numbersign',
                '%':'percent','^':'asciicircum','&':'ampersand','*':'asterisk',
                '(':'parenleft',')':'parenright','_':'underscore','-':'minus',
                '+':'plus','=':'equal','{':'braceleft','}':'braceright',
                '[':'bracketleft',']':'bracketright','|':'bar',';':'semicolon',
                ':':'colon',',':'comma','.':'period','<':'less','>':'greater',
                '/':'slash','?':'question','Page Up':'Prior','Page Down':'Next',
                'Left Arrow':'Left','Right Arrow':'Right','Up Arrow':'Up',
                'Down Arrow': 'Down', 'Tab':'Tab'}
        if key in translateDict:
            key = translateDict[key]
        if 'Shift' in modifiers and key in string.ascii_lowercase:
            key = key.upper()
        key = 'Key-' + key
        return key

    def OK(self, event=None):
        if self.advanced or self.KeysOK():  # doesn't check advanced string yet
            self.result=self.keyString.get()
            self.destroy()

    def Cancel(self, event=None):
        self.result=''
        self.destroy()

    def KeysOK(self):
        '''Validity check on user's 'basic' keybinding selection.

        Doesn't check the string produced by the advanced dialog because
        'modifiers' isn't set.

        '''
        keys = self.keyString.get()
        keys.strip()
        finalKey = self.listKeysFinal.get(ANCHOR)
        modifiers = self.GetModifiers()
        # create a key sequence list for overlap check:
        keySequence = keys.split()
        keysOK = False
        title = '键值错误'
        if not keys:
            tkMessageBox.showerror(title=title, parent=self,
                                   message='没有指定按键.')
        elif not keys.endswith('>'):
            tkMessageBox.showerror(title=title, parent=self,
                                   message='按键应以">"号结束')
        elif (not modifiers
              and finalKey not in self.functionKeys + self.moveKeys):
            tkMessageBox.showerror(title=title, parent=self,
                                   message='指定的按键未修改.')
        elif (modifiers == ['Shift']) \
                 and (finalKey not in
                      self.functionKeys + self.moveKeys + ('Tab', 'Space')):
            msg = ' shift 键不能和该键'\
                  ' 一块使用.'
            tkMessageBox.showerror(title=title, parent=self, message=msg)
        elif keySequence in self.currentKeySequences:
            msg = '该键值组合已被使用.'
            tkMessageBox.showerror(title=title, parent=self, message=msg)
        else:
            keysOK = True
        return keysOK


if __name__ == '__main__':
    from idlelib.idle_test.htest import run
    run(GetKeysDialog)
