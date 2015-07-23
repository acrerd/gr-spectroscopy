#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/astro/repositories/gnuradio_modules/gr-spectroscopy/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/astro/repositories/gnuradio_modules/gr-spectroscopy/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/astro/repositories/gnuradio_modules/gr-spectroscopy/build/swig:$PYTHONPATH
/usr/bin/python2 /home/astro/repositories/gnuradio_modules/gr-spectroscopy/python/qa_accumulator.py 
