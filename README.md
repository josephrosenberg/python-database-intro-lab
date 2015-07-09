# Database Intro Student Example

This code creates a database model for a `Student` and allows you to create students with an HTML form and display the resulting list of students.

## Launch

To run this code and make sure the site reflects changes in the database immediately make sure to run `dev_appserver.py` with these keys

```
dev_appserver.py --datastore_consistency_policy=consistent [path_to_app_name]
```

If you are in the directory with all of your App Engine code then `[path_to_app_name]` can be replaced with a `.` (period).

To clear the datastore:

```
dev_appserver.py --clear_datastore=1 [path_to_app_name]
```

To view the app:
```
localhost:8080
```

To view the database backend:
```
localhost:8000
```

## Goals

+ You are encouraged to run the code and tinker with the different elements
  + Try to add a field to the model and the HTML form
  + Try adding print statements in main.py to see what function is being called when
  + Add CSS to make the UI better looking
+ Use this as a template for future work
