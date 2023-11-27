from datetime import datetime
from decimal import Decimal

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    card_1 = BankCard('1234', 'Vasya Pupkin')
    card_2 = BankCard('4321', 'Vasya Pupkin')
    now = datetime.now()
    date, time = now.strftime('%y.%m.%d %H:%M').split()
    message = SmsMessage(
        f'200 RUB, xxxxxxxxxxxx1234 {date} {time} {date} authcode 1234',
        'user',
        datetime.now()
    )
    expense = Expense(
        Decimal('200'),
        card_1,
        date,
        datetime.strptime(f'{date} {time}', '%d.%m.%y %H:%M')
    )

    assert parse_ineco_expense(message, [card_1, card_2]) == expense
