# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:12:30 2020

@author: svea_
"""
from bs4 import BeautifulSoup
import urllib.request
import re
import string

url_list = []

def make_url (season, no_episodes_start, no_episodes_end, url_list):
    url = r"https://crazy-internet-people.com/site/gilmoregirls/pages/s"
    url = url +str(season) + "/s" + str(season) + "s/"
    for i in range(no_episodes_start, no_episodes_end):
        url_list.append(url + str(i+1) + ".html")
        
season_1 = [] 
season_2 = []
season_3 = []
season_4 = []
season_5 = []
season_6 = []
season_7 = []

def get_dialogue(url_list, dialogue_list):
    for i in url_list:
        url = urllib.request.urlopen(i)
        content = url.read()
        soup = BeautifulSoup(content, 'lxml')
        all_p = soup.findAll("p")
    
        #dialogue is in second paragraph
        raw_dialogue = all_p[1]
    
        #only retain the text not the html tags
        dialogue = raw_dialogue.text
        dialogue = dialogue.replace("\t", " ").replace("\n", " ").replace("\x92", "")
        #dialogue = re.sub(r'\b[A-Z]+\b', ' ', dialogue) activate this if names
        #are not needed
        dialogue = re.sub("[\(\[].*?[\)\]]", " ", dialogue)
        
        dialogue = re.sub(r"n\'t", " not", dialogue)
        dialogue = re.sub(r"\'re", " are", dialogue)
        dialogue = re.sub(r"\'s", " is", dialogue)
        dialogue = re.sub(r"\'d", " would", dialogue)
        dialogue = re.sub(r"\'ll", " will", dialogue)
        dialogue = re.sub(r"\'t", " not", dialogue)
        dialogue = re.sub(r"\'ve", " have", dialogue)
        dialogue = re.sub(r"\'m", " am", dialogue)
        
        translator = str.maketrans('', '',      string.punctuation)
        out = dialogue.translate(translator)
    
        dialogue_list.append(out)
   
def save_dialogue (dialogue_list, file_name):
    wordList = []
    for i in range(21):
        episode = re.sub("[^\w]", " ",  dialogue_list[i]).split()
        wordList.append(episode)
    
    with open(file_name,'w') as f:
        for item in wordList:
            f.write(' '.join(map(str, item)))
            f.write("\n")