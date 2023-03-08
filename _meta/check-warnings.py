#!/usr/bin/env python3
"""Reprocess Sphinx errors into github actions compatible syntax

... also fails CI on errors.

We could get the effect we need with sphinx-build -W (all warnings to errors)
if we could ignore one particular warning.  But the ignore machinery isn't
fine-grained enough to exclude only that error.

There are several other gh-actions "error matchers", but they can't ignore
certain errors (in our case, there are many orphan documents so 'document
isno't included in any toctree) is common in our docs.

Syntax guide:
  https://help.github.com/en/actions/reference/development-tools-for-github-actions

"""

import argparse
import sys
import re

r = re.compile(r'([^:]+):([0-9]+)?:? WARNING: (.*)')

# String of messages that should be errors instead of warnings
errors = [
     "'any' reference target not found",
     "unknown document",
     "undefined label: tutorials",
     "Duplicate target name, cannot be used as a unique reference",
     "Indirect hyperlink target",
     "Unknown directive type",
     "Anonymous hyperlink mismatch",
     "toctree contains reference to nonexisting document",
     "Title underline too short",
     "Title overline too short",
     "both interpreted text role prefix and reference suffix",
     "not found or reading it failed",
     "download file not readable",
     "image file not readable",
     "file not readable",
     "undefined label"
    ]

ignores = [
    "document isn't included in any toctree",
    ]

parser = argparse.ArgumentParser()
parser.add_argument('--fail', action='store_true')
parser.add_argument('--warnings-fail', action='store_true')
parser.add_argument('input')
args = parser.parse_args()

NERRORS = 0

for line in open(args.input):
    if 'WARNING' not in line:
        continue
    m = r.match(line)
    if m is None:
        print("UNMATCHED:", line)
    f = m.group(1)
    l = m.group(2) or ''
    assert ',' not in f
    assert ',' not in l
    if l:
        l = ',line=%s'%l
    msg = m.group(3)

    # Ignore certain messages
    if any(w.lower() in msg.lower() for w in ignores):
        continue

    # warning by default, things in list above become errors
    level = 'warning'
    if any(w.lower() in msg.lower() for w in errors) or args.warnings_fail:
        level = 'error'
        NERRORS += 1

    print('::%s file=%s%s::%s'%(level, f, l, msg))

if args.fail and NERRORS > 0:
    sys.exit(1)
