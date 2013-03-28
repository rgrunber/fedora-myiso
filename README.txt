This is meant to provide a USB Persistence boot for Fedora 18.  The
environment uses a kickstart file to generate the final ISO so a lot
of customization can be done with this environment (eg. pre-installed
RPMs, various configurations/setups). This is what was used to set up
the Live USB persistence environment for the EclipseCon Boston 2013
Tutorial on profiling C/C++ Applications.

== Setup ==

1) fedora-createiso.sh will create the ISO based on a kickstart file.
In this case we use the fedora-eclipsecon.ks file to define the live
installation. We can make customizations such as :

- Defining specific packages we want (eg. eclipse, eclipse-cdt,
  oprofile, valgrind, etc.)
- Defining user account properties we may want (eg. liveuser should be
  a member of stapdev,stapuser groups)
- Defining additional yum repositories from which to retrieve
  packages.

We must define an architecture as part of the command so that the yum
repositories know what kind of dependencies will be needed.

2) Once we have an ISO created we must burn it to some device.
fedora-burniso.txt contains the commands that may be used for this.
There's one for burning a standard BIOS/MBR boot, and one for an EFI
boot. (They're not very different)


== Additional notes ==

One very important part of providing this environment to users, is the
necessity that everything be set up for them ahead of time. For
example, at EclipseCon, we wanted to have the user start up Eclipse,
with a bunch of plugins already installed. We also we wanted the
projects to be loaded in the workspace.

All of this can be accomplished as follows :

1) Create an RPM that provides the necessary content in the proper
location.

eg. Use rpmbuild on the eclipsecon-setup.spec and corresponding
sources.

2) Create a local yum repository and place it somewhere under the
document root of the local web server. We can use Apache HTTP server,
along with running createrepo on the rpm package folder.

3) Provide the yum repository in the kickstart file
(fedora-eclipsecon.ks)

eg. repo --name=local --baseurl=http://localhost/packages


== Dependencies ==

livecd-tools-18.14-1.fc18.x86_64

== References ==

http://fedoraproject.org/wiki/How_to_create_and_use_Live_USB#Command_line_method:_Using_the_livecd-iso-to-disk_tool_.28Fedora_only.29
