# Dictionary Bot
### The Twitter Bot **@ADictionaryBot**

Here is the code for my Twitter **Dictionary Bot**.
You can view and experiment with the code, but I don't recommend launching a Dictionary Bot similar to mine unless you change key features; Twitter users typically will only follow one account/bot if there are multiple providing the same service.

You can view a tutorial on how to make this bot yourself in *DIY.md*


## Libraries Used

I used **PyDictionary** to get the definitions - however this does not have all of the definitions for the 370k+ words the program has access to. In a case that a word without a definition is chosen, it'll skip to another word.

I used **Tweepy** to access Twitter - it's a very simple module to access Twitter through Python. It uses Twitter APIs, so your account will have to be a Twitter developer to get those APIs. Tweepy has a large amount of uses, but I only use the Tweet functionality. 

I used **Random** to choose a random word - this is pretty simple and I'm sure most people who have used Python have used this at some point. Essentially, it picks a random word from *words.txt* and then adds it to a variable.

## Words

**words.txt** is a text file with 370,103 words. This was sourced from *https://github.com/dwyl/english-words* under the file name **words_alpha.txt**. (Note: for simplicity reasons, I renamed the sourced file **words_alpha.txt** to **words.txt** so don't get confused. In short, the file here **words.txt** *is* **words_alpha.txt**.) It's unnecessary in this case to use the sourced file **words.txt** as the program doesn't need a ton of data, and **words_alpha.txt** is sufficient for this use. Sorry if this is confusing!

**BlockedWords.txt** contains explicit words from *https://en.wiktionary.org/wiki/Category:English_swear_words* and the bot chooses a new word if one from the list is chosen to be Tweeted.

**UsedWords.txt** contains words that the bot has used - whether or not they had a definition in **PyDictionary** and was thus Tweeted. Adding the word at the stage of choosing it means that the program has less code to get through before realising that a lot of the previous code for defining the word was unneeded if the word can't even be used - this is the same with **BlockedWords.txt**.
