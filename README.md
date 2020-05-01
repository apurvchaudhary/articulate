# Articulate Rating & Review
<h4>Giving personal Rating & Review on movies/series/documentaries/shortfilms most of them  are under famous.</h3>
<ul>
    <li>
    Reader will get small detailed review about various movie, series etc.</li>
    <li>
    Trailer watch option is also accessible via button click as per user choice
    </li>
    <li>
    This is open source project and you are welcome to contribute.
    </li>
    <li>
    project url : http://ec2-3-135-201-128.us-east-2.compute.amazonaws.com/ani/home/
    </li>
    <li>
    currently running on AWS ec2 with apache2 server
    </li>
    <li>
    Tech Stack : python, django, djangorestframework, html, css, JS, Jquery
    </li>
</ul>

Installation Setup : steps
<ol>
<li>
git pull https:// this repository as it is public. 
</li>
<li>
create python3 virtual environment. (python >= 3.6.5) :
~ python3 -m venv env_name
</li>
<li>
activate env : ~ source env_name/bin/activate
</li>
<li>
install requirements : ~ pip install -r path_to_requirement.txt
</li>
<li>
migrations : ~ python manage.py migrate
</li>
<li>
create superuser : ~ python manage.py createsuperuser
</li>
<li>
collect static files : ~ python manage.py collectstatic articulate_static
</li>
<li>
all these setup has dependency on settings.py, contact for settings.
</li>
<li>
Image upload default set to AWS s3 bucket i.e defined in settings.py
</li>
<li>
finally run server : ~ python manage.py runserver
</li>
</ol>