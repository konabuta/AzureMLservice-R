from __future__ import print_function

import argparse
import os
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str, dest='file', help='filename and parameters')
    parser.add_argument('--alpha', type=str, dest='alpha', default = 100, help='filename and parameters')
    parser.add_argument('--beta', type=str, dest='beta', default = 200, help='filename and parameters')
    args = parser.parse_args()
    print("引数情報", args)

    command_line = ' '.join(['Rscript', '--vanilla']+[args.file]+[args.alpha]+[args.beta])
    print('Launching:', command_line)
    os.system(command_line)