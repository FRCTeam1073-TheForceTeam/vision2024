# Setup up service auto-start:

Once your code is developed and tested, you'll want to set up the
vision services to start automatically on the Mini-PC as part of your
robot startup.

The autostart directory contains several files that are
systemd service unit files. These need to be copied
to:

    sudo cp <service file> /etc/systemd/system

Now reload configurations:

    sudo systemctl daemon-reload

Now you enable the services you want enabled to auto-start:

    sudo systemctl enable <service name>


You can then check on services using:

    systemctl status <service name>


Note that the autostart files assume you are using user team1073 and
that you have checked out the vision repository on the system at:
/home/team1073/Projects/vision20
