import wx
import wx.grid
from wx.lib import wordwrap


class GridFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        # wxGrid オブジェクトを作成する
        grid = wx.grid.Grid(self, -1)

        # 次に、CreateGrid を呼び出してグリッドの寸法を設定します。
        # (この例では 50 行 10 列)
        grid.CreateGrid(50, 10)

        # 個々の行と列のサイズをピクセル単位で設定できます
        grid.SetRowSize(0, 60)
        grid.SetColSize(0, 120)

        # グリッドセルの内容を文字列として設定します
        grid.SetCellValue(0, 0, 'これいいね！')

        # 一部のセルを読み取り専用に指定できます
        grid.SetCellValue(0, 3, '読み込み専用編集不可')
        grid.SetReadOnly(0, 3)

        # グリッドセルの内容に色を指定可能
        grid.SetCellValue(3, 3, '緑色だねえ')
        grid.SetCellTextColour(3, 3, wx.GREEN)
        grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)

        # 一部のセルに文字列ではなく数値を格納するように指定できます
        # ここでは、幅 6、精度 2 で表示される浮動小数点値を保持するようにグリッド列 5 を設定します

        grid.SetColFormatFloat(5, 6, 2)
        grid.SetCellValue(0, 6, '3.1415')

        self.Show()


if __name__ == '__main__':
    app = wx.App(0)
    frame = GridFrame(None)
    app.MainLoop()
