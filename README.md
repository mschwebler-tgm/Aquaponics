Automated Home Aquaponics
=======================

Setup for Django
----------------
    * Clone repository
    * cd django/myproject
    * vagrant up
    * vagrant ssh
    * ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8000/ . The codebase is located on the host
machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host.

