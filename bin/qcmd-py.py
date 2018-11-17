#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from source.python.git.report import gitReport

bases = ['C:\\source', 'C:\\source\\LBS']
users = ['Isaac Adams', 'iadams']

gitReport(bases[0], users)