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
import os

if __name__ == '__main__':
    arguments = docopt(__doc__)
    annotation_file = arguments['ANNOTATION_FILE']
    filename = os.path.basename(arguments['ANNOTATION_FILE'])
    raw_filename = filename.split('.')[0]
    print("Converting {0}".format(filename))

    annotations = []

    # Import
    with open(annotation_file) as file:

        # Check if CSV has a header
        has_header = csv.Sniffer().has_header(file.read(1024))
        # Rewind file
        file.seek(0)
        reader = csv.reader(file, delimiter=';')
        if has_header:
            next(reader)

        for row in reader:
            annotation = {}
            annotation['page'] = row[3]
            annotation['quote'] = row[4]
            annotations.append(annotation)

    # Export
    export_location = '{0}.md'.format(raw_filename)
    export_file = open(export_location, 'w')
    for annotation in annotations:
        quote = annotation['quote']
        page = annotation['page']

        quote = quote.strip().replace('\n', '\n> ')
        export_file.write("> {0} *(p.{1})*\n\n".format(quote, page))
    export_file.close()
