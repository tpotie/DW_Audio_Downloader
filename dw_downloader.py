""" DW German Course Audio Downloader
    Supplementary tool that aids in downloading spoken, (high quality audio from DW), 
    pronunciation that can be used in creating personal flash cards or other learning aids.
    Tested with the Nico's Weg course provided by Deutsche Welle (https://learngerman.dw.com/en/overview)
    Copyright (C) 2018  Electrobub (TimP)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    This program is not endorsed, sponsored or affiliated with DW (Deutsche Welle) or their partners.    
"""
# Added recursive downloading from course list page
# Added more word cleanups (for irregular cases)
# Added file check (if it already exists, skip download)
# Added output folder

from requests import get, codes
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import argparse
import os.path

# Example url: "https://learngerman.dw.com/en/wem-geh%C3%B6rt-das/l-37372077/lv"

def main():
    parser = argparse.ArgumentParser(description="An audio file downloader for the DW Nico's Weg German Learning course")

    parser.add_argument('URL', help="URL of a vocabulary page from https://learngerman.dw.com (Nico's Weg) ")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--list', help="List all available words with audio files from the given URL", action="store_true")
    group.add_argument('-d', '--detail', help="Detailed List. Like --list but adds complete text as well (plural and article)", action="store_true")
    group.add_argument('-w', '--word', help="Download the audio file of the specified word only")
    group.add_argument('-a', '--all', help="Download all audio files from the vocabulary list", action="store_true")
    parser.add_argument('-r', '--recursive', help="Provide the course page (eg A1) and it will recursively download all audio of included lessons", action="store_true")
    parser.add_argument('-o', '--output', help="Output folder for audio files. If not set, they are downloaded to the current directory.")
    
    args = parser.parse_args()

    url = args.URL

    if (args.recursive):
        parse_course_list(url, args)
    else:
        parse_vocab_list(url, args)

def parse_course_list(url, args):
        tempUrl = urlparse(url)
        rootUrl = tempUrl.scheme+"://"+tempUrl.netloc

        response = get(url)
        if response.status_code == codes.ok:
            #html = BeautifulSoup(response.content, 'lxml')
            html = BeautifulSoup(response.content, 'html.parser')
            for snippet in html.select("div.col-sm-12.col-lg-3"):
                sectionText = snippet.h2.get_text()
                seNum, seTitle = sectionText.split(" ", 1)
                print(seNum+ ". Section: "+seTitle.ljust(36)+'#'*(20))
                
                for chaptercode in snippet.find_all('a', attrs={"data-lesson-id": True}):
                    #chTitle = chaptercode.h3.get_text() # Quote from episode in German (More useful to use the English title given later?)
                    chUrl = chaptercode.get('href')
                    chTitle = chaptercode.find('span', class_='title').get_text()

                    print("\t"+chTitle.ljust(40)+"-"*(20))
                    urlVocabList = rootUrl + chUrl + "/lv"
                    print(urlVocabList)
                    parse_vocab_list(urlVocabList, args)
        else:
            raise Exception('Problem with specified URL')


def parse_vocab_list(url, args):
    response = get(url)
    if response.status_code == codes.ok:
        #html = BeautifulSoup(response.content, 'lxml')
        html = BeautifulSoup(response.content, 'html.parser')
        for snippet in html.select("a.audio-wortschatz-link.audio-link"):
            text = str(snippet.strong.string)
            # For stripping the word from the text, take into consideration
            # 1: Nouns with , before the plural / article, eg. Bestellung, -en (f.)
            # 2: Words with (etwas) before them, eg. (etwas) lernen
            # 3: Nouns that do not change in the singular or plural, eg. Papier (n.)
            # 4. Some words have extra blankspace. Also remove periods (.)
            # 5. Strip etwas AND jemanden from words, as they are not represented in audio file.
            # …
            word = text.split(',')[0].split(') ')[-1].split(' (')[0].strip(' .').split('etwas ')[-1].split('jemanden ')[-1]
            url = snippet.source.get('src')
            # Problems with words presented in an irregular formatting, such as  'jemanden/etwas kennen'
            # Check if '/' char and avoid. The words identified like this, have already been downloaded in any case. 
            if '/' in word:
                print("Skipped word: "+word)
                continue

            if (args.list):
                print(word)
            if (args.detail):
                print(word.ljust(20)+'\t\t\t'+text)
            if (args.all) or (args.word == word):
                get_save(url, word, args)                
    else:
        raise Exception('Problem with specified URL')


def get_save(url, name, args) :
    """Provide the url to download from
    and a name (without extension) to rename
    the file to"""
    if (args.output):
        outFolder = args.output
        if not os.path.exists(outFolder):
            os.makedirs(outFolder)
    else:
        outFolder = ''

    if (name):
        ext = url.rsplit('.', 1)[1]
        filename = name + "." + ext
    else:
        filename = url.rsplit('/', 1)[1]
    filename = outFolder + "/" + filename

    if (os.path.isfile(filename)):
        print("File: "+filename+" already exists. Skipping.")
    else:
        response = get(url)

        if response.status_code == codes.ok:
            open(filename, 'wb').write(response.content)
            print("Downloaded: "+name) 
        else:
            raise Exception('Problem downloading file: ' + name)

if __name__ == "__main__":

    main()