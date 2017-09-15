#!/bin/bash
# Author: Ronny Restrepo
# The contents of this script are explained in this blog post
#   - http://ronny.rest/blog/post_2017_09_15_opencv/
#
# Source package urls for available versions are on this page:
#   - http://opencv.org/releases.html
#
# This script is based on this Fedora tutorial:
#   - http://docs.opencv.org/3.3.0/dd/dd5/tutorial_py_setup_in_fedora.html
# With the following modifications:
# - Modified to work on ubuntu
# - Updated for specifics of opencv 3.3
# - Modified to use packaged version zip files instead of entire git repository.
# - Modified to make use of multiple cored for compilation of source code.
# - Different compilation settings (eg, not disabling GPU support)
# - Entire process designed to be automated, after setting some initial
#   variables.

################################################################################
#                                    VARIABLES
################################################################################
CV_SOURCE_PACKAGE="3.3.0.zip"
CV_SOURCE_URL="https://github.com/opencv/opencv/archive/${CV_SOURCE_PACKAGE}"
TEMP_DIR="/tmp/cv"  # where to store the source files temporarily
NCORES=4            # Number of CPU cores to use during compiling of source code

################################################################################
#                                    FAILSAFE
################################################################################
# terminate script if any line returns a non-zero exit status
set -e

################################################################################
#                                   DEPENDENCIES
################################################################################
echo "\n========================================================="
echo "INSTALLING DEV DEPENDENCIES"
echo "=========================================================\n"
sudo apt-get update
#sudo apt-get upgrade -y

sudo apt-get install -y build-essential cmake gcc swig pkg-config #gcc-c++
sudo apt-get install -y python-pip python-dev python-wheel python-virtualenv
sudo apt-get install -y unzip

echo "\n========================================================="
echo "INSTALLING GUI AND CAMERA DEPENDENCIES"
echo "=========================================================\n"
sudo apt-get install -y libgtk2.0-dev
sudo apt-get install -y libdc1394-dev
sudo apt-get install -y libavcodec-dev libavformat-dev
sudo apt-get install -y libswscale-dev libavresample-dev
sudo apt-get install -y libv4l-dev ffmpeg-dev
sudo apt-get install -y gstreamer-plugins-base1.0-dev

echo "\n========================================================="
echo "INSTALLING IMAGE DEPENDENCIES"
echo "=========================================================\n"
sudo apt-get install -y libtiff4-dev libjasper-dev libpng12-dev
sudo apt-get install -y libjpeg8-dev libjpeg-turbo8-dev
sudo apt-get install -y libopenexr-dev
sudo apt-get install -y libwebp-dev

sudo apt-get install -y libprotobuf-dev
sudo apt-get install -y libgphoto2-6 libgphoto2-dev

echo "\n========================================================="
echo "INSTALLING PYTHON DEPENDENCIES"
echo "=========================================================\n"
sudo apt-get install -y libopenblas-dev  # Speeds up numpy/scipy
sudo apt-get install -y liblapack-dev gfortran # Needed for scipy/numpy
sudo apt-get install -y python-numpy python3-numpy
sudo apt-get install -y python-scipy python3-scipy

echo "\n========================================================="
echo "INSTALLING OPTIMIZATION DEPENDENCIES"
echo "=========================================================\n"
# Intel's Threading Building Blocks (TBB) - For parallelization
# Cmake configuration: -D WITH_TBB=ON
sudo apt-get install -y libtbb-dev

# Eigen for optimized mathematical operations.
#  Cmake configuration: -D WITH_EIGEN=ON
sudo apt-get install -y libeigen3-dev


################################################################################
#                                      BODY
################################################################################
# Make a temporary directory to store the source files in
echo "CREATING TEMPORARY DIRECTORY FOR SOURCE FILES"
mkdir ${TEMP_DIR}
cd ${TEMP_DIR}

echo "\n========================================================="
echo "DOWNLOADING THE SOURCE FILES"
echo "=========================================================\n"
wget -c ${CV_SOURCE_URL}

echo "\n========================================================="
echo "EXTRACTING THE SOURCE FILES"
echo "=========================================================\n"
unzip ${CV_SOURCE_PACKAGE} -d opencv_source_files
cd opencv_source_files/opencv*

echo "\n========================================================="
echo "BUILDING FROM SOURCE CODE"
echo "=========================================================\n"
# Create a directory to store the build
mkdir build
cd build

# A hacky variable used to sandwich comments in between a long line
COMMENT=

# Make the build
cmake \
    -D CMAKE_BUILD_TYPE=RELEASE           {COMMENT-"Release Mode "}\
	-D CMAKE_INSTALL_PREFIX=/usr/local    {COMMENT-"Installation path"}\
	-D INSTALL_C_EXAMPLES=OFF             {COMMENT-"No C examples"}\
	-D INSTALL_PYTHON_EXAMPLES=ON         {COMMENT-"Include Python Examples"}\
    -D BUILD_TESTS=OFF                    {COMMENT-"disable tests"}\
    -D BUILD_PERF_TESTS=OFF               {COMMENT-"disable tests"}\
    -D BUILD_EXAMPLES=OFF                 {COMMENT-"disable samples"}\
    -D WITH_TBB=ON    {COMMENT-"Enable Intel's (TBB) - For parallelization"}\
    -D WITH_EIGEN=ON {COMMENT-"Enable Eigen - for optimized math operations."}\
    ..

#=================================================================
# ADITIONAL FLAGS that could be used
#=================================================================
# Extra modules
# cmake \
    # -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules
    # ..

# Disable all GPU related modules.
# cmake \
    # -D WITH_OPENCL=OFF \
    # -D WITH_CUDA=OFF \
    # -D BUILD_opencv_gpu=OFF \
    # -D BUILD_opencv_gpuarithm=OFF \
    # -D BUILD_opencv_gpubgsegm=OFF \
    # -D BUILD_opencv_gpucodec=OFF \
    # -D BUILD_opencv_gpufeatures2d=OFF \
    # -D BUILD_opencv_gpufilters=OFF \
    # -D BUILD_opencv_gpuimgproc=OFF \
    # -D BUILD_opencv_gpulegacy=OFF \
    # -D BUILD_opencv_gpuoptflow=OFF \
    # -D BUILD_opencv_gpustereo=OFF \
    # -D BUILD_opencv_gpuwarping=OFF \
    # ..


#=================================================================
# CHECK BUILD PRINTOUT FOR THE FOLLOWING LINES - SHOULD BE SIMILAR
#=================================================================
# --   GUI:
# --     GTK+ 2.x:                    YES (ver 2.24.23)
# --     GThread :                    YES (ver 2.40.2)
#
# --   Media I/O:
# --     ZLib:                        /usr/lib/x86_64-linux-gnu/libz.so (ver 1.2.8)
# --     JPEG:                        /usr/lib/x86_64-linux-gnu/libjpeg.so (ver )
# --     WEBP:                        /usr/lib/x86_64-linux-gnu/libwebp.so (ver encoder: 0x0202)
# --     PNG:                         /usr/lib/x86_64-linux-gnu/libpng.so (ver 1.2.50)
# --     TIFF:                        /usr/lib/x86_64-linux-gnu/libtiff.so (ver 42 - 4.0.3)
# --     JPEG 2000:                   /usr/lib/x86_64-linux-gnu/libjasper.so (ver 1.900.1)
#
# --   Video I/O:
# --     DC1394 2.x:                  YES (ver 2.2.1)
# --     FFMPEG:                      YES
# --       avcodec:                   YES (ver 54.35.1)
# --       avformat:                  YES (ver 54.20.4)
# --       avutil:                    YES (ver 52.3.0)
# --       swscale:                   YES (ver 2.1.1)
# --       avresample:                YES (ver 1.0.1)
# --     GStreamer:
# --       base:                      YES (ver 1.2.4)
# --       video:                     YES (ver 1.2.4)
# --       app:                       YES (ver 1.2.4)
# --       riff:                      YES (ver 1.2.4)
# --       pbutils:                   YES (ver 1.2.4)
# --     V4L/V4L2:                    NO/YES
# --     gPhoto2:                     YES
#
# --   Parallel framework:            TBB (ver 4.2 interface 7000)
#
# --   Other third-party libraries:
# --     Use Intel IPP:               2017.0.2 [2017.0.2]
# --                at:               /tmp/cv/opencv_source_files/opencv-3.3.0/build/3rdparty/ippicv/ippicv_lnx
# --     Use Lapack:                  NO
# --     Use Eigen:                   YES (ver 3.2.0)
# --     Use Cuda:                    NO
# --     Use OpenCL:                  YES
#
# --   Python 2:
# --     Interpreter:                 /usr/bin/python2.7 (ver 2.7.6)
# --     Libraries:                   /usr/lib/x86_64-linux-gnu/libpython2.7.so (ver 2.7.6)
# --     numpy:                       /usr/local/lib/python2.7/dist-packages/numpy/core/include (ver 1.11.0)
# --     packages path:               lib/python2.7/dist-packages
# --
# --   Python 3:
# --     Interpreter:                 /usr/bin/python3.4 (ver 3.4.3)
# --     Libraries:                   /usr/lib/x86_64-linux-gnu/libpython3.4m.so (ver 3.4.3)
# --     numpy:                       /usr/local/lib/python3.4/dist-packages/numpy/core/include (ver 1.11.0)
# --     packages path:               lib/python3.4/dist-packages
# --
# --   Python (for build):            /usr/bin/python2.7
# --

echo "\n========================================================="
echo "COMPILING FROM SOURCE CODE"
echo "=========================================================\n"
make -j${NCORES}  # compile using NCORES number of CPU cores

echo "\n========================================================="
echo "INSTALLING THE COMPILED BINARIES"
echo "=========================================================\n"
sudo make install
sudo ldconfig

################################################################################
#                       LINKING THE LIBRARY TO PYTHON
################################################################################
# All files are installed in the following directory:
#   /usr/local/

echo "\n========================================================="
echo "LINKING PYTHON to open CV"
echo "=========================================================\n"
# For Opencv 3.3, it places the cv file for python2.7 in:
#   /usr/local/lib/python2.7/dist-packages/cv2.so
# Which should be ready to use

# For older versions of open cv, you may need to manually move the file
# to the correct place, using something like:
# cd /usr/lib/python2.7/dist-packages/
# sudo ln -s -f /usr/local/lib/python2.7/site-packages/cv2.so cv2.so


# For Opencv 3.3, it places the cv file for python3.4 in:
#   /usr/local/lib/python3.4/dist-packages/cv2.cpython-34m.so
# Which should be ready to use

# For older versions of open cv, you may need to manually move the file
# to the correct place, using something like:
# cd /usr/local/lib/python3.4/dist-packages/
# sudo ln -s -f /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.cpython-34m.so
#
# If that doesnt work,then try this one
# cd /usr/lib/python3/dist-packages
# sudo ln -s -f /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.cpython-34m.so


################################################################################
#                                    TESTING
################################################################################
# To test that it is installed correctly, got into the python environment.
#   python
#
# Now import and check the version of the cv imported, it should match the
# version you tried to install. NOTE: even though we installed version 3, it is
# imported in python as cv2 (yes, its confusing):
#
# >>> import cv2
# >>> print(cv2.__version__)
# 3.3.0


################################################################################
#                       REMOVING TEMPORARY INSTALLATION FILES
################################################################################
echo "\n========================================================="
echo "REMOVING TEMPORARY INSTALLATION FILES"
echo "=========================================================\n"
cd ${TEMP_DIR}
rm ${CV_SOURCE_PACKAGE}
rm -rf opencv_source_files
