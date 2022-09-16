from messages import notification
import traceback


_credentials = "notification-config.yaml"
def test_credentials():
    try:
        raise Exception('test credentials')
    except Exception as e:
        notification().logfile(file=_credentials)
        
        
        
def test_send_email():
    try:
        raise Exception('test send email')
    except Exception as e:
        message_config = notification(file=_credentials)
        message_config.send_mail(message=traceback.format_exc(),subject='test email')
        

def test_groupme():
    try:
        raise Exception('test groupme')
    except Exception as e:
        message_config = notification(file=_credentials)
        message_config.send_message(message=traceback.format_exc())
        
        
def test_logs():
    try:
        message = notification(file=_credentials)
        message.logger.info('test info')
        message.logger.debug('test debug')
        message.logger.warning('test warning')
        message.logger.error('test error')
        message.logger.critical('test critical')
        # message.logger.exception('test exception')
        # message.logger.log(1,'test log')
    except Exception as e:
        # print("test_logs: {}".format(traceback.format_exc()))
        message.logger.exception(traceback.format_exc())
