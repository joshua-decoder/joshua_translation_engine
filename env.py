import os
import sys

def assert_valid_env():
    if not os.environ.get('JOSHUA'):
        sys.stderr.write('FATAL: the JOSHUA environment variable is not set.\n')
        sys.exit(-1)
