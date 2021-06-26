# Simple Django Blog
>Hello everyone,I was a programman for  two years and a half
## Properties of the project
- ## Simple ##
- Fast
- Light
- Small capacity
```python
print('The blog support markdown')
print('Post in admin page')
```
# How to use
**Ensure that your python version is up to 3.6**  

*this project use django internal admin to manage blog*
1. pip install -r requirement.txt
2. python manage.py migrate
3. python manage.py createsuperuser
4. if you run everything in local, you need to change debug false to true and delete gornicore on installed apps in setting
5. python manage.py runserver

***  

*If you run in server, please self-configure nginx, proxy, gornicore or something*
