# -*- coding: utf-8 -*-
{
    'name': 'LBS Dynamic Financial Reports',
    'version': '15.0.1',
    'description': 'LBS Dynamic Financial Reports',
    'author': 'LBS Company',
    'license': 'OPL-1',
    'sequence': 15,
    'category': 'Accounting/Accounting',
    'depends': ['account', 'report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'data/data_financial_report.xml',

        'views/views.xml',
        'views/res_company_view.xml',

        'views/general_ledger_view.xml',
        'views/partner_ledger_view.xml',
        'views/trial_balance_view.xml',
        'views/partner_ageing_view.xml',
        'views/financial_report_view.xml',

        'wizard/general_ledger_view.xml',
        'wizard/partner_ledger_view.xml',
        'wizard/trial_balance_view.xml',
        'wizard/partner_ageing_view.xml',
        'wizard/financial_report_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'account_dynamic_reports/static/src/js/script.js',
            'account_dynamic_reports/static/src/js/select2.full.min.js',
            'account_dynamic_reports/static/src/js/action_manager.js',
            'account_dynamic_reports/static/src/scss/dynamic_common_style.scss'
        ],
    },
    'qweb': ['static/src/xml/view.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
