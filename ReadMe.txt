System Implementation(UML-to-Django):
Prerequisites: 
1. Python, Django, libxml, and ArgoUML installed on the PC.
2. A Django project called PRJ with an empty application called APP.
3. The settings.py must be correctly configured with a reference to a database and the admin and APP application are enabled. 'python manage.py syncdb' and 'python manage.py runserver'. have been executed successfully.
4. Extract the contents of the DjangoUML.zip file into your project's root folder.

Operating Procedure(UML-to-Django):
1. Open PRJ/uml2dj.zargo, rename it APP.zargo and draw a single class diagram (and nothing else in it).
3. In ArgoUML, export your diagram as a XMI file: PRJ/APP.xmi
3. Go to the command line, in the PRJ folder and type: 'python uml2dj APP'. This command will generate the models.py and admin.py files in your APP folder.
4. In the PRJ/APP folder, rename _admin_custom.py into admin_custom.py and _models.py into models.py. (you only need to do this once).
5. Commit the changes to the database: 'python manage.py syncdb'.
6. Now run the server: 'python manage.py runserver'.

System Implementation(Django-to-UML):
Prerequisites: 
1. A Django project with a developed application.
2. Python, Django, libxml, and ArgoUML installed on the PC.
3. The settings.py must be correctly configured with a reference to a database and the admin and APP application are enabled. 'python manage.py syncdb' and 'python manage.py runserver'. have be executed successfully.

Operating Procedure(Django-to-UML):
1. Open up a command prompt, and navigate to you Django project's root folder.
2. Run the command "python djangodjenerator.py APP > output.xmi"
3. Open up ArgoUML, and import the output.xmi file.

**** Additional Notes *****
1. You may change the PRJ Project name and App name to your own names, but you must specify the changes in the SysPath headers of both application files.