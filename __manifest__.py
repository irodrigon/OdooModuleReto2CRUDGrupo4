{
    'name' : 'RovoBank',
    'version' : '1.0',
    'description' : 'The bank that helps you',
    'autor' : 'Grupo4',
    'depends': ['base', 'auth_signup','mail'],
    'data' : [
        'security/rovobank_security.xml',
        'security/ir.model.access.csv',
        'views/rovobankmenu.xml',
        'views/accountView.xml',
        'views/movementView.xml',
        'views/loanView.xml',
        'reports/reportAccount.xml',
        'reports/reportMovement.xml',
        'reports/reportLoan.xml',
        'reports/report_action.xml',
        'reports/report_action_movement.xml',
        'reports/report_action_loan.xml',
        #'views/grupo4AccountsView.xml',
    ]
}

