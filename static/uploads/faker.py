# -*- coding: utf-8 -*-
import sys, os, time
from multiprocessing import Process, Pipe
import rpy2.robjects as robs
import rpy2.rinterface as rint
from threading import Timer

"""
Python script to 'emulate' a very basic R console
The console supports multiline commands, and all R input and output,
but does not have any command history or other such features
"""

class OutputCatcher:
    def __init__(self, pipe):
        self.pipe = pipe

    def write(self, stuff):
        self.pipe.send(stuff)

    def flush(self):
        pass

    def clear(self):
        pass

class RProcess(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        sys.stdout = sys.stderr = OutputCatcher(self.pipe)
        try_ = robs.r.get("try", mode='function')
        parse_ = robs.r.get("parse", mode='function')
        paste_ = robs.r.get("paste", mode='function')
        withVisible_ = robs.r.get("withVisible", mode='function')
        t = Timer(0.03, self.update)
        t.start()
        while 1:
            cmd = self.pipe.recv()
            if cmd is None:
                break
            try:
                result = try_(parse_(text=paste_(unicode(cmd, "UTF-8"))), silent=True)
                value, visible = try_(withVisible_(result[0]), silent=True)
                iss4 = isinstance(value, robs.methods.RS4)
                if visible[0]:
                    if iss4:
                        self.pipe.send(unicode(value))
                    elif str(value).count('NULL'):
                        self.pipe.send(unicode(value))
            except Exception, err:
                self.pipe.send(unicode(err))
            time.sleep(0.03)
            self.pipe.send(None)

    def update(self, interval=0.03):
        while 1:
            try:
                rint.process_revents()
            except:
                pass
            time.sleep(interval)

if __name__ == "__main__":

    welcome = """
Welcome to fakeR version 0.01
Copyright (C) 2010 Carson J. Q. Farmer

fakeR is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.
fakeR is a toy R console, and so shouldn't really be used for anything

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q' (not q()!) to quit fakeR.
"""
    parent, child = Pipe()
    p = RProcess(child)
    p.start()
    inp = ""
    def f(x):
        pass # basically ignores R output
    rint.set_writeconsole(f)
    print welcome
    while not inp == "q":
        inp = raw_input('> ')
        try:
            robs.r.parse(text=inp)
        except rint.RRuntimeError, err:
            err = str(err)
            # as long as the error is simply due to an incomplete 
            # (multiline) commmand, keep looking for more input
            while "unexpected end of input" in err:
                inp += raw_input('+ ')
                try:
                    robs.r['try'](robs.r.parse(text=inp), silent=True)
                    err = ""
                except rint.RRuntimeError, err:
                    err = str(err)
        parent.send(inp)
        # this could be done in a separate thread, but this 
        # keeps things clean when using Python's raw_input
        while 1:
            out = parent.recv()
            if out is None:
                break
            else:
                print out,
            time.sleep(0.03)
    parent.send(None)
    
