#!/usr/bin/env bash
################################################################################
# On an already established computer where you already might have other
# related machine learning/data science virtualens, this creates a fresh
# new tensorflow virtualenv, with other packages that are useful to have
# for the pipeline.
#
# NOTE: Assumes you have already installed all the developer/system packages.
#       This only installs the things inside the virtualenv environment.
#
# VERSION: This pipeline works as of tensorflow version 1.3
################################################################################
# terminate script if any line returns a non-zero exit status
set -e

#-------------------------------------------------------------------------------
#                                                                      VARIABLES
#-------------------------------------------------------------------------------
TF="tensorflow"                        # Use "tensorflow-gpu" for gpu version
PYTHON_VERSION="3.4"
VIRTUAL_ENV_NAME="myenv"
VIRTUAL_ENV_ROOT="${HOME}/virtualenvs" # Where your virtual envs are stored.
                                       # NOTE: no trailing forward-slash at
                                       # the end

#-------------------------------------------------------------------------------
#                                                                          START
#-------------------------------------------------------------------------------
START_DIR=pwd   # Store Initial Working Directory

echo "==========================================================="
echo "                                           SETUP VIRTUALENV"
echo "==========================================================="
echo "CREATING VIRTUALENV"
mkdir -p ${VIRTUAL_ENV_ROOT}
cd ${VIRTUAL_ENV_ROOT}
virtualenv --system-site-packages -p /usr/bin/python${PYTHON_VERSION} ${VIRTUAL_ENV_NAME}

echo "ENTERING VIRTUALENV"
. ${VIRTUAL_ENV_ROOT}/${VIRTUAL_ENV_NAME}/bin/activate


echo "==========================================================="
echo "                                   INSTALL PYTHON LIBRARIES"
echo "==========================================================="
echo "UPGRADING PIP"
sudo apt-get update
pip install --upgrade pip

echo "INSTALLING NUMPY AND SCIPY"
pip install numpy
pip install scipy
# sudo apt-get install -y python-numpy


echo "INSTALLING PANDAS"
sudo apt-get install -y python-tk  # Needed by Pandas
pip install pytz                   # Needed by pandas
pip install pandas

# Libraries for image processing
echo "INSTALLING PILLOW IMAGE PROCESSING LIBRARY"
sudo apt-get install -y libjpeg-dev libpng12-dev    # Needed by pillow
pip install Pillow

echo "INSTALLING VISUALIZATION LIBRARIES"
pip install pydot
pip install graphviz

echo 'INSTALLING PLOTTING LIBRARIES'
pip install seaborn

echo 'INSTALL JUPYTER'
# Jupyter is upgraded and forced to reinstall on the virtualenv to
# ensure that the command `jupyter kernelspec list` will recognize
# the virtualenv as containing a viable python kernel to run
pip install -U --force-reinstall jupyter

echo 'INSTALLING DATA LOADING LIBRARIES'
pip install h5py


echo "==========================================================="
echo "                                         INSTALL TENSORFLOW"
echo "==========================================================="
# Ensure this version of tensorflow is separate from anything that
# might already be installed on the system
pip install --upgrade --force-reinstall ${TF}


echo "==========================================================="
echo "                                               FINISHING UP"
echo "==========================================================="
echo "EXITING VIRTUALENV"
deactivate

# Go back to the directory we started off at.
cd ${START_DIR}
