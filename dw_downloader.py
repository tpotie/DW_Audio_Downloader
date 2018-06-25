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

from requests import get, codes
from bs4 import BeautifulSoup
import argparse

# Example url: "https://learngerman.dw.com/en/wem-geh%C3%B6rt-das/l-37372077/lv"

def main():
    parser = argparse.ArgumentParser(description="An audio file downloader for the DW Nico's Weg German Learning course")

    parser.add_argument('URL', help="URL of a vocabulary page from https://learngerman.dw.com (Nico's Weg) ")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--list', help="List all available words with audio files from the given URL", action="store_true")
    group.add_argument('-d', '--detail', help="Detailed List. Like --list but adds complete text as well (plural and article)", action="store_true")
    group.add_argument('-w', '--word', help="Download the audio file of the specified word only")
    group.add_argument('-a', '--all', help="Download all audio files from the vocabulary list", action="store_true")

    args = parser.parse_args()

    url = args.URL
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
            word = text.split(',')[0].split(') ')[-1].split(' (')[0]
            url = snippet.source.get('src')

            if (args.list):
                print(word)
            if (args.detail):
                print(word.ljust(20)+'\t\t\t'+text)
            if (args.all) or (args.word == word):
                get_save(url, word)
                print("Downloaded: "+word)                 
    else:
        raise Exception('Problem with specified URL')

def get_save(url, name = '') :
    """Provide the url to download from
    and an optional name (without extension) to rename
    the file to"""
    if (name):
        ext = url.rsplit('.', 1)[1]
        filename = name + "." + ext
    else:
        filename = url.rsplit('/', 1)[1]

    response = get(url)

    if response.status_code == codes.ok:
        open(filename, 'wb').write(response.content)
    else:
        raise Exception('Problem downloading file: ' + name)

if __name__ == "__main__":

    main()