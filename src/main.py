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
import urllib

def parameters_string_to_dict(parameters):
    paramDict={}
    if parameters:
        paramPairs=parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits=paramsPair.split('=')
            if len(paramSplits)==2:
                paramDict[paramSplits[0]]=paramSplits[1]
    return paramDict

def construct_plugin_url(base_url, parameters={}):
    if len(parameters) > 0:
        return base_url + '?' + urllib.urlencode(parameters)
    else:
        return base_url