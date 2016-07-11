# Statspup
This bot makes pawsitively terrier puns abone statistics.

# About
This bot is still in alpha.

# To Use
## Step 1:
Review, change, or add puns to "Word Replacements" in `pupdictionary.py`
Format is for changing puns is 'existing word':'pun' so "Algorithm" is changed to "algrrrrrythm" with `'algorithm': 'algrrrrrrrithym'`

## Step 2:
Paste text to be parsed in `raw_statspupsays.txt` Later this will be updated with how to automatically scrape from wikipedia pages of your choice.

## Step 3:  
Run the command `python pupdictionary.py`  
This parses the raw text and replaces it with puns.  The parsed output text of `statpupsays.txt` is then chunked for twitter using NLTK library. You will get the message "DONSIES" when its complete. 

## Step 4:  
Check the output file of `statspup_chunks.txt`  
If you see `\n` that means the line is 140 characters.
If you see `SPLIT` then you need to fix that line otherwise you'll get an error from Twitter API that the tweet is too long.

## Step 5:
Now you're ready to tweet. Run `python barkbark.py` (Here named `barkbark_forgithub.py` so you can see how to enter authkeys).  Either leave it running in the background via a rasberry pi or a chron task scheduler.
