# Dictionary Bot
### The Twitter Bot **@ADictionaryBot**

Here is the code for my Twitter **Dictionary Bot**.
You can view and experiment with the code, but I don't recommend launching a Dictionary Bot similar to mine unless you change key features; Twitter users typically will only follow one account/bot if there are multiple providing the same service.


# Libraries Used

I used **PyDictionary** to get the definitions - however this does not have all of the definitions for the 370k+ words the program has access to. In a case that a word without a definition is chosen, it'll skip to another word.

I used **Tweepy** to access Twitter - it's a very simple module to access Twitter through Python. It uses Twitter APIs, so your account will have to be a Twitter developer to get those APIs. Tweepy has a large amount of uses, but I only use the Tweet functionality. It also is able to stop the program if the Tweet has already been sent. (This can be handled via the program istelf, but as the bot is not going to Tweet the same word/definition regularly, it's not needed as of now.)

I used **Random** to choose a random word - this is pretty simple and I'm sure most people who have used Python have used this at some point. Essentially, it picks a random word from *words.txt* and then adds it to a variable.

# Other

*words.txt* is a text file with 370,103 words. This was sourced from *https://github.com/dwyl/english-words* under the file name **words_alpha.txt**. (Note: for simplicity reasons, I renamed the sourced file **words_alpha.txt** to **words.txt** so don't get confused. In short, the file here **words.txt** *is* **words_alpha.txt**.) It's unnecessary in this case to use the sourced file **words.txt** as the program doesn't need a ton of data, and **words_alpha.txt** is sufficient for this use. Sorry if this is confusing!
