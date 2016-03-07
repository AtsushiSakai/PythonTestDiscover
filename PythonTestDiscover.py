#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Atsushi Sakai
import os
import sys
import logging as log
import subprocess 

#You can set top dir of the test file search
SearchPath="../../../"

class PythonTest:
    def __init__(self):
        # Get PythonTest dir path
        testPaths=self.SearchTestFiles()

        for path in testPaths:
            self.ExeTest(path)

    def ExeTest(self,path):
        """
            Execute test
        """
        # cmd="python "+path
        p = subprocess.Popen(['python', path],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     shell=False)
        # print 'return: %d' % (p.wait(), )
        # print 'stdout: %s' % (p.stdout.readlines(), )
        # print 'stderr: %s' % (p.stderr.readlines(), )

        std=p.stdout.readlines()
        err=p.stderr.readlines()

        if  "F" in err[0]:
            for errone in err:
                Print(errone.replace("\n",""),"red")
        else:
            for errone in err:
                Print(errone.replace("\n",""),"green")
 


    def SearchTestFiles(self):
        """ 
        Search test file
        """
        testPaths=[]
        for file in self.fild_all_files(SearchPath):
            if "Test.py" in file and ".pyc" not in file:
                testPaths.append(file)

        if len(testPaths)==0:
            Print('Cannot find any test file.',"yellow")
            exit(0)

        print((str(len(testPaths))+" test files are found"))
        print(testPaths)
        return testPaths

    def fild_all_files(self,directory):
        for root, dirs, files in os.walk(directory):
            yield root
            for file in files:
                yield os.path.join(root, file)




def Print(string, color, highlight=False):
    """
    Colored print

    colorlist:
        red,green

    """
    end="\033[1;m"
    pstr=""
    if color == "red":
        if highlight:
            pstr+='\033[1;41m'
        else:
            pstr+='\033[1;31m'
    elif color == "green":
        if highlight:
            pstr+='\033[1;42m'
        else:
            pstr+='\033[1;32m'
    elif color == "yellow":
        if highlight:
            pstr+='\033[1;43m'
        else:
            pstr+='\033[1;33m'

    else:
        print(("Error Unsupported color:"+color))

    print((pstr+string+end))


if __name__ == '__main__':
    print(__file__+" start!!")
    argvs = sys.argv 
    if len(argvs)>=2:
        SearchPath=argvs[1]
    PythonTest()


