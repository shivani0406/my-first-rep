# frame works for designing website and api designing

#django
#flask
#fastAPI

#postgresql============by own=======connect using python   ======tssk=====tutorial youtube===pgadmin4

#django

# cmd====    pip install django                                            #We also give specific version like django=4

#virtual enviroment=====================if  we wan to use two saperate version for two diff projects so one do not disturb other otherwise last version od django will be deletetd\

# pip install virtualenv                             ========to create virtual enviorment

# to check existing libraries in cmd

#pip freeze

# ab hume folder banana hai jis folder me banana hai wha jake cmd call karo fir django ka naya version dnld kr sakte hai

#  virtualenv shiva_env    ========my foldername

#to activate follow steps

# cd shiva_env
# dir
# cd scripts
# dir
# activate
# pip freeze                        ----no opt coz folder me koi library ni hai

# ab django ka naya version install kar sakte hai

#pip install django==4.0
#pip freeze
#deactivate.bat         -----------to deactivate virtualenv
#activate

# if not deactivate
# cd..
# cd ..

# to make directory

#cd ..
#cd ..
#mkdir django_projects                                                #mkdir folder_name
#django-admin startproject first_project                              #django-admin startproject project_name

#c drive me save hai yaad rakhna

#first_project
        #__init__.py
        #asgi.py
        #setting.py
        #urls.py
        #wsgi.py
#manage.py

# to run file on vs
# open vs --> drag onto the screen of vs code-->ctrl+shift+p 
# teminal open --> type selct interpretter --> first_project-->-->shiva_env--> python.exe--> click

# to check on terminal
#ctrl+j 
#run manage.py --> type check
#output:=
# (shiva_env) C:\first_project>c:/python/shiva_env/Scripts/python.exe c:/first_project/manage.py check
# System check identified no issues (0 silenced).

# to runserver

#up arrow
#type py manage.py runserver

#opt
#(shiva_env) C:\first_project>c:/python/shiva_env/Scripts/python.exe c:/first_project/manage.py runserver
# Watching for file changes with StatReloader
# Performing system checks...

# System check identified no issues (0 silenced).

#now copy url    ---> http://127.0.0.1:8000 --. paste on internet terminal

#to intrupt the terminal --> ctrl + c


# to deal with django project we have to deal with manager.py

