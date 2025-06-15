# Linux

- [General](#general)
- [Man pages](#man-pages)
- [Users and Groups](#users-and-groups)
- [Linux Containers](#containers)
- [Daemons](#daemons)

## General

- "Everything is a file" - Unix treats mostly everything accessible as a file
  that can be read from and written to. All hardware components are represented
  as files and the system uses these files to enable communication between them.
  The idea is an important one and a great property of Linux, where input/output
  resources such as your documents, directories (folders in Mac OS X and
  Windows), keyboard, monitor, hard-drives, removable media, printers, modems,
  virtual terminals and also inter-process and network communication are streams
  of bytes defined by file system space.

## Man pages

Online manual pages or (man pages) represent the most complete Unix/Linux documentation.

### System calls (1)

- `ptrace` (https://man7.org/linux/man-pages/man2/ptrace.2.html) - a system call that provides a way for one process (tracer) to observe and control the execution of another process (tracee).

### User commands (2)

- `lscpu | grep Endian` - displays "endianness of a machine" (note: does not
  possibly work in all distro)
- `whereis` - allows user to locate things that could be files, source and
  manual pages.
- `mv !(new) new` - allows to move all files inside the current directory to be
  moved into "new" directory
- `chmod` - change permissions in Linux (great article -
  https://www.pluralsight.com/blog/it-ops/linux-file-permissions)
- `cp -a /source/. /dest/` - copies files from inside source to dest
- `getfacl` - get file access control lists (get information such as file owner, group etc.)
- `xargs` - pass output from the previous command as input into the next command
- `ps` - report a snapshot of the current, active processes
  - `ps -fC` - full-format listing, of the processes whose name is given in the command list (e.g. `ps -fC node`)

### Library calls (3)

- `realpath` - usage `realpath .` will show you the real path of a directory if
  it's symlinked

## Users and Groups

Each file has associated owner id and group id these help identify which user
and group file belongs to when file is created user ID is taken from the
effective user ID of the process

Example permissions - 775

| Category  | Permissions | Digit | Formula            |
|-----------|-------------|-------|--------------------|
| O (Owner) | rwx         | 7     | 4(r) + 2(w) + 1(x) |
| G (Group) | rwx         | 7     | 4(r) + 2(w) + 1(x) |
| U (User)  | rx          | 5     | 4(r) + 1(x)        |

## Containers

Linux Containers is a virtualisation method for running multiple, isolated Linux systems/containers on a host using a single Linux kernel. 

These are all container primitives:

- cgroups (control groups) - cgroups control resource usage and isolate resource (CPU, memory, network, etc.) usage of a collection of processes.
- namespaces - cgroups and namespace work in tandem to achieve process isolation and resource management. Namespaces help create isolated environments for processes. Such aspects of a process environment as file system, network, process IDs are isolated by the namespaces.
- root fs - specialized file system and top level of Linux file system that contains all of the files required to boot Linux.

### Cgroups (control groups)

- The goal of cgroups is enable fine-grained control over allocating, managing, prioritising and resource monitoring.
- This is one of the Linux container primitives

## What does a modern Linux distribution consist of?                                                                                                               

- Linux kernel (a part of OS that is always resident in memory and it manages and allocates computer resources)
  - Things like drivers, scheduler, networking, security and much more
- Package manager such as Apt for Debian-based distros, Yum
- GNU tools and libraries - such as
  - various command line tools (e.g. GNU coreutils, shell utils, fs utils etc)
  - compilers (e.g. gcc)
  - tooling that comes with compilers (e.g.  make, ld(linker), gbd(debugger), valgrind(memory checker))
- C library
  - glibc (most distros have this)
  - musl (apline-specific)
  - uclibc (mostly for embedded devices)
- Bootloader - a component that loads the OS into memory
- Init system - a component that manages startup and shutdown on a system (e.g. systemd, openrc, busybox init)
- Distribution specific kernel patches (i.e. device drivers)
- Various system daemons
  - systemd-journald for logging
  - cron for scheduling tasks
  - ntpd for time synchronization
- Additional software and documentation
- GUI
  - display server (X11 or Wayland)
  - Desktop environment (GNOME, XFCE, ect.)
  - Window manager - manages how display server displays windows
                                                                                   
## Fundamental concepts

### Directories

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

### User space and kernel space                                                   
                                                                                   
- Modern OSs' virtual memory is normally segmented into user space and kernel space for memory and hardware protection                                       
  - User space - code that runs outside of system's kernel, application software and some drivers. This space is isolated from the kernel space to prevent system corruption and unexpected behaviour.
    - Examples: vim, browsers, bash, gcc etc.
    - User processes cannot access code and data structures of the kernel. However there is a way to interact and communicate with it.
    - This is done via syscalls (or system calls)
    - Simplified example. When a `write()` system call is triggered in the user space, the CPU switches to kernel mode, writes to a file descriptor and returns control to the user space. This is called **context switch** and done by the CPU.
  - Kernel space - the are where Linux kernel runs. Here there's full access to:
    - Hardware (CPU, memory, network etc)
    - System resources
    - Processes and their state
    - Examples: scheduler, VFS (virtual files system, an abstraction between user apps and various file systems), device drivers

## Daemons

- Daemon is a long-lived process usually created during system startup and runs until shutdown.
- It's a process that runs in the background. Almost all daemons have their names end with a `d`.
  - The kernel never auto-generates any job/terminal-related signals such as
    - SIGINT - a signal sent to a process when the user interrupts it (think, Ctrl + C)
    - SIGTSTP - an interactive stop signal and can be handled by the process (like leaving a file system before exiting)
    - SIGNUP - a signal that is sent to the process when a controlling it system is disconnected or closed (e.g. ssh session loss)
- Some of the examples of daemons
  - cron - a daemon that executes commands at a scheduled time
  - httpd  - a http server daemon (Apache)
  - sshd - secure shell daemon (permits logging from remote hosts using a secure communications protocol)

## Memory allocation

- Many dynamic data structures require memory allocation that is only known at run time. These are allocated on the heap.
- Memory (variables) can be dynamically allocated at run time on a "heap". The
  top end of the heap is called program break. Program break lies just past the 
  uninitialised data segment. Program break is raised (heap size is
  increased) functions such as brk(), sbrk() or malloc family functions are called. 
- The current limit of the heap is called *program break*
- More memory can be allocated by the program on heap using C's *malloc* family of functions
- *malloc* functions are based on *brk()* and *sbrk()*. It's about telling the kernel to adjust where the process's program break is, once increased the program can access addresses in the newly allocated area. The physical memory pages are only allocated however when the program access addresses in the pages.
  - *brk()* - sets the program break, program break is the first location after the end of the uninitialised data segment.

```c
// Return 0 on success, -1 on error/failure
int brk(void *end_data_segment)
```

  - *sbrk()* - 

```c
// Return previous program break on success, (void *)-1 on error.
// For clarity, (void *)-1 is the result of casting the integer -1 to void * (generic pointer).
// -1 is not a valid address and is used as a sentinel (signal) value to indicate an error.
void *sbrk(intptr_t increment);
```

## References / resources

- [The Linux Programming Interface](https://man7.org/tlpi/)
- [Advanced Programming in the Unix Environment](https://en.wikipedia.org/wiki/Advanced_Programming_in_the_Unix_Environment)
- [Rust for Linux Project](https://rust-for-linux.com/)
- [The Linux System Administrator's Guide](https://tldp.org/LDP/sag/html/)
- [The Linux Information Project](http://www.linfo.org/usr_bin.html)
- [/proc](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/proc.html)
- [Linux Beginner Boost - Day 4 (May 7, 2020) (dotfiles, vim etc)](https://www.youtube.com/watch?v=xuBiLyCcTzM&list=PLrK9UeDMcQLrO5fwV5smfNvau0PAP16-I&index=4)
- [Intro to Dotfiles](https://thoughtbot.com/upcase/videos/intro-to-dotfiles)
- [An Introduction to Linux Automation, Tools and Techniques](https://linuxconfig.org/an-introduction-to-linux-automation-tools-and-techniques)
- [Linux Container Primitives](https://www.schutzwerk.com/en/blog/linux-container-cgroups-01-intro/)
