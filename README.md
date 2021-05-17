# finance_data
Automation of data collection and distribution
# Installation GUIDE 

Web site for data scrapy and return json  

0. python < 3.7
1. pip install pipenv
2. pip install sync
3. pipenv shell


### First navigate to this folder:
##### finance/finance/selen.py 
##### command:  
#####  python selen.py  -- for collecting a url of company from web site to company.txt file 
##### Folder for Csv is here -- finance/media/received_csv
##### Folder for url from site is here -- finance/media/company_name
##### Folder for Chrome bot is here --  finance/media/chrome_exe/chromedriver.exe
##### Version Chrome -- 90.0.4430.212
### Сhange settings databases here to your own -- finance/finance/settings.py:
### Change posgresql data here function commit_psql  -- finance/company/request.py 

In Windows Terminal: 
Then go to your home folder   
cd finance  
python manage.py migrate  
python manage.py createsuperuser  
python manage.py runserver  

After http://127.0.0.1:8000/   -  choose a file which have a link  
txt file is here:  finance/media/company.txt  

After prossecing with txt file:  
http://127.0.0.1:8000/json/pins/  -  returns json data for company PINS  
http://127.0.0.1:8000/json/zuo/  -  returns json data for company ZUO  

http://127.0.0.1:8000/detail    - you can find here csv file of company as ZUO, PINS
