#!/usr/bin/env python

from flask import *
import numpy
import numpy.distutils.system_info as sysinfo

# The WSGI configuration on Elastic Beanstalk requires 
# the callable be named 'application' by default.
application = Flask(__name__)

# Setup the root route of the website, and render the 'index.html' template
@application.route("/")
def default():
    #display welcome page
    return render_template('index.html')

@application.route("/page2")
def page2():
    blas_info = sysinfo.get_info('blas')
    lapack_info = sysinfo.get_info('lapack')
    return render_template('page2.html', data={'blas': str(blas_info), 'lapack': str(lapack_info)})

if __name__ == '__main__':
    application.debug = True
    application.run(host='0.0.0.0')
