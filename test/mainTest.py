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

import main
import unittest


class TestMain(unittest.TestCase):
    def test_parameters_string_to_dict(self):
        parameterPairs = parameters_string_to_dict('?foo=bar&gold=silver')
        self.assertEqual(parameterPairs['foo'],'bar')
        self.assertEqual(parameterPairs['gold'],'silver')


if __name__ == '__main__':
    unittest.main()
