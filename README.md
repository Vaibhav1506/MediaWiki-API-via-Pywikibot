# Remote-Editing-via-Pywikibot
This is a small demo about the remote editing feature you can acheive with Pywikibot. 

## Objective
Let's just say we have a web page about some product or some other items or even a game. What we wanna do is to fetch the statistics related to this particular item and then side - by - edit it on our web page. So for this demonstration we will be taking the Downtown 1930s Mafia Wiki as the web page and its crazy games website as the one from which we will be fetching the statistics. The website has many stats like rating votes, upvotes and downvotes as well as the rating. So instead of updating manually on our wiki page we can just use an automating script for this using the Pywikibot. 

## What is Pywikibot ?
Pywikibot is a Python library and command-line tool designed to automate work on wikis that run on MediaWiki, such as Wikipedia, Fandom, or any MediaWiki-powered site. It allows you to programmatically interact with wiki pages — reading, editing, creating, and organizing content — using scripts. It was originally developed for MediaWiki but now works for any MediaWiki powered site.

## What is MediaWiki and how it works in sync with Pywikibot?
MediaWiki is a free, open-source wiki software platform that powers websites where many users can collaboratively create and edit content. It was originally developed for Wikipedia, but now it is widely used by organizations, communities, and individuals to build knowledge bases, documentation sites, and public or private wikis. MediaWiki and Pywikibot work together through the MediaWiki API — a powerful interface that allows bots to read, edit, and manage content just like a human editor, but programmatically and efficiently. It connects to a MediaWiki API and Pywikibot communicates with the MediaWiki API (e.g., api.php) for retrieving page content, editing pages or uploading files or get any metadata.

## Requirements
The setup uses a Bot Account, that is, you typically create a bot account on the wiki and then authenticate it using the **user-config.py** file which contains the username and family / wiki info.

## Setup
The obvious fact is you are gonna need the pywikibot python library which you can install via **pip3 install pywikibot** which is as simple as that. Now for this particular demo we also need the **Requests** library for **Web-Scraping** the stats from the site. 

### Creating a Bot Account
For working with pywikibot a bot account with administrator or bureaucrat rights is needed. You can create a bot account by registering it on your account or creating a dummy account and going to **Special:BotPasswords** on your own wiki / family. After that you can tweak any of the options of the bot accounts regarding editing, moving, etc. related to the user accounts right and then generate the password which will give you the following :- 


![image](https://github.com/user-attachments/assets/43aacdfa-ec87-40b6-869c-7a780448405f)

where:-
- the text highlighted in red is the bot password.
- the text highlighted in blue is the account name.
- the text highlighted in green is the bot name.

### Creation of the user-config.py
After installing the pywikibot library what you wanna do is to create the **user-config.py** in the workingfolder in which you wanna write the script. The **user-config.py** file in Pywikibot is a required configuration file that tells the bot about your wiki login, preferred language, project family (like Wikipedia, Fandom, etc.), and some behavior preferences. The format is as below :-

    family = 'downtown1930smafia'
    mylang = 'en'
    usernames['downtown1930smafia']['en'] = 'YourBotUsername'
    password_file = "user-password.py"

where:-
- **_family_** variable contains the the wiki project type you're working with. Examples include **'wikipedia'**, **'wiktionary'**, **'wikidata'**, **'fandom'** (for Fandom wikis), etc. and so on.
- **_mylang_** variable is the language code of your target wiki. For example, '**en**' for English, '**fr**' for French, '**de**' for German.
- **_usernames_** variable is actually a a python dictionary that maps family + language to your bot's username.
- **_password_file_** (optional) as we have used in above where it is used to securely store your bot’s login credentials in Pywikibot. It specifies the path to a Python file (usually user-password.py) where your bot's username and password are stored securely. the password file should preferably created in the same directory to avoid any confusions.
   
#### Optional variables 
You can set up optional variables such as the :-
- **_console_encoding_** where you can define the type of encoding. For example a valid syntax can be :-
  
      console_encoding = 'UTF-8'
- **_put_throttle_** where you cam set a pause (in seconds) between each page edit your bot makes. It is a good practice as it prevents overloading the server.

      put_throttle = 5

### Creation of the user-password.py
In this file its recommended to import the BotPassword class so as to write the correct order of the bot name, account name and the password in the format as below :-

     ('yourFandomUsername', BotPassword('yourBotName', 'yourPasswordHere'))
  
Login credentials thus are stored securely via pywikibot login in here and you don't need to give the password repeatedly when performing the task.

### Creation of the family file
Since **Fandom** is a 3rd party wiki - hosting service hosted on MediaWiki platform, it is necessary to add your own family wiki. A **family.py** file tells Pywikibot how to connect to your specific wiki domain — it's like a connection profile. You must define the domain, script path, language codes, API endpoint, etc. **An important thing** to note in this particular file is that you should create the file **inside the root directory of where the pywikibot library** is installed. It should be created inside the path **C:\PathToPywikibot\Pywikibot\families** as family.py or custom_family_name.py with the format given in the file.

    name = 'downtown1930smafia'  
    langs = {
        'en': 'downtown1930smafia.fandom.com',
    }
where :-
- name is the chosen file name.
- langs is the dictionary containing the encoding language as well as the link to the wiki.
  
After all this setup its good to check if you were logged in successfully using the command in the current working directory where you want the script to run:-

    pwb login

The output will be as follows which indicates a successful connection to the website:-

![image](https://github.com/user-attachments/assets/7ab99f94-8bdc-4d8b-bcf2-e634929d4d1d)

Now you will be able to successfully write automation scripts in this directory.

## Use Case 
So as you can see in the stats.py we use requests to **web - scrap** the data required via sending a request to the link and returning the statistics as a list for later usage. In the update.py we import pywikibot as well as the stats.py file. Now for this usage targeted the page at [https://downtown1930smafia.fandom.com/wiki/Template:WikiStatistics](https://downtown1930smafia.fandom.com/wiki/Template:WikiStatistics). 

    pywikibot.Site() ==> Creates a connection to a specific wiki according to the user-config.py
    site.login() ==> Logs in to the site.  
    pywikibot.Page(site, page_url) ==> Allows you to interact with a specific page on the site
    page.text ==> Returns the source code of the page.
    page.save() ==> Saves the page on the server.

Thus Pywikibot performs Actions like a Human Editor Pywikibot simulates what a human editor would do: 
   
    Opens a page → reads text → modifies text → submits it → adds an edit summary → logs the result.

## Automation
For automation you can use **Launchd** for MacOS, **Cron** for Linux, **Task Scheduler** for Windows. In this case since I am using a Virtual Environment I had to write a bash script since I needed to enable the Virtual Environment everytime for running the script. Hence for automation I used the bash script which you can run periodically using any of the softwares as listed earlier with the output being :-

![Screenshot 2025-06-05 131243](https://github.com/user-attachments/assets/2efeb7f1-ea7f-468f-954e-c3b631951188)

The pause at the end of the bash script for just for testing purposes so that's not neccessary because its only purpose is to pause the CMD window instead of closing automatically after it run successfully.
