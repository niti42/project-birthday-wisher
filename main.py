import smtplib
import pandas as pd
import datetime as dt
import random

my_email = "nithishkr62@gmail.com"
password = "hmkauryxkqiantxo"  # nithishkr62


def get_birthday_letter(to_name):
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    from_name = "Nithish"

    template_file = random.choice(letters)
    with open(f"letter_templates/{template_file}", "r") as f:
        template = f.read()

    birthday_letter = template.replace(
        "[NAME]", to_name).replace("Angela", from_name)

    return birthday_letter


def send_email(subject, message, to_email, user_email, user_password, email_provider="smtp.gmail.com"):
    """email_provider: Gmail (smtp.gmail.com), Yahoo (smtp.mail.yahoo.com), 
    Hotmail (smtp.live.com), Outlook (smtp-mail.outlook.com)"""
    with smtplib.SMTP(email_provider) as connection:  # gmail smtp server
        connection.starttls()  # for encryption
        try:
            connection.login(user=user_email, password=user_password)
            connection.sendmail(from_addr=user_email,
                                to_addrs=to_email,
                                msg=f"Subject:{subject}\n\n{message}")
            print(f"Message Sent to {to_email}!")
        except:
            print("Error! Message not sent")


today_date = f"{dt.datetime.today().month}-{dt.datetime.today().day}"
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthdays_df = pd.read_csv(r'birthdays.csv')
birthdays_dict = birthdays_df.to_dict(orient="records")

for row in birthdays_dict:
    birthdate = f"{row.get('month')}-{row.get('day')}"
    if today_date == birthdate:
        letter = get_birthday_letter(row.get('name'))
        send_email(subject="Happy Birthday!!!",
                   message=letter,
                   to_email=row.get('email'),
                   user_email=my_email,
                   user_password=password)
