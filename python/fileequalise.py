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
import numpy.fft
from gnuradio import gr

class fileequalise(gr.sync_block):
    """
    docstring for block spline_equalise
    """
    def __init__(self,vlen,flatfield):
        self.flatfield = numpy.genfromtxt(flatfield)[0]
        self.flatfield = self.flatfield/numpy.abs(numpy.max(self.flatfield))
        self.vlen=vlen
        self.axis=numpy.arange(self.vlen)
        gr.sync_block.__init__(self,
            name="fileequalise",
                               in_sig=[(numpy.float32, self.vlen)],
                               out_sig=[(numpy.complex64, self.vlen)])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        in0m = numpy.mean(in0)
        # <+signal processing here+>
        out[:] = numpy.fft.ifft(in0  / (in0m*self.flatfield))
        return len(output_items[0])

