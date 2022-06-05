import datetime
import smtplib
from email.message import EmailMessage
import pandas as pd
import os

class EmailSender:
    def __init__(self) -> None:
        self.email_addr = str(os.getenv('EMAIL_ADDR'))
        self.email_pwd = str(os.getenv('EMAIL_PWD'))
        
    def send_email_to_self(self, query_df):
        today_date = datetime.datetime.today().strftime('%Y-%m-%d')
        msg = EmailMessage()
        msg['Subject'] = f'{today_date} stock analysis results'
        msg['From'] = self.email_addr
        msg['To'] = self.email_addr
        msg.set_content('analysis file attached')

        # excel_file = query_df.to_excel(f'{today_date}_results.xlsx')

        msg.add_attachment(query_df, maintype="application", subtype="xlsx", filename=f'{today_date}_results')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email_addr, self.email_pwd)
            smtp.send_message(msg)
