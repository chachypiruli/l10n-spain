# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Avanced Open Source Consulting
#    Copyright (C) 2010 - 2011 Avanzosc <http://www.avanzosc.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Previsión de Tesorería",
    "version": "1.0",
    "depends": [
                "account",
                "account_payment",
                ],
    "author": "Avanzosc S.L.",
    "website": "http://www.avanzosc.com",
    "category": "Accounting",
    "description": """
    Este modulo contiene :
        Formularios para realizar las previsiones de tesoreria
    """,
    "init_xml": [],
    'update_xml': ["security/l10n_es_tesoreria_security.xml",
                   "security/ir.model.access.csv",
                   "wizard/wiz_crear_factura_view.xml",
                   "prev_tesoreria_view.xml",
                   "prev_tesoreria_plantilla_view.xml",
                   ],
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}