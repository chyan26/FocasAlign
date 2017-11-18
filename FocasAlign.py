from __future__ import print_function

import sys, os
import gc

from inspect import getframeinfo, stack

import astropy.io.fits as fits

from ginga.misc.Bunch import Bunch


class FocasImage(object):

    star = None
    mask = None

    def loadImage(self):
        path='/home/chyan/FOCAS/mospointing/'

        try:
            self.star.raw1=fits.open(path+'FCSA00125883.fits',memmap=False)[0]
            self.star.raw2=fits.open(path+'FCSA00125884.fits',memmap=False)[0]
            
            self.mask.ch1=fits.open(path+'FCSA00125885.fits',memmap=False)[0]
            self.mask.ch1=fits.open(path+'FCSA00125886.fits',memmap=False)[0]
        
        except IOError as e:
            caller = getframeinfo(stack()[1][0])
            print("{0}:{1}({2}) I/O error[{3}]: \n  {4}:'{5}'".format(
                caller.filename, stack()[0][3], sys.exc_traceback.tb_lineno , 
                e.errno,e.strerror, e.filename))
            raise  

    def closeImage(self):
    
        if self.star is not None:
            del self.star
        
        if self.mask is not None:
            del self.mask

    def __init__(self):
        self.star=Bunch(dict(raw1 = 0, raw2 = 0, mosaic = 0))
        self.mask=Bunch(dict(ch1 = 0, ch2 = 0, mosaic = 0))

        
        #self.loadImage()


    def __del__(self):
        
        self.closeImage()
        gc.collect()

    def main(self):
        self.__init__()

#if __name__ == '__main__':
#    main()

# END