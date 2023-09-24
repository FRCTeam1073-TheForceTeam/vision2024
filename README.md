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


# Setting up SSH and Github For Your Account:
Go to GitHub.com:

- Find Settings
- Click on SSH and GPG Keys [SSH and GPG Keys](https://docs.github.com/authentication/connecting-to-github-with-ssh)
    - Click "generate ssh key" (the link above) then [Generating Keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    - Click link above (Generating a new SSH Key and adding it to the ssh-agent)
    - Locally in a Shell on the machine run: ``ssh-keygen -t ed25519 -C "your_email@example.com"``
      - Fill in your email (whatever email you use for github)
      - Find the key you just made 
      	- ``cd .ssh``
	- cat your *public* key: ``cat id_ed25519.pub``
	- Copy the key and put it in the spot on the Github textbox for the SSH Key (the big one)
      - CONGRATULATIONS YOU HAVE MADE YOUR KEY!!!
- Go to this awesome and cool link: [Using ssh over http](https://docs.github.com/en/authentication/troubleshooting-ssh/using-ssh-over-the-https-port)
  -  Assuming you are still in your ~/.ssh directory:
     - Run: ``nano config``
     - Cut and paste this config to use SSH over HTTPS for github:
     
       Host github.com
           Hostname ssh.github.com
    	   Port 443
    	   User git

      - Type: Ctrl-O and then CTRL-X to save your ``~/.ssh/config`` file
- Now we're going to test your connection, so run the following in the shell:
  - ``ssh -T git@github.com``
  - then it should say "Hi [username]"
- Now you can check out a code repo that you can securely sync with github over our restricted wifi network:
  - Go back to Github, click on profile picture, go to organizations, click on 1073.
  - Then, click on the repository that you are working on
  - Click on the big green CODE button
  - Click SSH and copy the link (it should be like this)
    ``git@github.com:FRCTeam1073-TheForceTeam/vision2024.git``
  - Run in your terminal(paste in the url part you copied above):
     - git clone git@github.com:FRCTeam1073-TheForceTeam/vision2024.git

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

## Basic Dev Package Installation:

>   sudo apt-get update
>   sudo apt-get install emacs screen build-essential git-core nano wget cmake


These are the packages for C/C++ compilers, build tools and basic text editing.

## System Management:

>   sudo apt-get install cockpit

This provides us with a web-based management console for when the
systems are on the robot and without a screen/keyboard available. For
those who need to know more the documentation for cockpit is here:
https://cockpit-project.org/


## Camera Debug Tools:

>   sudo apt-get install yavta guvcview

These are two tools, one a command line V4L2 camera
debugging/management tool and the other is a graphical camera viewer
just to make sure cameras are going to work with our setup.

## Python3 Development Envirobnment:

>   sudo apt-get install python3 python-is-python3 python3-pip python3-full pipx

This gives us latest Ubuntu version of Python3, makes it the default
and adds the pip tool for installing python specific pacakges.

## Video Codec and GStreamer:

>   sudo apt-get install libavformat-dev libavcodec-dev libswscale-dev ffmpeg
   vainfo
>   sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio gstreamer1.0-vaapi


This installs commonly available codec libraries, tools for the VAAPI
hardware accelerator on Intel platforms and most of gstreamer,
including accelerated video codecs.

## Python3 Environment Extras:

>   sudo apt-get install python3-ipython ipython3 python3-opencv idle

This pulls in a lot of common Python3 tools and libraries like numpy
and matplotlib, etc. as well as OpenCV for Python3.

Now we can pull in the april tag wrapper driver:

>    pip3 install apriltag

## Network Tables:

Last, but not least, we need to pull in networktables in python so we
can easily talk to subsystems on the robot to get data, etc.

>    pip3 install pynetworktables
