from flask import Flask, Blueprint, render_template
from controllers.DbConnector import DbConnector

account_page = Blueprint('account_page', __name__, template_folder='templates')


@account_page.route('/')
def accounts_page():
    db_connector = DbConnector()
    conn = db_connector.getConn()
    db_connector.closeConn(conn)
    user = {'username': 'Hello World'}
    return render_template('accounts.html', title='Home', user=user)