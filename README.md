# girlfriend-goodnight-bot 🤖


Python script that sends goodnight messages when you fall asleep. 

Writen using [fbchat](https://github.com/carpedm20/fbchat) lib.



## 🌈 Idea 🌈
The idea is to run the script before the bed (you can put it on RaspberryPi and schedule time for auto-running).
Script reads your last message tat you've sent, and if there are no messages older than 5 mins, bot starts typing instead of you.
Bot is able to send randomized messages(taken out of array of predefined messages), log you out and shutdown your computer.



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



if you have some problems or ideas for improvements feel free to contact me on `fr1sk@live.com`
