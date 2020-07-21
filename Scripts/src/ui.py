import wx
import olRamseyNumber
class ExamplePanel(wx.Frame):

    def __init__(self, parent,id):
        """
        UI for generating. The Ui contains input the limit length of the
        chronomatic path and the online ramsey number for that path
        """
        wx.Frame.__init__(self,parent,id,"Online Ramsey Calculator")
        p = wx.Panel(self)

        # The input and output logger
        self.input = 0
        self.output = 0

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        #create status bar
        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()
        menubar.Append(first,"File")
        menubar.Append(second,"Edit")
        self.SetMenuBar(menubar)



        # the edit control - one line version.
        lblname = wx.StaticText(p, label= "Path Length :")
        grid.Add(lblname, pos=(1,0))
        self.editname = wx.TextCtrl(p, value="Enter here length of Path", size=(140,-1))
        grid.Add(self.editname, pos=(1,1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)

        resultName = wx.StaticText(p,label = "OL Ramsey Number:   ")
        grid.Add(resultName,pos = (2,0))

        # A button
        self.button =wx.Button(p, label="Run")
        grid.Add(self.button,pos=(1,2))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        # The output window
        self.resultText = wx.StaticText(p,label = str(self.output))
        grid.Add(self.resultText,pos = (2,1))


        hSizer.Add(grid, 0, wx.ALL, 5)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        p.SetSizerAndFit(mainSizer)


    def OnClick(self, event):
        """
        Click <RUN> Button
        """
        if not (self.input).isdigit():
            print(self.input.isdigit())
            self.resultText.SetLabel(-1)
        else:
            self.output = olRamseyNumber.get_online_ramsey_number(int(self.input))
            self.resultText.SetLabel(self.output)

    def EvtText(self, event):
        """
        Output result
        """
        self.input = event.GetString()


app = wx.App(False)
frame = ExamplePanel(None,1)
frame.Show()
app.MainLoop()