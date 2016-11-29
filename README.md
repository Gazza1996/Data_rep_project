# data_rep_project
Third Year Software Development Data Representation &amp; Querying Project

##** Project Brief **
> You are required to develop a single-page web application(SPA) [7] written
in the programming language Python [1] using the Flask framework [6].
You must devise an idea for a web application, write the software, write
documentation explaining how the application works, and write a short user
guide for it.

My app will be a bucket list app where a user can sign up, sign in, create a new item to their bucket list and then logout again and save as many items to the list as they want.

I first started my project by researching different web app ideas on github and the google search engine. I had many different ideas such as a currency converter, a percentage calculator and then my final idea a bucket list.


To start my project i first had to install the different flask packages needed to run the python files.
// edit here
After this i began creating my index.html file by using a bootstrap method called Jumbotron which i found on the bootstrap website to design my application. I then defined a method in my data.py file in order to run the file in my browser.

I then further designed my html by adding a new signin.html file where i can sign in as a user. I once again used the bootstrap jumbotron method. I then had to create a new function in data.py to call the html file. And also created my bucketList.html file which provides the user with a textarea to enter a title and also a description area to write up a new item which they wish to add to their bucket list. I then created a method in my data.py file in order to allow the html files to run in the localhost.

I created my database then in table.py which created bucketlist.db in my data_rep folder. I went on to create dummy.py which is a python file that runs in the background to allow input of user in the sign in method.


For my project i used different tutorial videos on youtube that taught me how to operate Python, Flask and HTML
I also used the following links as guidelines:																
- (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)												
- (http://www.w3schools.com/bootstrap/default.asp)																
- (http://stackoverflow.com/)																		
- (http://www.w3schools.com/css/)																		
- (http://mindmapengineers.com/mmeblog/creating-web-app-scratch-using-python-flask-and-mysql-part-3)									

##** Programs used **
For my project i used two different programs. One was by JetBrains called PyCharm which i used to create my python files and which also created my database for me by creating a python file and running it in a command line
```
python table.py
```
I also used notepad++ to create all of my html programs. I could have also used notepad++ to create my python files but after discovering pycharm on the jetbrains website i decided that it was a better option as it provided me with the flask framework already pre-installed and was much better formatted and more user friendly for a first time python user.
