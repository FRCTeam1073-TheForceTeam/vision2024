# vision2024
Vision code and setup for 2023/2024 season.

# Hardware Setup:

This season we're going to try out some newly available Mini-PC systems
as our hardware platform and set them up on Ubuntu 23.04 Linux as
our software platform.

Our first hardware machine is:

https://www.amazon.com/GMKtec-Nucbox5-Desktop-Computer-Windows/dp/B0B75PT2RY/ref=sr_1_3?keywords=GMKtec%2Bmini-pc&qid=1691854541&sr=8-3&th=1

This provides us with a quad-core processor, 3 USB3 ports and hardline
ethernet to connect to the robot network as well as the media
acceleration features of the Intel platform.


# Software Setup:

The machines come with Windows 11 but we boot into the BIOS and
install Ubuntu 23.04 as our base operating system and then' we need to
install a bunch of software packages for writing and running robot
perception cdoe. We picked Ubuntu 23.04 because the gstreamer / vaapi
configurations for Ubuntu 22.04 were botched in some way and nearly
all hardware encoding is disabled in standard packages on that version
of the platform.

Some of the key things we want to be able to do this year with our
software include:

  - Stream back H.264 compressed video to driver station.
  - Handle multiple AprilTag trackers for alignment and navigation landmarks.
  - Game-piece detection and tracking.


## Miniconda Install:
We need to use a python enviorment to run our camera programs, and the latest version of ubuntu will not support what we are trying to do. 
To get the code to work install miniconda (https://docs.conda.io/en/main/miniconda.html).

  mkdir -p ~/miniconda3
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/miniconda3/miniconda.sh
  bash ./Miniconda3-latest-Linux-x86_64.sh -b -u -p ~/miniconda3
  ~/miniconda3/bin/conda init bash 
  conda create -n vision python=3.11
  conda activate vision

## NOW YOU INSTALL EVERYTHING ELSE INTO THIS VIRTUAL ENVIORMENT

## Basic Dev Package Installation:

   sudo apt-get update
   sudo apt-get install emacs screen build-essential git-core nano wget cmake


These are the packages for C/C++ compilers, build tools and basic text editing.

## System Management:

   sudo apt-get install cockpit

This provides us with a web-based management console for when the
systems are on the robot and without a screen/keyboard available. For
those who need to know more the documentation for cockpit is here:
https://cockpit-project.org/


## Camera Debug Tools:

   sudo apt-get install yavta guvcview

These are two tools, one a command line V4L2 camera
debugging/management tool and the other is a graphical camera viewer
just to make sure cameras are going to work with our setup.

## Python3 Development Envirobnment:

   sudo apt-get install python3 python-is-python3 python3-pip python3-full pipx

This gives us latest Ubuntu version of Python3, makes it the default
and adds the pip tool for installing python specific pacakges.

## Video Codec and GStreamer:

   sudo apt-get install libavformat-dev libavcodec-dev libswscale-dev ffmpeg
   vainfo

   sudo apt-get install libgstreamer1.0-dev
   libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev
   gstreamer1.0-plugins-base gstreamer1.0-plugins-good
   gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
   gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x
   gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3
   gstreamer1.0-qt5 gstreamer1.0-pulseaudio gstreamer1.0-vaapi


This installs commonly available codec libraries, tools for the VAAPI
hardware accelerator on Intel platforms and most of gstreamer,
including accelerated video codecs.

## Python3 Environment Extras:

   sudo apt-get install python3-ipython ipython3 python3-opencv

This pulls in a lot of common Python3 tools and libraries like numpy
and matplotlib, etc. as well as OpenCV for Python3.

Now we can pull in the april tag wrapper driver:

    pip3 install apriltag

## Network Tables:

Last, but not least, we need to pull in networktables in python so we
can easily talk to subsystems on the robot to get data, etc.

    pip3 install pynetworktables



