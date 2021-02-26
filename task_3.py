# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

class SendgridAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_message(self, message):
        print(f'Send message "{message.subject}" to {message.to_emails}')


class Mail:
    def __init__(self, to_emails, subject, content):
        self.to_emails = to_emails
        self.subject = subject
        self.content = content


class MailClient:
    def __init__(self, api_key, mail_backend='sengrid'):
        self.mail_backend = SendgridAPIClient(api_key=api_key) if mail_backend == 'sengrid' else None

    def send_message(self, mail):
        self.mail_backend.send_message(mail)


class Customer:
    def __init__(self, email):
        self.email = email


class Settings:
    SENDGRID_API_KEY = 'MY_API_KEY'


class Order:
    customer = Customer('ikozheko@gmail.com')
    settings = Settings()

    def ship(self):
        mail = Mail(to_emails=self.customer.email, subject='Вот ваш курс', content='Удачи в прослушивании')
        mail_client = MailClient(Order.settings.SENDGRID_API_KEY)
        mail_client.send_message(mail)


class Reminder:
    customer = Customer('ikozheko@gmail.com')
    settings = Settings()

    """ Вопрос о покупке спустя время"""
    def notify(self):
        mail = Mail(to_emails=self.customer.email, subject='Как вам курс?', content='Расскажите, что нам улучшить?')
        mail_client = MailClient(Reminder.settings.SENDGRID_API_KEY)
        mail_client.send_message(mail)


order = Order()
order.ship()


reminder = Reminder()
reminder.notify()
