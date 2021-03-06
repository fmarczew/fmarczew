from fabric.api import local, lcd, settings

def prepare_deployment(branch_name):
    with settings(warn_only=True):
	local('python manage.py test Chat')
	local('git add -p && git commit')
	local('git checkout master && git merge ' + branch_name)


def deploy():
    with lcd('/home/matsche/Dev/python_django/My_Page/'):
        local('git pull /home/matsche/Dev/python_django_local/fmarczew/')
        local('python manage.py migrate Chat')
        local('python manage.py test Chat')
        local('echo "Done deployment"')
