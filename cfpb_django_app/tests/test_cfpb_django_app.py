#!/usr/bin/env python
from __future__ import print_function

import unittest
from io import StringIO, TextIOWrapper

# Some Python 2-friendly imports
try:
    import builtins
except ImportError:
    import __builtin__ as builtins

try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch, MagicMock

import cfpb_django_app


class TestCFPBDjangoApp(unittest.TestCase):

    @patch('os.makedirs')
    @patch('os.path.exists')
    def test_makedirs(self, mock_os_path_exists, mock_os_makedirs):
        # Exists, then it doesn't exist
        mock_os_path_exists.side_effect = [True, False, False]
        mock_os_makedirs.side_effect = [True, OSError()]

        dest_dir = 'directory'

        # Try it dry
        result = cfpb_django_app.makedirs(dest_dir, dry=True)
        self.assertTrue(result)
        mock_os_path_exists.assert_not_called()
        mock_os_makedirs.assert_not_called()

        # Try it wet with an existing dir
        result = cfpb_django_app.makedirs(dest_dir, dry=False)
        mock_os_path_exists.assert_called_with(dest_dir)
        mock_os_makedirs.assert_not_called()
        self.assertFalse(result)

        # Try it wet without an existing dir
        result = cfpb_django_app.makedirs(dest_dir, dry=False)
        mock_os_path_exists.assert_called_with(dest_dir)
        mock_os_makedirs.assert_called_with(dest_dir)
        self.assertTrue(result)

        # Try it wet with an exception, which causes a False result
        result = cfpb_django_app.makedirs(dest_dir, dry=False)
        mock_os_path_exists.assert_called_with(dest_dir)
        mock_os_makedirs.assert_called_with(dest_dir)
        self.assertFalse(result)

    @patch('cfpb_django_app.makedirs')
    @patch('builtins.open')
    def test_makefile(self, mock_open, mock_makedirs):
        mock_file = """I'm a file: {{app_name}}"""
        replacements = {'app_name': 'myapp'}
        
        mock_source = StringIO(mock_file)
        mock_dest = MagicMock(spec=TextIOWrapper)
        mock_open.side_effect = [mock_source, mock_dest]

        # Try it dry 
        cfpb_django_app.makefile('source_file', 'dest_file',
                replacements, dry=True)
        mock_dest.__enter__.return_value.write.assert_not_called()

        # Try it wet
        cfpb_django_app.makefile('source_file', 'app_name_file',
                replacements, dry=False)
        mock_dest.__enter__.return_value.write.assert_called_with(
                "I'm a file: myapp")

        # Make sure app_name was replaced in 'app_name_file' 
        mock_open.assert_called_with('myapp_file', 'w',
                encoding='utf-8')

    @patch('cfpb_django_app.makedirs')
    @patch('cfpb_django_app.makefile')
    @patch('os.walk')
    def test_makeapp(self, mock_os_walk, mock_makefile, mock_makedirs):
        mock_os_walk.return_value = [
            ('/skel', ('app_name','app_name_proj', '.git'),
                ('foobar.py', '.DS_Store')),
            ('/skel/app_name', (), ('foobar.py',)),
            ('/skel/app_name_proj', (), ('foobar.py',)),
            ('/skel/.git', (), ('config',)),
        ]
    
        cfpb_django_app.makeapp('myapp', '', '', '/skel', 'dest', dry=True)

        # Make sure IGNORED files are actually ignored
        source_files = [a[0][0] for a in mock_makefile.call_args_list]
        ignored_files = [f for i in cfpb_django_app.IGNORE 
                for f in source_files if i in f]
        self.assertEqual(len(ignored_files), 0)
