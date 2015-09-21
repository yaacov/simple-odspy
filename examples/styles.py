#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simpleodspy.sodsspreadsheet import SodsSpreadSheet
from simpleodspy.sodshtml import SodsHtml

t = SodsSpreadSheet()

t.setValue("A1:A3", "green")
t.setStyle("A1:A3", background_color = "#00ff00")
t.setValue("B1:B3", "blue")
t.setStyle("B1:B3", background_color = "#0000ff")
t.setStyle("B3", border_top = "1pt solid #ff0000", border_bottom = "1pt solid #ff0000")

tw = SodsHtml(t)
tw.save("test.html")

