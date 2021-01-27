from flask import Blueprint, render_template, session, redirect, url_for
from controllers.DbConnector import DbConnector
from mysql.connector import Error
from classes.Card import Card

'''
File name: manage_cards_page.py
Author: Harry Kenny
Credits: Harry Kenny
Date created: 20/01/2021
Date last modified: 25/01/2021
Python version: 3.7
Purpose: Back-end file for allowing the user to transfer money from one account to another
'''

manage_cards_page = Blueprint('manage_cards_page', __name__, template_folder='templates')


@manage_cards_page.route('/', methods=['GET', 'POST'])
def manage_cards_page_func():
    user_id = session['user_id']
    all_user_cards = []
    try:
        db_connector = DbConnector()
        conn = db_connector.getConn()
        cursor = conn.cursor(buffered=True)

        cursor.execute("SELECT * FROM UserCards")
        result = cursor.fetchall()
        for row in result:
            if row[1] == user_id:
                user_card = Card(row[0], row[2], row[3], row[4], row[5])
                all_user_cards.append(user_card)

    except Error as e:
        print(e)
        return redirect(url_for('error_page.error_page_func', code="e2", src="index.html"))

    conn.close()

    return render_template('manage_cards.html', all_user_cards=all_user_cards)


def view_card_info():
    return

