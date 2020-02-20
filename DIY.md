# Do It Yourself (DIY)

Hello! If you're here, you probably want to get started with editing this bot for yourself. Here's a simple guide to set up and launch your own bot!

I was running mine from a Raspberry Pi 3 Model B with Raspbrian. It's only got an 8GB Micro SD card, but as you're only storing small text/Python files (*the largest file is words.txt which is still only 4.2MB*) that should leave you with around 1GB of free storage - at least for me, anyway!

I'm now running from [PythonAnywhere](https://www.pythonanywhere.com)

*Note: As said in README.md, "I don't recommend launching a Dictionary Bot similar to mine unless you change key features; Twitter users typically will only follow one account/bot if there are multiple providing the same service."*

## What You'll Need

**-Raspberry Pi (*or a PC running Raspbrian - skip step 1 and follow the tutorial at https://www.techrepublic.com/article/how-to-run-raspberry-pis-raspbian-os-on-a-pc/*)**

**8GB or Larger Micro SD Card (*and a way to connect it to your Mac or PC*)**

**HDMI Monitor/TV (*for setup only - this can be removed once the bot is completed*)**

**Mouse & Keyboard (*for setup only - this can be removed once the bot is completed*)**

**Ethernet or WiFi Dongle (*for Raspberry Pi models without WiFi. Ethernet is more reliable so use this if possible*)**

**Internet Connection (*your Pi needs to connect to Twitter to send Tweets*)**

**USB Drive (*if you do not want to download required files through the Pi itself. Your USB needs to be formatted as FAT or exFAT. Note that exFAT will require a simple installtion to be read*)**

**Termius (*download from https://termius.com - you can also use another SSH client but Termius seems to work best*)**

## Step 1 - Install Raspbrian

Download **Raspbrian** from *https://downloads.raspberrypi.org/raspbian_full_latest*. It's a large download, so give it time.
Extract it using **7Zip** (*Windows, download from https://www.7-zip.org/download.html*) or **The Unarchiver** (*macOS, download from https://dl.devmate.com/com.macpaw.site.theunarchiver/TheUnarchiver.dmg*).
Use **Etcher** (*download from https://www.balena.io/etcher/*) to install the *.img* file you extracted to your Micro SD Card.

## Step 2 - Install Libraries & Python 3

You'll need **PyDictionary**, **Tweepy**, **Random**, **Time**, and **Python 3**.
Random and Time are probably already installed on your system. Python 3 probably is too, but, if it's not and you only have Python 2, you're probably running Raspbrian Lite. Install it by pasting *sudo apt-get install python3* into the Terminal. *If you're back at this step as you are having an issue running your finished code, then be sure that you type **python3 <filename.py>** else you may be running Python 2.*

**Use the commands below to install the other libraries.**
PyDictionary - *pip install PyDictionary*
Tweepy - *pip install Tweepy*

## Step 3 - Get Twitter APIs

Login to *twitter.com* with the account you want to use as the bot and then go to *developer.twitter.com.*. 
(*If you're already a Twitter developer, you can skip this part.*)

Click **Apply** in the top right hand corner.

Click **Apply for a developer account**.

Choose **Making a bot** from the **Hobbyist** column and click **Next**.

Confirm your username and email.

Choose your country, name of your developer account, and select your email preferences.

Press **Next**.

Fill out the fields. I'm unable to help you with this bit as it would be putting my developer account(s) at risk - but good luck! Be honest and explain that you intend to use APIs to experiment with Python.

**Now you have to wait to get approved: this may take a while.**
If you do not get approved, then you will be unable to continue with this tutorial unless you apply and get approved with another account.

Once you are approved (you will recieve an email) go to *developer.twittter.com/apps* and click **Create an app**.

Enter the name of your app. This will be what appears as the "Tweeted From" text:  e.g. Twitter for iPhone or Twitter Web App. 

Add a description of your app. This can be fairly simple.

Add a URL - this can be your Twitter profile URL.

You don't need to add text into any of the other small boxes on the page.

In the last large box, explain how you will use APIs in Python to create a bot to Tweet information at certain intervals. Change this if you have intentions of changing the use of my code.

**Read the Automation Rules. This is extremely important.**

Navigate to the **Keys and tokens** tab.

Click **Create** and get your **Access token and Access token secret**.

Sign into Twitter Developer on your Raspberry Pi (if you're not already) Create a new file called **APIs.txt** in */home/pi*. You can also save them through your PC or Mac and move them over with a USB stick. You'll learn more about this in the next step.

## Step 3 - Download Code

Download all of the files in this repository and save them to */home/pi*. If you've changed your user account name, substitute *pi* for your custom account name. It's easier to keep them all in your root folder as you won't be using this Raspberry Pi for anything else. Again, you can also move them over from your PC or Mac with a USB stick - but be sure to transfer them off of your USB stick.

## Step 4 - Edit Code

This is the fun part! You can now do anything you want to the code - but firstly you must input your Twitter API keys. Open **APIs.txt** and minimise it for the time being.

Open Terminal and type **nano DictionaryBot.py**. Change this if you have renamed your files. If your files aren't in */home/pi*, use **cd** to navigate to that directory.

Move the cursor using your arrow keys to the line **auth = tweepy.OAuthHandler("INSERT YOUR API", "INSERT YOUR API")**. Move to **INSERT YOUR API** and replace each of the placeholders with your APIs - the first two on the Twitter Developer page are the two in the first brackets (line 25) and the last two on the Twitter Developer page are the two in the last brackets (line 26).

Theoretically, your bot should now work. But let me cast your brain back to this quote from *README.MD*: *"I don't recommend launching a Dictionary Bot similar to mine unless you change key features; Twitter users typically will only follow one account/bot if there are multiple providing the same service."*

### This is the point at which I leave you to figure it out yourself: you can either launch your bot as it is (not recommended) or make as many edits as you wish. It's your code now!
#### Don't forget what I said in *README.MD*. 

# Enjoy your bot!
