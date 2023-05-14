# Linux

- "Everything is a file" - Unix treats mostly everything accessible as a file
  that can be read from and written to. All hardware components are represented
  as files and the system uses these files to enable communication between them.
  The idea is an important one and a great property of Linux, where input/output
  resources such as your documents, directories (folders in Mac OS X and
  Windows), keyboard, monitor, hard-drives, removable media, printers, modems,
  virtual terminals and also inter-process and network communication are streams
  of bytes defined by file system space.
- daemon (background processes) - is a Linux / Unix program process that runs in
  the background. Almost all daemons have their names end with a `d`.

## User and Groups

Each file has associated owner id and group id these help identify which user
and group file belongs to when file is created user ID is taken from the
effective user ID of the process

r - 4 w - 2 x - 1

775 (O - rwx, G - rwx, U - rx)

## Tools

- `ptrace` - trace system calls
- `xargs` - pass output from the previous command as input into the next
    command 

## Directories

- `/usr` - general user system-wide applications / programs are stored here
  - `/sbin` - Non-essential standard system binaries that are used by the system
    administrator
  - `/bin` - Contains most of the executables that are not required for booting
    up the system
  - `/local` - locally installed software and files are located here and are
    used by the local administrator (not available to other users on machine);
    updates to distro will not overwrite any software here. 
- `/dev` - special device files for all the devices. 
  - `/sda1` - `sd` the  way Linux (Unix'es) names its drives. sd - from the old
    days of scsi which became a catch-all case for anything that stores devices.
    `a` find order. `1` is the partition on the device. `/dev/sda5` - 5th
    partition on the first drive.
  - `/loop` - not real device that makes file accessible as a block device.
  - `/null` - blackhole, anything written into it gets discarded
- `/proc/<pid>` - virtual file system, process information pseudo-file system.
  Process information can found here.
- `/var` - this is where data that is changed when the system is running
  normally located.
  - `/var/lib` - files that change while system is running normally

## Commands

- `whereis` - allows user to locate things that could be files, source and
  manual pages.
- `mv !(new) new` - allows to move all files inside the current directory to be
  moved into "new" directory
- `chmod` - change permissions in Linux (great article -
  https://www.pluralsight.com/blog/it-ops/linux-file-permissions)
- `cp -a /source/. /dest/` - copies files from inside source to dest
- `getfacl` - get file access control lists (get information such as file owner,
  group etc.)
- `realpath` - usage `realpath .` will show you the real path of a directory if
  it's symlinked
- `lscpu | grep Endian` - displays "endianness of a machine" (note: does not
  possibly work in all distro)

## Containers

Linux Containers is a virtualisation method for running multiple, isolated Linux systems/containers on a host using a single Linux kernel. 

These are all container primitives:

- cgroups (control groups) - cgroups control resourse usage and isolate resource (CPU, memory, network, etc.) usage of a collection of processes.
- namespaces - cgroups and namespace work in tandem to achieve process isolation and resource management. Namespaces help create isolated environments for processes. Such aspects of a process environment as file system, network, process IDs are isolated by the namespaces.
- root fs - specialized file system and top level of Linux file system that contains all of the files required to boot Linux.

## Memory allocation

- Memory (variables) can be dynamically allocated at run time on a "heap". The
  top end of the heap is called program break. Program break lies just past the 
  uninitialised data segment. Program break is raised (heap size is
  icreased) functions such as brk(), sbrk() or malloc family functions are called. 

### References / resources

- The Linux System Administrator's Guide - https://tldp.org/LDP/sag/html/
- The Linux Information Project - http://www.linfo.org/usr_bin.html
- /proc - https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/proc.html
- Linux Beginner Boost - Day 4 (May 7, 2020) (dotfiles, vim etc) -
  https://www.youtube.com/watch?v=xuBiLyCcTzM&list=PLrK9UeDMcQLrO5fwV5smfNvau0PAP16-I&index=4
- Intro to Dotfiles - https://thoughtbot.com/upcase/videos/intro-to-dotfiles
- [An Introduction to Linux Automation, Tools and Techniques](https://linuxconfig.org/an-introduction-to-linux-automation-tools-and-techniques)