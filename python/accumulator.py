#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class accumulator(gr.decim_block):
    """
    The accumulator takes in vectors containing a spectrum, 
    and adds them together to provide a long integration time.
    """
    def __init__(self, vlen=10):
        self.vlen=vlen
        self.buildup = numpy.zeros(vlen)
        self.i = 0
        gr.decim_block.__init__(self,
                                name="accumulator",
                                in_sig=[(numpy.float32, self.vlen)],
                                out_sig=[(numpy.float32, self.vlen)],
                                decim=1)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        # To test we'll just give a sum of the input vector.
        # out[:] = [numpy.sum(in0)]
        #print in0.sum(axis=0)
        self.i += 1
        self.buildup += in0.sum(axis=0)#/in0.sum()
        out[:] = self.buildup / numpy.abs(self.buildup.sum())
        return len(output_items[0])

    def reset(self, value):
        print("Resetting")
        self.buildup = numpy.zeros(self.vlen)
        #self.i = 0
        return 0
