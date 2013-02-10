#!/bin/bash
# For a strange reason, numpy need to be installed before starting the container
echo "====>"
echo "====> Manually installing numpy and/or scipy"
echo "====>"
#/opt/python/run/venv/bin/pip install -q --log /tmp/numpy.log --use-mirrors numpy
/opt/python/run/venv/bin/pip install -q --log /tmp/scipy.log --use-mirrors scipy
#/opt/python/run/venv/bin/pip install -q --log /tmp/sklearn.log --use-mirrors scikit-learn
/opt/python/run/venv/bin/pip freeze
