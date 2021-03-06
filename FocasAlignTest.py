import sys, os

from FocasAlign import FocasImage
import matplotlib.pyplot as plt
import traceback
from inspect import getframeinfo, stack

def fileIO():
    
    try:
        f=FocasImage()
        f.loadImage()
        
        f.closeImage()

    except IOError as e:
        print("{0}:{1}({2}) I/O error[{3}]: \n  {4}:'{5}'".format(
                os.path.basename(stack()[0][1]), stack()[0][3], 
                sys.exc_info()[2].tb_lineno , 
                e.errno,e.strerror, e.filename))
        raise
        #pass  



def main():
    try:
        print("Testing file IO....")
        fileIO()
        print("done\n") 


    except FileNotFoundError as e:
        print("{0}:{1}({2}) I/O error[{3}]: \n  {4}:'{5}'".format(
                os.path.basename(stack()[0][1]), stack()[0][3], 
                sys.exc_info()[2].tb_lineno , 
                e.errno,e.strerror, e.filename))
        raise

if __name__ == '__main__':
    try:
        main()
    except IOError as e:
        pass
    #    caller = getframeinfo(stack()[1][0])
    #    print("{0}:{1}({2}) I/O error[{3}]: \n  {4}:'{5}'".format(
    #            caller.filename, stack()[0][3], sys.exc_traceback.tb_lineno , 
    #            e.errno,e.strerror, e.filename))
        #raise