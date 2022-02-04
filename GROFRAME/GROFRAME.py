#!/usr/bin/env python
# coding: utf-8

# In[5]:





# In[101]:
import numpy as np
import pandas as pd

class GROFRAME:
    import numpy as np
    import pandas as pd
    def __init__(self, fname):
        self.fname = fname
        self.all_lines = open(self.fname, encoding = "utf-8").readlines()
        length = len(self.all_lines)
        if int(self.all_lines[1]) != (length - 3):
            print("Number of atoms mismatch!!")
    def make_line(self,i):
        Line = self.all_lines[i]
        mLine = self.getLine(Line)
        mDict = {"rid" : mLine[0], "resname" : mLine[1], "name" : mLine[2],
                 "id" : mLine[3], "x" : mLine[4], "y" : mLine[5], "z" : mLine[6]}
        return mDict
    def getLine(self,Line):
        rid = Line[:5].strip()
        resname = Line[5:10].strip()
        nname = Line[10:15].strip()
        nid = Line[15:20].strip()
        x = Line[20:28].strip()
        y = Line[28:36].strip()
        z = Line[36:44].strip()
        return rid, resname, nname, nid, x, y, z
    def makeDataFrame(self):
        totalAtomNumber = int(self.all_lines[1])
        #df = pd.DataFrame({"rid" : 0, "resname" : 1, "name" : 2,
        #         "id" : 3, "x" : 4, "y" : 5, "z" : 6}, index = [0])
        Lines = self.all_lines
        rid = np.array([self.getLine(Lines[i])[0] for i in range(totalAtomNumber)], dtype = int)
        resname = np.array([self.getLine(Lines[i])[1] for i in range(totalAtomNumber)], dtype = str)
        name = np.array([self.getLine(Lines[i])[2] for i in range(totalAtomNumber)], dtype = str)
        nid = np.array([self.getLine(Lines[i])[3] for i in range(totalAtomNumber)], dtype = int)
        x = np.array([self.getLine(Lines[i])[4] for i in range(totalAtomNumber)], dtype = float)
        y = np.array([self.getLine(Lines[i])[5] for i in range(totalAtomNumber)], dtype = float)
        z = np.array([self.getLine(Lines[i])[6] for i in range(totalAtomNumber)],dtype = float)
        #for i in range(totalAtomNumber):
        #    dictI = self.make_line(i)
        #    df.append(dictI, ignore_index = True)
        df = pd.DataFrame({"rid" : rid, "resname" : resname, "name" : name,
                 "id" :nid , "x" : x, "y" : y, "z" : z})
            
        return df

