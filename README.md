# ContentManagementSystem
This is a django rest-framework project for creating a post with all the crud functionalities  , user authentification field level validation
Setup :
1.To setup the project we first need to clone : use command git clone https://github.com/Maniabhishek/ContentManagementSystem.git
2.Run all the migrations , using python manage.py makemigrations and then python manage.py migrate
3.then create admin user using django seeding python manage.py loaddata appuser/fixtures/admindata.json (if in case you get the error saying UTF-8 then just save the                                   admindata.json file again in utf-8 format with the samedata )
      admin user will be created : with email= admin@gmail.com , password = Password , username=admin
      2 user will be created : with email =json@gmail.com password = Jsonroy12 , username = jsonroy and email =test@gmail.com password = Testuser12 , username = testuser

4.Creating user using API link : http://127.0.0.1:8000/api/user/register/
  User will have enter the username , email in correct format , first name , lastname , email address , password , confirm password , phone with correct format, pincode in correct format 
  password will only be accepted if it contain atleast one uppercase and one lower case and 8 digit long
5 To Create a Post :
  A user can create a post only when user is authorized and logged in using the link
    http://127.0.0.1:8000/api/home/content/create
    user will get the prompt to fill all the details like title , body , summary, category, pdf
    once the user fill the details and submit the post will be created 
    
6. TO see all the details of all the post user can visit the link :
    http://127.0.0.1:8000/api/home/  (all the post can be seen here )
 
7. to delete or update a post : 
    to delete a post a user has to be authenticated and user must own the post 
 Admin user can delete or update anyone's post 
 
8 to logout from the site use the link http://127.0.0.1:8000/logout/
9 to login to application : http://127.0.0.1:8000/appuser/login/
 
10. To run the unit test:
 use the command : python manage.py test appcms
  this will run all the test 
  
 Thank you!
 
 
 
