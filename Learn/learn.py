import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size = (700, 500))


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title = "The first Window ever")
        self.frame.Show()
        return True

app = MyApp()
app.MainLoop()