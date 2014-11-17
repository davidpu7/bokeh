from __future__ import absolute_import

from ...properties import Bool, Int, Float, String, Instance, Auto, List
from ...plot_object import PlotObject
from ..sources import DataSource
from ..widget import Widget

class CellFormatter(PlotObject):
    pass

class CellEditor(PlotObject):
    pass

class StringFormatter(CellFormatter):
    pass

class CheckmarkFormatter(CellFormatter):
    pass

class StringEditor(CellEditor):
    pass

class TextEditor(CellEditor):
    pass

class SelectEditor(CellEditor):
    options = List(String)

class PercentEditor(CellEditor):
    pass

class CheckboxEditor(CellEditor):
    pass

class IntEditor(CellEditor):
    step = Int(1)

class NumberEditor(CellEditor):
    step = Float(0.01)

class TimeEditor(CellEditor):
    pass

class DateEditor(CellEditor):
    pass

class TableColumn(PlotObject):
    field = String
    title = String
    width = Int(300) # px
    formatter = Instance(CellFormatter, lambda: StringFormatter())
    editor = Instance(CellEditor, lambda: StringEditor())

class TableWidget(Widget):
    source = Instance(DataSource)

class DataTable(TableWidget):
    columns = List(Instance(TableColumn))
    width = Int(None)                # px, optional
    height = Int(400) | Auto         # px, required, use "auto" only for small data
    fit_columns = Bool(True)
    editable = Bool(False)
    selectable = Bool(True)
    row_headers = Bool(True)
