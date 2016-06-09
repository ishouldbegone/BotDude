# BotDude
[![Build Status](https://travis-ci.org/manparvesh/BotDude.png)](https://travis-ci.org/manparvesh/BotDude) 
![Python](https://img.shields.io/badge/python-2.7-blue.svg) 
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/swapagarwal/JARVIS-on-Messenger/master/LICENSE) 
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/manparvesh/BotDude/) 
[![forages](https://img.shields.io/badge/For%20ages-16%2B-red.svg)](https://img.shields.io/badge/For%20ages-16%2B-red.svg)  
[![forthebadge](http://forthebadge.com/badges/built-with-swag.svg)](http://forthebadge.com)

A facebook messenger bot inspired by the Dude ([The Big Lebowski](http://www.imdb.com/title/tt0118715/))

### Objective

I developed Bot Dude mainly for fun. Moreover, anyone can contribute to this project by suggesting more fun features that can be added or by sending a PR :smile:  
You can take a look at the [contributing guidelines](https://github.com/manparvesh/BotDude/blob/master/CONTRIBUTING.md) for any help required.  
A lot of help wasa taken from Swapnil's (@swapagarwal) project [JARVIS](https://github.com/swapagarwal/JARVIS-on-Messenger).

### Usage

The Dude is now live [here](https://www.messenger.com/t/BotDude). Currently, it's pending approval before the public can engage. If you'd like to be a tester, post [here](https://www.facebook.com/BotDude/posts/190232388040620).

### Sample Queries

`Hi, dude!`  
`Duuuuuude!`  
`:P`  
`Yay!`  
`How are you?`  
`What are you doing?`  
`Do you know about God?`  
`Who made you?`  
`Who is Man Parvesh?`  
`:D`  
`Goodbye dude!`  
`help`  
`Who are you?`  
`Tell me a joke`  
`Tell me a quote`

### Local Development / Testing

1. Clone this repo.
2. `sudo apt-get install python-dev libffi-dev libssl-dev`
3. `pip install -r requirements.txt`
4. `python dude.py`
5. Visit the following URLs to see results:  
`http://localhost:5000/process/?q=<YOUR_QUERY>` returns the intent of the query.  
`http://localhost:5000/search/?q=<YOUR_QUERY>` returns the search result of the query.
