# -*- coding: utf-8 -*-

import pytest
import plaster
import configparser

settings = {}


def pytest_configure(config):
    global settings

    inifile = config.inifile

    if not type(inifile) is str:
        inifile = str(inifile)

    loader = plaster.get_loader(inifile)
    for section in loader.get_sections():
        settings[section] = _get_section_settings(section, loader)


def _get_section_settings(section_name, loader):
    try:
        return dict(loader.get_settings(section_name))
    except configparser.InterpolationMissingOptionError:
        return dict()
