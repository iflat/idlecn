import re

from tkinter import *
import tkinter.messagebox as tkMessageBox

from idlelib.editor import EditorWindow
from idlelib import iomenu


class OutputWindow(EditorWindow):

    """An editor window that can serve as an output file.

    Also the future base class for the Python shell window.
    This class has no input facilities.
    """

    def __init__(self, *args):
        EditorWindow.__init__(self, *args)
        self.text.bind("<<goto-file-line>>", self.goto_file_line)

    # Customize EditorWindow

    def ispythonsource(self, filename):
        # No colorization needed
        return 0

    def short_title(self):
        return "内容窗口"

    def maybesave(self):
        # Override base class method -- don't ask any questions
        if self.get_saved():
            return "yes"
        else:
            return "no"

    # Act as output file

    def write(self, s, tags=(), mark="insert"):
        if isinstance(s, (bytes, bytes)):
            s = s.decode(iomenu.encoding, "replace")
        self.text.insert(mark, s, tags)
        self.text.see(mark)
        self.text.update()
        return len(s)

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def flush(self):
        pass

    # Our own right-button menu

    rmenu_specs = [
        ("剪切", "<<cut>>", "rmenu_check_cut"),
        ("复制", "<<copy>>", "rmenu_check_copy"),
        ("粘贴", "<<paste>>", "rmenu_check_paste"),
        (None, None, None),
        ("转到文件/行", "<<goto-file-line>>", None),
    ]

    file_line_pats = [
        # order of patterns matters
        r'file "([^"]*)", line (\d+)',
        r'([^\s]+)\((\d+)\)',
        r'^(\s*\S.*?):\s*(\d+):',  # Win filename, maybe starting with spaces
        r'([^\s]+):\s*(\d+):',     # filename or path, ltrim
        r'^\s*(\S.*?):\s*(\d+):',  # Win abs path with embedded spaces, ltrim
    ]

    file_line_progs = None

    def goto_file_line(self, event=None):
        if self.file_line_progs is None:
            l = []
            for pat in self.file_line_pats:
                l.append(re.compile(pat, re.IGNORECASE))
            self.file_line_progs = l
        # x, y = self.event.x, self.event.y
        # self.text.mark_set("insert", "@%d,%d" % (x, y))
        line = self.text.get("insert linestart", "insert lineend")
        result = self._file_line_helper(line)
        if not result:
            # Try the previous line.  This is handy e.g. in tracebacks,
            # where you tend to right-click on the displayed source line
            line = self.text.get("insert -1line linestart",
                                 "insert -1line lineend")
            result = self._file_line_helper(line)
            if not result:
                tkMessageBox.showerror(
                    "没有找到指定的行",
                    "你指定的位置不像是一个 "
                    "可用的文件和行号.",
                    parent=self.text)
                return
        filename, lineno = result
        edit = self.flist.open(filename)
        edit.gotoline(lineno)

    def _file_line_helper(self, line):
        for prog in self.file_line_progs:
            match = prog.search(line)
            if match:
                filename, lineno = match.group(1, 2)
                try:
                    f = open(filename, "r")
                    f.close()
                    break
                except OSError:
                    continue
        else:
            return None
        try:
            return filename, int(lineno)
        except TypeError:
            return None

# These classes are currently not used but might come in handy

class OnDemandOutputWindow:

    tagdefs = {
        # XXX Should use IdlePrefs.ColorPrefs
        "stdout":  {"foreground": "blue"},
        "stderr":  {"foreground": "#007700"},
    }

    def __init__(self, flist):
        self.flist = flist
        self.owin = None

    def write(self, s, tags, mark):
        if not self.owin:
            self.setup()
        self.owin.write(s, tags, mark)

    def setup(self):
        self.owin = owin = OutputWindow(self.flist)
        text = owin.text
        for tag, cnf in self.tagdefs.items():
            if cnf:
                text.tag_configure(tag, **cnf)
        text.tag_raise('sel')
        self.write = self.owin.write
