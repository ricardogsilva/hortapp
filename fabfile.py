#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
A fabric fabfile to automate deployment tasks.
'''
import os
from ConfigParser import SafeConfigParser
from fabric.api import settings, sudo, local

def _install_apt_dependencies():
    sudo('apt-get install python-dev libsqlite3-dev python-virtualenv')

def _create_virtualenv(virtualenv_dir):
    with settings(warn_only=True):
        if local('test -d %s' % virtualenv_dir).failed:
            local('virtualenv %s' % virtualenv_dir)

def _install_pysqlite(python_interpreter):
    '''
    Download, configure and install pysqlite.

    In order to use spatialite, the pysqlite module must have been compiled 
    allowing the loading of extensions, which is not the default. As such,
    it is necessary to get the pysqlit source code and compile with the 
    required configuration.
    '''
    _install_apt_dependencies()
    source_code = {
        'download_dir' : 'tmp',
        'base_url' : 'http://pysqlite.googlecode.com/files',
        'package_name' : 'pysqlite-2.6.3.tar.gz'
    }
    local('mkdir -p %(download_dir)s' % source_code)
    with cd('(download_dir)s' % source_code):
        local('wget %(base_url)s/(package_name)s' % source_code)
        local('tar -zxvf %(package_name)s' % source_code)
        config_file = '(package_name)s/setup.cfg' % source_code 
        config = SafeConfigParser()
        config.read(config_file)
        config.remove_option('build_ext', 'define')
        with open(config_file, 'w') as fh:
            config.write(fh)
        local('%s setup.py install' % python_interpreter)

def prepare_development():
    root_dir = os.path.dirname(os.path.realpath(__file__))
    env_dir = os.path.join(root_dir, 'env')
    _create_virtualenv(env_dir)
    interpreter = os.path.join(env_dir, 'bin', 'python')
    _install_pysqlite(interpreter)

def clone_repo():
    run('git clone https://github.com/ricardogsilva/hortapp.git')
