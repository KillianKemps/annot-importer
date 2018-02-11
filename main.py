#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Usage: main.py ANNOTATION_FILE

Convert annotation file to Markdown

Arguments:
  ANNOTATION_FILE File to import

Options:
  -h --help
"""

from docopt import docopt
import csv

if __name__ == '__main__':
    arguments = docopt(__doc__)
