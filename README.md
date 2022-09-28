# workflow-notification
used to send notification and logs  to email, groupme and... ~~siasky~~.

```
create a file called dev.notification.yaml and include the required variables
notifications:
  - groupme:
      bot_id: ""
  - email:
      to: ""
      from: ""
      smtp_host: ""
      smtp_port:
      smtp_username: ""
      smtp_password: ""
      smtp_tls: true
      subject: "hello from {{program.notifications}}"

```

# Usage
```
pip install workflow-notification

```

```python
from  secret_assistant import notification

notification("testing notifications").info().sendmessage().send_mail()
notification("testing notifications").warning().sendmessage().send_mail()
notification("testing notifications").critical().sendmessage().send_mail()

```



TODO:
1. siasky for logs sending
2. use trace to hook into stdout for logging .




