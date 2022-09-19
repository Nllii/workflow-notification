# from logging import WARNING
from secret_assistant import notification
import traceback
import sys

notification("critical - message").critical().sendmessage().send_mail()
