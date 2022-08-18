#!/usr/bin/env python3
# test for hello.py
"""test for hello.py"""

import os
from subprocess import getstatusoutput, getoutput

from asyncio.windows_events import NULL


prg = 'hello.py'
s = '5651'
if s !=NULL:
   print('S exits ')
else:
   print('Not an integer')


# if test exisits
def test_exists():
     """exists"""

assert os.path.isfile(prg)


 # if test is runnable
def test_runnable():
    """Runs using python3"""

    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'Hello, World!'

#----------------------------------------------------------


# if test is executable
def test_executable():
    """says 'Hello, World!' by default"""
    
    out = getoutput({prg})
    assert out.strip() == 'Hello, World!'
    


# if test is usable
    def test_usage():
        """usage"""
        
        for flag in ['-h', '--help']:
            rv, out = getstatusoutput(f'{prg} {flag}')
            assert rv == 0
            assert out.lower().startswith('usuage') 



# test for input
def test_input():
    """test for input"""
    
    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{prg} {option} {val}')
            rv, out == 0
        assert out.strip() == f'Hello, {val}!'
        