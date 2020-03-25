=============
Split picking
=============

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fstock--logistics--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/stock-logistics-workflow/tree/12.0/stock_split_picking
    :alt: OCA/stock-logistics-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/stock-logistics-workflow-12-0/stock-logistics-workflow-12-0-stock_split_picking
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.odoo-community.org/runbot/154/12.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

This module adds a "Split" button on the outgoing pickings form.

It works like the classical picking Transfer but it leaves both pickings
(picking and its backorder) as confirmed without processing the transfer.

**Table of contents**

.. contents::
   :local:

Usage
=====

#. Go to **Inventory** dashboard and open any picking.
#. If picking state is **available** you can see an split button.
#. On the "Operations" tab, fill the field "Done" to the quantity you want to
   split for each line.
#. If you click on **Split** button, wizard will split current picking into
   two different pickings depends on quantity done you entered above.
#. Both pickings remain confirmed.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/stock-logistics-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/stock-logistics-workflow/issues/new?body=module:%20stock_split_picking%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Camptocamp
* Tecnativa
* 

Contributors
~~~~~~~~~~~~

* Nicolas Bessi <nicolas.bessi@camptocamp.com>
* Guewen Baconnier <guewen.baconnier@camptocamp.com>
* Yannick Vaucher <yannick.vaucher@camptocamp.com>
* Vicent Cubells <vicent.cubells@tecnativa.com>
* Julien Coux <julien.coux@camptocamp.com>
* Andrius Preimantas <andrius@versada.eu>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/stock-logistics-workflow <https://github.com/OCA/stock-logistics-workflow/tree/12.0/stock_split_picking>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.