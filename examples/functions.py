#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simpleodspy.sodsspreadsheet import SodsSpreadSheet
from simpleodspy.sodshtml import SodsHtml

t = SodsSpreadSheet()
t.setValue("D2", 123.5)

t.setValue("D3", "=3.0/5.0")
t.setValue("D4", "=D2*3")
t.setValue("D5", "=ABS(D3)")
t.setValue("D6", "=SIN(PI * D3)")
t.setValue("D7", "=SUM(D2:D6)")
t.setValue("D8", "=IF(D3>D2;D6;D7)")
t.setValue("D9", "=SUM(D2:D6)")
t.setValue("A1", "=D7/D9")

t.setValue("E3", "=hello,world")
t.setValue("E4", "=CUT(E3,1)")

tw = SodsHtml(t)
tw.save("test.html", tip = True, headers = True)

