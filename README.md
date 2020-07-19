# DW German Audio Downloader

This is a supplementary program to help you in your German language studies.
It is to be used with the (excellent) Deutsche Welle free German Language Learning resources that are found at https://learngerman.dw.com/en/overview

It has been tested with the Nico's Weg course. It works by being fed the URL of a vocabulary list (that is provided at the end of a section) or a whole course list (eg. course for A1) and provides you with options to download the pronunciation files (which are clear, concise and presented in a regular pattern throughout the course).
The pronunciation files can then be used with a supplementary learning aid, such as the creation of personal flash cards (using a free program such as Anki).

(This script came about because after each chapter I found myself digging through the code so I could get the pronunciation files that were used to teach new words and to add them to my personal German flashcards. This script just saves a bit of time.)

## Changelog

V0.2c:

- Changed all filepaths to use os.path

V0.2b:

- Replaced invalid Window filename chars with valid alternatives

V0.2a:

- Updated for DW page changes (course list)

V0.2:

- Added recursive downloading from course list page
- Added more word cleanups (for irregular cases)
- Added file check (if it already exists, skip download)
- Added output folder

## Requirements

This script uses the following libraries:

- BeautifulSoup (for webscraping)
- requests (for GET requests)

```$ sudo pip install beautifulsoup4 requests```

It has been tested on Linux (should work on Windows / Mac if the requirements are met), with the A1 Nico's Weg course (should work with other levels if the files are presented the same way).

## Usage

The script itself is very simple, therefore its usage should be very simple!

    $ python dw_downloader.py --help
    usage: dw_downloader.py [-h] [-l | -d | -w WORD | -a] [-r] [-o OUTPUT] URL

    An audio file downloader for the DW Nico's Weg German Learning course

    positional arguments:
      URL                           URL of a vocabulary page from
                                    https://learngerman.dw.com (Nico's Weg)

    optional arguments:     
      -h,           --help          show this help message and exit
      -l,           --list          List all available words with audio files from the
                                    given URL
      -d,           --detail        Detailed List. Like --list but adds complete text as
                                    well (plural and article)
      -w WORD,      --word WORD     Download the audio file of the specified word only
      -a,           --all           Download all audio files from the vocabulary list
      -r,           --recursive     Provide the course page (eg A1) and it will
                                    recursively download all audio of included lessons
      -o OUTPUT,    --output OUTPUT
                                    Output folder for audio files. If not set, they are
                                    downloaded to the current directory. 

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
    Ordner      Ordner, - (m.)  
    ein         ein  
    eine        eine  
    Bestellung  Bestellung, -en (f.)  
    Jahr        Jahr, -e (n.)  
    Wort        Wort, Wörter (n.)  
    lernen      (etwas) lernen  
    lesen       (etwas) lesen  
    Text        Text, -e (m.)  
    üben        (etwas) üben  
    Pause       Pause, -n (f.)  

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

### Recursive

All recursive downloads can use the existing switches (eg. --list and --detail)

### Download all audio files from a whole course list (for eg. A1 course) recursively. To specified output folder

    $ python dw_downloader.py https://learngerman.dw.com/en/beginners/c-36519789 -ra -o audio_files
    1. Section: Welcome!                            ####################
            Greetings                               --------------------
    https://learngerman.dw.com/en/hallo/l-37250531/lv
    Downloaded: Wie geht es dir?
    Downloaded: Wie geht es Ihnen?
    Downloaded: Es geht mir gut
    Downloaded: sehr gut
    Downloaded: super
    Downloaded: gut
    Downloaded: nicht
    Downloaded: danke
    Downloaded: Und Ihnen?
    Downloaded: auch
    Downloaded: Und dir?
    Downloaded: Herr
    Downloaded: Frau
    Downloaded: oder

Hope this script proves useful to somebody else!

Happy (German) Language Learning!

Licenced under the GPL v3
