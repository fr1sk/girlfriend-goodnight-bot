import time
import random
import fbchat
from fbchat.models import *
import os
import sys
from pprint import pprint

reload(sys)
sys.setdefaultencoding('UTF8')

uname = "" #your username
passwd = "" #your password
client = fbchat.Client(uname,passwd)


id = 1234567890 #client id
myId = u'0123456789' #your id

reason = ["resaon1", "resaon2", "reason3", "reason4", "reason4"]
emoticon = [":(", ":/", ":O"]
night = ["night1", "night2", "night3", "night4", "night5"]
love = ["love1", "love2", "love3", "love4", "love5"]

uniId = str(id)

def goodNight():
    #todo STICKER

    if(client.sendMessage(random.choice(reason), thread_id=uniId, thread_type=ThreadType.USER)):
        print "Reason: sent"
    else:
        print "Reason: failed"
    time.sleep(random.randint(3, 7))

    if(client.sendMessage(random.choice(emoticon), thread_id=uniId, thread_type=ThreadType.USER)):
        print "Emoticon: sent"
    else:
        print "Emoticon: failed"
    time.sleep(random.randint(3, 7))

    if(client.sendMessage(random.choice(night), thread_id=uniId, thread_type=ThreadType.USER)):
        print "Night: sent"
    else:
        print "Night: failed"
    time.sleep(random.randint(3, 7))

    if(client.sendMessage(random.choice(love), thread_id=uniId, thread_type=ThreadType.USER)):
        print "Love: sent"
    else:
        print "Love: failed"
        time.sleep(random.randint(3, 7))


while(1):
    messages = client.fetchThreadMessages(id, limit=100)
    #getting my last message
    for i in range(0, len(messages)):
        if(messages[i].author == myId):
            myLastMessage = messages[i]
            print "your last message was: " +myLastMessage.text
            break

    timePassed = (int(time.time() - (int(myLastMessage.timestamp))/1000)/60)

    if(timePassed >= 5):
        goodNight()
        client.logout()
        os.system("poweroff")
        break
    else:
        print "time passed: "+timePassed
