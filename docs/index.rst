Welcome to Mailman Web's documentation!
=======================================

Mailman 3 web is an umbrella Django project that combines all the web
components of Mailman 3 into a single project that can be installed with a
single command and configured using a TOML configuration file.


=======
Install
=======

To install ``mailman-web`` using ``pip`` run the following command::

  $ pip install mailman-web


=====
Usage
=====

To run Django's development server, you can try::

  $ mailman-web migrate
  $ mailman-web runserver

========
Settings
========

Mailman Web can be customized using a configuration file at
``/etc/mailman3/settings.py``

You can see a list of all the default configurations supported:

.. toctree::
   :maxdepth: 2

   settings


Important Links
===============

* Issue Tracker: https://gitlab.com/mailman/mailman-web/issues
* Documentation: https://mailman-web.readthedocs.io/
* Mailman Suite: https://docs.mailman3.org/
* Mailman Project: https://list.org
