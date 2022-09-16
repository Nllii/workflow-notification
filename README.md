# workflow-notification
script  i use to send notification and logs  to email, groupme and siasky.


# pretty logs
https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output?page=1&tab=scoredesc#tab-top

config file
``` 

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

```

# Usage 
```
see test_notification.py for example
```



