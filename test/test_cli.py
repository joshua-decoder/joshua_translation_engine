import os
import sys
import unittest
sys.path.append('..')
import app

class TestHandleArgs(unittest.TestCase):

    def test_no_args(self):
        argv = ['app.py']
        self.assertRaises(SystemExit, app.handle_cli_args, argv)

    def test_source_bundle_dir_no_source_lang_no_target_lang(self):
        argv = ['app.py', '--bundle-dir', 'test/content/test_run_bundle']
        self.assertRaises(SystemExit, app.handle_cli_args, argv)
