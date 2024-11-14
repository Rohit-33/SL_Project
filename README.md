sl_wellness
	-wellness
	-instance


flask app should be set to package containing __init__.py
So,now go to c:\sl_wellness(your folder in which the wellness folder is present)
	set FLASK_APP=wellness
	set FLASK_DEBUG=1

For adding new tables to database, re instiate the database tables. Generally not preferrable, but it is fine for now
So, from same directory, type 
* python
Now, in the python commands, import db and create_app from wellness package
* from wellness import create_app, db
* app = create_app()
* with app.app_context():
	  db.create_all()
* quit()
* now all the tables in models.py will be recreated
