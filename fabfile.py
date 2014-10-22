from fabric.contrib.files import upload_template

__author__ = 'GoldenGate'
from fabric.colors import green, yellow
from fabric.decorators import task
from fabric.operations import local
from fabric.api import *

env.hosts = ['54.187.121.120']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/dating.pem'
env.shell = "/bin/bash -l -i -c"

# fab hello
@task
def hello():
    print(green("I'm alive!"))

@task
def create_blank_file():
    local("touch /Users/GoldenGate/Desktop/dummy_file.txt")

# fab create_file:hey_peter
@task
def create_file(file_name):
    local("touch /Users/GoldenGate/Desktop/{}.txt".format(file_name))

@task
def desktop_dir(dir_name):
    local("mkdir /Users/GoldenGate/Desktop/{}".format(dir_name))

@task
def dir_anywhere(path, dir_name):
    local("mkdir {}/{}".format(path, dir_name))

@task
def ubuntu_hello1():
    run("lsb_release -a")

@task
def ubuntu_hello():
    with hide("stdout"):
        output = run("lsb_release -a")
        print(yellow(output))

@task
def deploy():
    with prefix("workon dating"):
        with cd("/home/ubuntu/dating"):
            run("git pull origin master")
            run("pip install -r requirements.txt")
            # run("python manage.py makemigrations")
            run("python manage.py migrate")
            run("python manage.py collectstatic --noinput")
            setup_nginx()
    restart_app()


def restart_app():
    sudo("service supervisor restart")
    run("sudo service nginx restart")

@task
def setup_postgres(database_name, password):
    sudo("adduser {}".format(database_name))
    sudo("apt-get install postgresql postgresql-contrib libpq-dev")

    with settings(sudo_user='postgres'):
        sudo("createuser {}".format(database_name))
        sudo("createdb {}".format(database_name))
        alter_user_statement = "ALTER USER {} WITH PASSWORD '{}';".format(database_name, password)
        sudo('psql -c "{}"'.format(alter_user_statement))

@task
def setup_nginx(project_name, server_name):
    upload_template("./deploy/nginx.conf",
                    "/etc/nginx/sites-enabled/{}.conf".format(project_name),
                    {'server_name': server_name},
                    use_sudo=True,
                    backup=False)

    restart_app()
