# -*- coding: utf-8 -*-

{
    'name': 'TT - Accounting',
    'version': '1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This is the latest TT Odoo localisation necessary to run Odoo accounting for TT SME's
=================================================================================================""",
    'author': 'Centralasis Proactive Solutions Ltd.',
    'website': 'https://www.centralasis.com',
    'depends': [
        'account',
        'base_vat',
    ],
    'data': [
        'data/l10n_tt_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.chart.template.csv',
        'data/account.tax.group.csv',
        'data/account_tax_data.xml',
    ],

    'license': 'OPL-1',
}
