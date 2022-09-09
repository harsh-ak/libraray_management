{
    'name' : 'Library Managment',
    'version' : '1.0',
    'sequence': -200,
    'description': "This is an Library Managment Module",
    #'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : [],
    'data': ['security/ir.model.access.csv',
    'views/visitors.xml',
    'views/librarian.xml',
    'views/library_management.xml',
    'views/library_book.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}