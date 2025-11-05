{
    "name": "Paraguayan Electronic Invoicing",
    "summary": "Paraguayan Electronic Invoicing (odoo 19)",
    "version": "1.0.0",
    'category': 'Accounting/Localizations/EDI',
    "author": "Ansuz Solutions",
    "website": "https://www.ansuzsolutions.com/",
    'description': """
Functional
----------

Technical
---------
""",
    'depends': [
        'l10n_py',
        #'certificate',
    ],
    'external_dependencies': {
        #'python': ['zeep'],
        #'apt': {
        #    'zeep': 'python3-zeep',
        #},
    },
    'data': [
        #'wizards/l10n_ar_afip_ws_consult_view.xml',
        #'wizards/account_move_reversal_view.xml',
        #'views/l10n_ar_afipws_connection_view.xml',
        #'views/res_config_settings_view.xml',
        #'views/account_move_view.xml',
        #'views/account_journal_view.xml',
        #'views/res_currency_view.xml',
        #'views/product_template_view.xml',
        'views/res_config_settings_view.xml',
        #'security/ir.model.access.csv',
        #'data/ir_actions_act_url_data.xml',
    ],
    'demo': [
        #'demo/res_company_demo.xml',
        #'demo/res_config_settings_demo_view.xml',
    ],
    'installable': True,
    'auto_install': ['l10n_py'],
    "license": 'LGPL-3',
}
