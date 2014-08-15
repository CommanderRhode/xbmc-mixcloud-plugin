# -*- coding: utf-8 -*-

'''
@author: CommanderRhode

Copyright (C) 2011-2014 jackyNIX

This file is part of XBMC MixCloud Plugin.

XBMC MixCloud Plugin is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

XBMC MixCloud Plugin is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with XBMC MixCloud Plugin.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import os
testdirectory = os.path.dirname(__file__)
srcdirectory = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdirectory, srcdirectory)))

from main import *
import unittest


class TestMain(unittest.TestCase):
    def test_parameters_string_to_dict(self):
        parameterPairs = parameters_string_to_dict('?foo=bar&gold=silver')
        self.assertEqual(parameterPairs['foo'],'bar')
        self.assertEqual(parameterPairs['gold'],'silver')

    def test_construct_plugin_url_with_populated_base_url_and_paramaters_gives_a_string(self):
        query_parameters = {}
        query_parameters['foo'] = 'bar'
        query_parameters['gold'] ='silver'
        base_url = 'plugin://plugin.video.myaddon/'
        expected_url = 'plugin://plugin.video.myaddon/?foo=bar&gold=silver'
        self.assertEqual(construct_plugin_url(base_url=base_url, parameters=query_parameters),expected_url)

    def test_construct_plugin_url_with_populated_base_url_but_not_paramaters_gives_a_string(self):
        query_parameters = {}
        base_url = 'plugin://plugin.video.myaddon/'
        expected_url = 'plugin://plugin.video.myaddon/'
        self.assertEqual(construct_plugin_url(base_url=base_url, parameters=query_parameters),expected_url)

if __name__ == '__main__':
    unittest.main()