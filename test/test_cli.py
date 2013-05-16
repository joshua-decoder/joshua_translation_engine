import unittest
import app

class TestHandleArgs(unittest.TestCase):

    def test_no_args(self):
        argv = ['app.py']
        self.assertRaises(SystemExit, app.handle_cli_args, argv)

    def test_source_bundle_dir_no_source_lang_no_target_lang(self):
        argv = ['app.py', '--bundle-dir', 'test/content/test_run_bundle']
        self.assertRaises(SystemExit, app.handle_cli_args, argv)

    def test_no_port_numbers(self):
        """
        Not specifying a port number with multiple bundles will have
        incremental port numbers based on the the DEFAULT_TCP_PORT.
        """
        argv = [
            'app.py',
            '-b', 'bundle1', 'bundle2',
            '-s', 'es',      'en',
            '-t', 'en',      'es',
        ]
        self.assertEqual([56748, 56749], app.handle_cli_args(argv).port)

    def test_only_one_port_number(self):
        """
        Only one port can be specified. Multiple bundles will have incremental
        port numbers.
        """
        argv = [
            'app.py',
            '-b', 'bundle1', 'bundle2',
            '-s', 'es',      'en',
            '-t', 'en',      'es',
            '-p', '56749',
        ]
        self.assertEqual([56749, 56750], app.handle_cli_args(argv).port)

    def test_number_of_port_numbers_matches_number_of_bundles(self):
        """
        The number of ports specified can be the same as the number of bundles
        specified.
        """
        argv = [
            'app.py',
            '-b', 'bundle1', 'bundle2',
            '-s', 'es',      'en',
            '-t', 'en',      'es',
            '-p', '56740',  '56741',
        ]
        self.assertEqual([56740, 56741], app.handle_cli_args(argv).port)

    def test_port_number_not_one_or_N(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
