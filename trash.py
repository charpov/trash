#!/usr/bin/env python3

# This is a script from Dave Abrahams, with minor edits
# See https://gist.github.com/dabrahams/14fedc316441c350b382528ea64bc09c.

import os
import sys
import subprocess

BATCH = 1024  # more files than this limit use several invocations of osascript
verbose = True

args = sys.argv[1:]
if args:
    if args[0] == '-q' or args[0] == '--quiet':
        verbose = False
        args.pop(0)
    files = []
    for arg in args:
        if os.path.exists(arg):
            if verbose:
                print(f"trashing {arg}")
            p = os.path.abspath(arg).replace('\\', '\\\\').replace('"', '\\"')
            files.append(f'the POSIX file "{p}"')
        else:
            print(f"{arg}: no such file or directory", file=sys.stderr)
    for start in range(0, len(files), BATCH):
        cmd = ['osascript', '-e',
               f'tell app "Finder" to move {{{", ".join(files[start:start + BATCH])}}} to trash']
        r = subprocess.call(cmd, stdout=open(os.devnull, 'w'))
        if r != 0:
            sys.exit(r)
    if len(files) != len(args):
        sys.exit(1)
