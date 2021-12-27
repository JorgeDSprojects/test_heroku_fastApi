# main driver app
from app.fastapp import app
import uvicorn
if __name__=='__main__':
    uvicorn.run(app)
    

"""
Ensure your create an app on heroku and then follow the command below:

0) pip freeze > requirements.txt
1) login heroku login -i
2) initiate git: git init
3) heroku git:remote -a <app name>
4) git add .
5) git commit -am "flask-app"
6) git push heroku master 
7) Test your api on postman
"""
"""
Ensure your create an app on heroku and then follow the command below:
https://codigofacilito.com/articulos/deploy-flask-heroku
0) pip freeze > requirements.txt
1) heroku login
2)heroku create <nombre de tu aplicación heroku>
3) heroku git:remote -a <nombre de tu aplicación heroku>
4)initiate git: git init
4) git add .
5) git commit -am "fastapp"
6) git push heroku master 
7) Test your api on postman
heroku git:remote -a appflask292

"""
