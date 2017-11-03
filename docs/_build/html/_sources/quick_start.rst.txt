Quick Start Guide
=================
 
 
Download AnisongDB Project
----------------------------------------------
 
Download a branch from GitHub. 
 
 
 
Virtual environments and Settings Files
---------------------------------------
 
First, find your Python 3 path::
 
    $ which python3
 
Next, create a Development virtual environment with Python 3 installed::
 
    $ mkvirtualenv --python=/usr/local/bin/python3 django_anisongdb
 
If using virtualenviornmentwrapper either set PATH or use these lines::

    $ export WORKON_HOME= ~/venv/
    $ source /home/usrname/.local/bin/virtualenvwrapper.sh

Edit the postactivate file in the /bin/ inside virtualenv::
 
    $ vi postactivate
 
Add the lines: ::
 
    export DJANGO_SETTINGS_MODULE="anisongdb.settings.development"
    export SECRET_KEY="secret_django_key"
    
    export DATABASE_NAME="anisongdb"
    export DATABASE_USER="mirose"
    export DATABASE_PASSWORD="database_password"
 
Next, edit the **predeactivate** to unset::
 
    unset SECRET_KEY
    unset DATABASE_NAME
    unset DATABASE_USER
    unset DATABASE_PASSWORD
 
Repeat the last steps for your testing environment::
 
    $ mkvirtualenv --python=/usr/local/bin/python3 anisong_test
    $ cd $VIRTUAL_ENV/bin
    $ vi postactivate
 
postactivate::
 
    export DJANGO_SETTINGS_MODULE="anisong.settings.testing"
    export SECRET_KEY="secret_django_key"
    
    export DATABASE_NAME="anisongdb"
    export DATABASE_USER="mirose"
    export DATABASE_PASSWORD="database_password"
 
predeactivate::
 
    unset SECRET_KEY
    unset DATABASE_NAME
    unset DATABASE_USER
    unset DATABASE_PASSWORD
 
Next, install the packages in each environment::
 
    $ workon django_anisongdb
    $ pip install -r requirements/development.txt
    $ workon anisong_test
    $ pip install -r requirements/testing.txt
 
 
 
Internationalization and Localization
-------------------------------------
 
Settings
********
 
The default language for this Project is **English**, and we use internatinalization to translate the text into Japanese hopefully...
 
If you want to change the translation language, or include a new one, you just need to modify the **LANGUAGES** variable in the file *settings/base.py*. The language codes that define each language can be found |codes_link|.
 
.. |codes_link| raw:: html
 
    <a href="http://msdn.microsoft.com/en-us/library/ms533052(v=vs.85).aspx" target="_blank">here</a>
 
For example, if you want to use German you should include::
 
    LANGUAGES = (
        ...
        'de', _("German"),
        ...
    )
 
You can also specify a dialect, like Luxembourg's German with::
 
    LANGUAGES = (
        ...
        'de-lu', _("Luxemburg's German"),
        ...
    )
 
Note: the name inside the translation function _("") is the language name in the default language (English).
 
More information on the |internationalization_post|. 
 
.. |internationalization_post| raw:: html
 
    <a href="http://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones" target="_blank">TaskBuster post</a>
 
 
Translation
***********
 
Go to the terminal, inside the anisong_project folder and create the files to translate with::
 
    $ python manage.py makemessages -l ja
 
change the language "ja" for your selected language.
 
Next, go to the locale folder of your language::
 
    $ cd auto/locale/ja/LC_MESSAGES
 
where anisongdb is your project folder. You have to edit the file *django.po* and translate the strings. You can find more information about how to translate the strings |translation_strings_post|.
 
.. |translation_strings_post| raw:: html
 
    <a href="http://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones#inter-translation" target="_blank">here</a>
 
Once the translation is done, compile your messages with::
 
    $ python manage.py compilemessages -l ja
 
 
 
Tests
*****
 
We need to update the languages in our Tests to make sure the translation works correclty. Open the file *functional_tests/test_all_users.py*:
 
- in **test_internationalization**, update your languages with the translation of title text, here "Welcome to AnisongDB!"
- in **test_localization**, update your languages.
 
 
 
Useful commands
---------------
 
A list of all the commands used to run this template::
 
    $ workon django_anisong
    $ workon anisong_test
 
    $ python manage.py makemessages -l ca
    $ python manage.py compilemessages -l ca

