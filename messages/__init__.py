import logging
import requests
import os 
import json
import yaml
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import traceback
import sys


class CustomFormatter(logging.Formatter):
    grey = '\033[95m'
    OKGREEN = '\033[92m'
    yellow = '\033[93m'
    bold_red = '\033[91m'
    reset = '\033[0m'
    red = "\x1b[31;1m"
    UNDERLINE = '\033[4m'
    format = "%(asctime)s - %(message)s - line %(lineno)d - %(funcName)s"


    # format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s from file - %(filename)s: line %(lineno)d from - %(funcName)s() in %(module)s"
    # format = "%(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
    FORMATS = {
        logging.DEBUG: UNDERLINE + format + reset,
        logging.INFO: OKGREEN + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def handle_excepthook():
    traceback.print_last(file=open('./test-script.txt',"a"))




sys.excepthook = handle_excepthook
class notification(CustomFormatter):
    def __init__(self, logger=None,**kwargs):
        self.logger = logger if logger else logging.getLogger(self._get_logger_name())
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())
        self.logger.propagate = False
        self.logger.handlers[0].setFormatter(CustomFormatter())
        if kwargs.get('file'):
            self.notification_config = self.logfile(file=kwargs.get('file'))
            if self.notification_config:
                config = yaml.safe_load(open(f'{self.notification_config}'))
                for information in config:
                    if information == 'notifications':
                        self.notify = config[information]


    def send_mail(self,message,subject):
        msg = MIMEMultipart()
        msg['From'] = self.notify[1]['email']['from']
        msg['To'] = self.notify[1]['email']['to']
        msg['Subject'] = subject
        message = str(''.join(message))
        msg.attach(MIMEText(message))
        
        mailserver = smtplib.SMTP(self.notify[1]['email']['smtp_host'], self.notify[1]['email']['smtp_port'])
        # identify ourselves
        mailserver.ehlo()
        # secure our email with tls encryption
        if self.notify[1]['email']['smtp_tls']:
            mailserver.starttls()
            mailserver.ehlo()

            # mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.login(self.notify[1]['email']['smtp_username'], self.notify[1]['email']['smtp_password'])
        mailserver.sendmail(self.notify[1]['email']['from'],self.notify[1]['email']['to'], msg.as_bytes())
        mailserver.quit()
        return self
        


    def send_message(self,message):
        data = {
            'text': message,
            'bot_id': self.notify[0]['groupme']['bot_id']
            
        }
        
        info = json.dumps(data)
        response = requests.post('https://api.groupme.com/v3/bots/post', data=info)
        if response.status_code == 202:
            pass

        else:
            #TODO, handle error and send email when groupme is down or errors.
            print(response.text)
        return self
    


    def logfile(self, file):
        if(not os.path.isfile(file)):
            notification().logger.error("config file not found for notifications. Provide a absolute path to the config file or full path to the file")
        else:
            return file
    
    
    def send(self,message):
        return self
    
    def logs(self,level, message):
        return  self.logger
        
    def _get_logger_name(self):
        return self.__class__.__name__
    