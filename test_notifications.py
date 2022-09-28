from  secret_assistant import notification

notification("testing notifications").info().sendmessage().send_mail()
notification("testing notifications").warning().sendmessage().send_mail()
notification("testing notifications").critical().sendmessage().send_mail()