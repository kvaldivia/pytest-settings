# -*- coding: utf-8 -*-

import os


def test_paste_deploy_parser(testdir):
    """Make sure that pytest accepts our fixture."""
    testdir_path = os.getcwd()

    testdir.makefile(".ini", example_cfg="""
        [app:main]
        host_addr = 127.0.0.1 

        [alembic]
        script_location = package/alembic
        file_template = %%(year)d%%(month).2d%%(day).2d_%%(rev)s
        sqlalchemy.url = mysql+pymysql://username:password@0.0.0.0:3306/database

        [formatter_generic]
        format = %(asctime)s %(levelname)-5.5s [%(name)s][%(threadName)s] %(message)s
        """)
    testdir.makepyfile(
        """
        from pytest_settings import settings
        def test_foo():
            ipaddr = settings['app:main']['host_addr']
            assert ipaddr == '127.0.0.1'

            db_url = mysql+pymysql://username:password@0.0.0.0:3306/database
            assert settings['alembic']['sqlalchemy.url'] == db_url
        """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        f'-c={testdir_path}/example_cfg.ini',
        '-v'
    )

    result.stdout.fnmatch_lines([
        '*test_paste_deploy_parser.py::test_foo PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
