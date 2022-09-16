#!/usr/bin/env python

import argparse
import os


def main():
    parser = argparse.ArgumentParser(description='The abqpy command line interface')
    parser.add_argument('script', metavar='script', type=str, nargs=1,
                        help='the python script to run')
    parser.add_argument('-n', '--noGUI', dest='noGUI', action='store_true',
                        help='run Abaqus in batch mode')
    parser.add_argument('-m', '--mode', dest='mode', type=str, default='cae', choices=['cae', 'python'],
                        help='option to run Abaqus, either cae or python, by default cae')
    parser.add_argument('others', nargs=argparse.REMAINDER,
                        help='other arguments to pass to Abaqus')
    args = parser.parse_args()
    if args.mode == 'cae':
        option = 'noGUI' if args.noGUI else 'script'
        cmd = f"abaqus cae {option}={args.script[0]} {' '.join(args.others)}"
        message = f'Running the following abaqus command: {cmd}'
        print('', '-' * len(message), message, '-' * len(message), sep='\n')
        os.system(cmd)
    elif args.mode == 'python':
        cmd = f"abaqus python {args.script} {' '.join(args.others)}"
        message = f'Running the following abaqus command: {cmd}'
        print('', '-' * len(message), message, '-' * len(message), sep='\n')
        os.system(cmd)
    else:
        print('Unknown mode, please use either cae or python')
