#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simpleodspy.sodsspreadsheet import SodsSpreadSheet
from simpleodspy.sodshtml import SodsHtml

t = SodsSpreadSheet()

def mul3Callback(arg):
  val = t.evaluateFormula(arg) * 3 
  return str(val)

t.registerFunction('MUL3', mul3Callback)

t.setValue("D2", 123.5)
t.setValue("D3", "=3.0/5.0")
t.setValue("D4", "=MUL3(D2+D3)")

tw = SodsHtml(t)
tw.save("test.html")

