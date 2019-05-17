## Basic currency converter in Python
### using PyQt5 GUI
------------------------

This project is my first attempt at a Python app with a proper GUI.

This also contains my first, simple web crawler.

The script to execute is **currency_main.py**. It will draw the window with the UI, from where the crawler can be accessed via button.

The crawler will access the ECB website and create the following file in the same folder it is in:

```
rates_table.csv
```

The file is structured as follows:
```
Date;EUR to SEK;EUR to USD;1 SEK in EUR;1 USD in EUR;100 SEK in EUR;100 USD in EUR
2019.05.03;10.704;1.115;0.0934;0.896;9.34;89.64
```

The important columns are 2 and 3; they will be read and parsed as **float**.

You can also use your own csv file containing rates instead of crawling the ECB site.

## Dependencies

The following modules are needed for this script to run:

```
requests
os
bs4
re
datetime
time
csv
sys
qtpy
PyQt5
```

## This script is a work in progress.
Use it at our own risk. It will try to **read** the file you select, and it will try to **write** the crawled
rates into the file **rates_table.csv**. Also, it's probably a good idea to not crawl the website in quick succession (TODO: 
learn more about the DOs and DON'Ts of crawling :smile:)


### TODO:
- [ ] Implement a weekend/holiday check, warn user if rates haven't been updated yet
- [ ] Check for all possible errors
- [ ] Let user choose any currency and try and crawl it
- [ ] Let user choose a time period to crawl
- [ ] Make a nicer GUI


### Acknowledgments:
- Stack Overflow for info on how to redraw the GUI before returning to the main function
- Udemy Python course
- Twitter and #100DaysOfCode for the constant motivation
