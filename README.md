# girlfriend-goodnight-bot

===
Python script that sends goodnight messages when you fall asleep. 
Writen using https://github.com/carpedm20/fbchat lib.

===

## 🌈 Idea 🌈
You turn on the script before the bed (you can put it on RaspberryPi and schedule time for auto-running)
It reads your last message that you sent and if there is no messages longer than 5 minutes, bot starts to helping you.
He sends randomized message form array of messages, logs you out, and shutdown your computer.

===

## 📦 Installation & configuration 📦

Install dependencies using pip `pip install fbchat`
Edit attributes in script: 
* `uname` -- your facebook username
* `passwd` -- your facebook password
* `id` -- your girlfriend ID (int value)
* `myId` -- your ID (unicode value)

Fill arrays with your own sentences that will be sent randomly:
* `reason` -- array of reasons why are you going to sleep
* `emoticon` -- array of FB emoticons
* `night` -- array of good night messages
* `love` -- array of love messages

And finally: `python bot.py` 

===

if you have some problems or ideas for improvements feel free to contact me on `fr1sk@live.com`
