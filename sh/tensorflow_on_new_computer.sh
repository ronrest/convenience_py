#!/usr/bin/env bash
################################################################################
# Creates a tensorflow virtualenv, with other packages that are useful to have
# for the pipeline, on a new system.
#
# NOTE: installs developer and system packages.
#
# VERSION: This pipeline works as of tensorflow version 1.3
################################################################################
# terminate script if any line returns a non-zero exit status
set -e

#-------------------------------------------------------------------------------
#                                                                      VARIABLES
#-------------------------------------------------------------------------------
TF="tensorflow-gpu"                    # Use "tensorflow" for cpu version
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
echo "                            INSTALL THE DEVELOPER LIBRARIES"
echo "==========================================================="
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y build-essential git  swig
sudo apt-get install -y python-pip python-dev python-wheel python-virtualenv
sudo apt-get install -y unzip

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
pip install --upgrade pip
sudo apt-get update

echo "INSTALLING NUMPY AND SCIPY"
sudo apt-get install -y libopenblas-dev  # Speeds up numpy/scipy
sudo apt-get install -y liblapack-dev gfortran # Needed for scipy/numpy
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
sudo apt-get install matplotlib
#pip install -U matplotlib
pip install seaborn

echo 'INSTALLING ADITIONAL USEFUL PYTHON LIBRARIES'
pip install h5py

echo 'INSTALL JUPYTER'
# Jupyter is upgraded and forced to reinstall on the virtualenv to
# ensure that the command `jupyter kernelspec list` will recognize
# the virtualenv as containing a viable python kernel to run
pip install -U --force-reinstall jupyter


echo "==========================================================="
echo "                                         INSTALL TENSORFLOW"
echo "==========================================================="
pip install --upgrade ${TF}


echo "==========================================================="
echo "                                               FINISHING UP"
echo "==========================================================="
echo "EXITING VIRTUALENV"
deactivate

# Go back to the directory we started off at.
cd ${START_DIR}
