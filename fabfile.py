#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
A fabric fabfile to automate deployment tasks.
'''

import os
from ConfigParser import SafeConfigParser
from fabric.api import lcd, settings, sudo, local, env

def _install_apt_dependencies(where):
    '''
    Install the needed apt dependencies on a local machine.
    '''

    where('sudo apt-get install python-dev libsqlite3-dev python-pip fabric ' \
         'python-virtualenv libspatialite3 spatialite-bin')

def _install_pysqlite(root_dir, env_dir):
    '''
    Download, configure and install pysqlite.

    In order to use spatialite, the pysqlite module must have been compiled 
    allowing the loading of extensions, which is not the default. As such,
    it is necessary to get the pysqlite source code and compile with the 
    required configuration.
    '''

    source_code = {
        'download_dir' : os.path.join(root_dir, 'tmp'),
        'base_url' : 'http://pysqlite.googlecode.com/files',
        'package_name' : 'pysqlite-2.6.3',
        'compression' : 'tar.gz',
    }
    local('mkdir -p %(download_dir)s' % source_code)
    with lcd(source_code['download_dir']):
        local('wget %(base_url)s/%(package_name)s.%(compression)s' % \
              source_code)
        local('tar -zxvf %(package_name)s.%(compression)s' % source_code)
        config_file = os.path.join(source_code['download_dir'],
                                   source_code['package_name'],
                                   'setup.cfg')
        config = SafeConfigParser()
        config.read(config_file)
        config.remove_option('build_ext', 'define')
        with open(config_file, 'w') as fh:
            config.write(fh)
    with lcd(os.path.join(source_code['download_dir'], 
                          source_code['package_name'])):
        local('%s setup.py install' % os.path.join(env_dir, 'bin', 'python'))
    local('rm -rf %(download_dir)s' % source_code)

def prepare_env():
    '''
    Prepare a local machine for development.

    This task will create a virtualenv and download any required packages and
    python modules that need compilation in order to work on the project's
    development.
    '''

    _install_apt_dependencies(local)
    root_dir = os.path.dirname(os.path.realpath(__file__))
    env_name = 'env'
    virtualenv_dir = os.path.join(root_dir, env_name)
    if not os.path.isdir(virtualenv_dir):
        local('virtualenv %s' % env_name)
        _install_pysqlite(root_dir, virtualenv_dir)

def install_extra_requirements(where=local):
    where('pip install -r requirements.txt')

def clone_repo():
    pass
    run('git clone https://github.com/ricardogsilva/hortapp.git')
