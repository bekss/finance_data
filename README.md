# finance_data
Automation of data collection and distribution

# finance_data
Automation of data collection and distribution
# Installation GUIDE 
web site for data scrapy and return json 
0. python < 3.7
1. pip install pipenv
2. pip install sync
3. pipenv shell
In Windows Terminal:  
cd finance  
python manage.py migrate  
python manage.py createsuperuser  
python manage.py runserver  

After http://127.0.0.1:8000/   -  choose a file which have a link  
txt file is here:  finance/media/comp.txt  

After prossecing with txt file:  
http://127.0.0.1:8000/json/pins/  -  returns json data for company PINS  
http://127.0.0.1:8000/json/zuo/  -  returns json data for company ZUO  

http://127.0.0.1:8000/detail    - you can find here csv file of company as ZUO, PINS
