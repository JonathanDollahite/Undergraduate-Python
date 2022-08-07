#!/usr/bin/env python3

import sys
import argparse
from lxml import etree
from dateutil import parser as dtp

def convert(infile, outfile):
    xt = etree.parse(infile)
    ns = xt.getroot().nsmap
    for pt in xt.iterfind('trk/trkseg/trkpt', ns):
        lat = pt.get('lat')
        lon = pt.get('lon')
        dt = dtp.parse(pt.find('time', ns).text)
        print(lat, lon, dt.date(), dt.time(), file=outfile)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Convert from gpx to plain text')
    ap.add_argument('infile', type=argparse.FileType('r'),
        help='GPX file to read from')
    ap.add_argument('outfile', type=argparse.FileType('w'),
        nargs='?', default=sys.stdout,
        help='TXT file to create (default standard out)')
    args = ap.parse_args()
    convert(args.infile, args.outfile)
