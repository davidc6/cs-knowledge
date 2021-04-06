# Linux

* "Everything is a file" - Unix treats mostly everything accessible as a file that can be read from and written to. All hardware components are represented as files and the system uses these files to enable communication between them. The idea is an important one and a great property of Linux, where input/output resources such as your documents, directories (folders in Mac OS X and Windows), keyboard, monitor, hard-drives, removable media, printers, modems, virtual terminals and also inter-process and network communication are streams of bytes defined by file system space.
* daemon (background processes) - is a Linux / Unix program process that runs in the background. Almost all daemons have their names end with a `d`.

## Directories

`/usr` - general user system-wide applications / programs are stored here
  * `/sbin` - Non-essential standard system binaries that are used by the system administrator
  * `/bin` - Contains most of the executables that are not required for booting up the system 
`/dev` - special device files for all the devices. 
  * `/sda1` - `sd` the  way Linux (Unix'es) names its drives. sd - from the old days of scsi which became a catch-all case for anything that stores devices. `a` find order. `1` is the partition on the device. `/dev/sda5` - 5th partition on the first drive.
  * `/loop` - not real device that makes file accessible as a block device.
  * `/null` - blackhole, anything written into it gets discarded


## Commands

* `whereis` - allows user to locate things that could be files, source and manual pages.
* `mv !(new) new` - allows to move all files inside the current directory to be moved into "new" directory
* `chmod` - change permissions in Linux (great article - https://www.pluralsight.com/blog/it-ops/linux-file-permissions)
* `cp -a /source/. /dest/` - copies files from inside source to dest

### References / resources

* The Linux System Administrator's Guide - https://tldp.org/LDP/sag/html/
* The Linux Information Project - http://www.linfo.org/usr_bin.html
