#!/usr/bin/env python
# -*- coding: utf-8  -*-

class diction():
    def __init__(self):
        self.dict = {"name":"han",
                     "age": "20"}
        
    def NewDict(self):
        row = []
        for i in range(0, 3):
            temp = self.dict.copy()
            temp["age"] = str(i)
            row.append(temp)
        print row
            

if __name__ == "__main__":  
    d = diction()
    d.NewDict()
        
