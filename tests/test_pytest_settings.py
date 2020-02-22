# -*- coding: utf-8 -*-

import os
import pytest


def test_paste_deploy_parser(testdir):
    """Make sure that pytest accepts our fixture."""

    testdir.makefile(".ini", example_cfg="""
        [app:main]
        host_addr = 127.0.0.1 

        [alembic]
        script_location = package/alembic
        file_template = %%(year)d%%(month).2d%%(day).2d_%%(rev)s

        [formatter_generic]
        format = %(asctime)s %(levelname)-5.5s [%(name)s][%(threadName)s] %(message)s
        """)
    testdir.makepyfile(
        """
        from pytest_settings import settings


        def test_paste_deploy_parser():
            ipaddr = settings['app:main']['host_addr']
            assert ipaddr == '127.0.0.1'
        """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '-c',
        '{testdir_path}/example_cfg.ini'.format(testdir_path=os.getcwd()),
        '-v'
    )

    result.stdout.fnmatch_lines([
        '*test_paste_deploy_parser.py::test_paste_deploy_parser PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
