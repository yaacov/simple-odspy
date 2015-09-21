#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simpleodspy.sodsspreadsheet import SodsSpreadSheet

t = SodsSpreadSheet(10, 10)

print "Test spreadsheet naming:"
print "-----------------------"

# setting values and formulas
t.setValue("A1", "Hello world !")

t.setValue("B2:C2", 123.4)
t.setValue("B3", "=B2+3")
t.setValue("B4", "=sum(B2:B3)")

# cell styles
t.setStyle("A1", color = "#0000ff")
t.setStyle("A1:A5", background_color = "#00ff00")
t.setStyle("B1:B5", border_left = "1pt solid #ff0000", background_color = "#ffff00")

# conditional styles
t.setStyle("B1:B5", condition = "cell-content()<=125")
t.setStyle("B1:B5", condition_color = "#ff0000")

# export
from simpleodspy.sodsxml import SodsXml
tw = SodsXml(t)
tw.save("test.xml")

# import
t2 = SodsSpreadSheet(10, 10)
tw = SodsXml(t2)
tw.load("test.xml")
tw.save("test2.xml")

from simpleodspy.sodshtml import SodsHtml

def myCallback(args):
    val = 0
    for arg in t.rangeIterator(args):
        val += t.evaluateFormula(arg) * 2
        
    return str(val)

t.registerFunction('MY', myCallback)
t.setValue("B5", "=MY(B2:B3)")

tw = SodsHtml(t)
tw.save("test.html")

