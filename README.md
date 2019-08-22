"# djangorecruitment" 
"# djangorecrutment" 
"# djangoproject" 


#execute the commend in current project directory 
python manage.py runserver


############## ADD email and password in  recrutmentsystem >> settings.py
######################  Allow access for your gmail by click this below url    
   https://myaccount.google.com/lesssecureapps
 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your gamil address'
EMAIL_HOST_PASSWORD = 'gmail password'



########## User submit application URL

localhost:8000


############ Admin site  url  

localhost:8000/showdetails


!!!! This appllication email sending features also available !!!!


kindly add your email And passsword while testing this application





 




