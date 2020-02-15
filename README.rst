===============
pytest-settings
===============

.. image:: https://img.shields.io/pypi/v/pytest-settings.svg
    :target: https://pypi.org/project/pytest-settings
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-settings.svg
    :target: https://pypi.org/project/pytest-settings
    :alt: Python versions

.. image:: https://travis-ci.org/kvaldivia/pytest-settings.svg?branch=master
    :target: https://travis-ci.org/kvaldivia/pytest-settings
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/kvaldivia/pytest-settings?branch=master
    :target: https://ci.appveyor.com/project/kvaldivia/pytest-settings/branch/master
    :alt: See Build Status on AppVeyor

Access your configuration file's parsed settings from your tests

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

* Access the sections of your .ini file.


Requirements
------------

* plaster_pastedeploy
* pytest >= 5.3.5


Installation
------------

You can install "pytest-settings" via `pip`_ from `PyPI`_::

    $ pip install pytest-settings


Usage
-----

* Import the `settings` and you are good to go, each key matches a configuration section::

    from pytest_settings import settings

* Then you can access the sections like this::

    my_section = settings['mysection']

* And each value in the section::

    my_value = settings['mysection']['myvalue']


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `BSD-3`_ license, "pytest-settings" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/kvaldivia/pytest-settings/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
