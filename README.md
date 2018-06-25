## DW German Audio Downloader

This is a supplementary program to help you in your German language studies.
It is to be used with the (excellent) Deutsche Welle free German Language Learning resources that are found at https://learngerman.dw.com/en/overview

It has been tested with the Nico's Weg course. It works by being fed the URL of a vocabulary list, that is provided at the end of a section and provides you with options to download the pronunciation files (which are clear, concise and presented in a regular pattern throughout the course).
The pronunciation files can then be used with a supplementary learning aid, such as the creation of personal flash cards (using a free program such as Anki).


(This script came about because after each chapter I found myself digging through the code so I could get the pronunciation files that were used to teach new words and to add them to my personal German flashcards. This script just saves a bit of time.)

## Requirements

This script uses the following libraries:

 - BeautifulSoup (for webscraping)
 - requests (for GET requests)
 

```$ sudo pip install beautifulsoup4 requests```

It has been tested on Linux (should work on Windows / Mac if the requirements are met)

## Usage

The script itself is very simple, therefore its usage should be very simple!

    $ python ./dw_downloader --help
    usage: dw_downloader.py [-h] [-l | -d | -w WORD | -a] URL  
      
    An audio file downloader for the DW Nico's Weg German Learning course  
      
    positional arguments:  
    URL 		URL of a vocabulary page from https://learngerman.dw.com (Nico's Weg)  
      
    optional arguments:  
    -h, 		--help 			show this help message and exit  
    -l, 		--list 			List all available words with audio files from the  
    given URL  
    -d, 		--detail 		Detailed List. Like --list but adds complete text as  
    well (plural and article)  
    -w 	WORD, 	--word WORD 	Download the audio file of the specified word only  
    -a, 		--all 			Download all audio files from the vocabulary list

Files are downloaded to the directory the script is located in. 

   
## Examples

### List all words 

    $ python dw_downloader.py https://learngerman.dw.com/en/wem-geh%C3%B6rt-das/l-37372077/lv -l
    Ordner 		 
    ein 	
    eine
    Bestellung
    Jahr  
    Wort
    lernen  
    lesen 
    Text  
    üben 
    Pause 

### List all words (detailed)

    $ python dw_downloader.py https://learngerman.dw.com/en/wem-geh%C3%B6rt-das/l-37372077/lv -d  
    Ordner 		Ordner, - (m.)  
    ein 		ein  
    eine 		eine  
    Bestellung 	Bestellung, -en (f.)  
    Jahr 		Jahr, -e (n.)  
    Wort 		Wort, Wörter (n.)  
    lernen 		(etwas) lernen  
    lesen 		(etwas) lesen  
    Text 		Text, -e (m.)  
    üben 		(etwas) üben  
    Pause 		Pause, -n (f.)  
   
### Download a specific word

    $ python dw_downloader.py https://learngerman.dw.com/en/wem-geh%C3%B6rt-d  
    as/l-37372077/lv -w Wort 
    Downloaded: Wort 

	$ python dw_downloader.py https://learngerman.dw.com/en/wem-geh%C3%B6rt-d  
    as/l-37372077/lv -w Text 
    Downloaded: Text  
     

### Download all words

    $ python dw_downloader.py https://learngerman.dw.com/en/wem-geh%C3%B6rt-d  
    as/l-37372077/lv -a  
    Downloaded: Ordner  
    Downloaded: ein  
    Downloaded: eine  
    Downloaded: Bestellung  
    Downloaded: Jahr  
    Downloaded: Wort  
    Downloaded: lernen  
    Downloaded: lesen  
    Downloaded: Text  
    Downloaded: üben  
    Downloaded: Pause  

Hope this script proves useful to somebody else!

Happy (German) Language Learning!
 
Licenced under the GPL v3