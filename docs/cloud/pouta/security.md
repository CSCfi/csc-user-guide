## Security Guidelines for Pouta

!!! warning
    Users  are responsible for managing
    the  security of  their virtual  machines as  they are  in control  of
    firewalls,  user accounts  and all  other access  control methods  for
    their virtual  machines. Users are  also  responsible for  maintaining
    operating system and application security. 

The virtual machines
running  in cPouta can  be connected  to  the public  internet by  the
users, in  this case the users  should use  strict firewall  rules for
securing their virtual machines.

Below are guidelines that we  recommend all Pouta users follow,  to
ensure the safe  running of virtual machines. Please  follow these. If
you have discovered  a critical security flaw or  believe your machine
has   been    compromised,   please   contact   us    immediately   at
<servicedesk@csc.fi>.

[TOC]

#### Enable Automatic Updates

All operating systems have the ability to apply updates automatically,
and its  easy to turn this  on. Please do so,  and ask us if  you need
help.

#### No Mail Servers

We  hate spam  as much  as you  do! Unfortunately,  it's very  easy to
configure a mail server so that it can be used by spammers. So, we ask
that you  instead use an existing  SMTP server outside the  cloud (see
section 6.1).

#### Upgrade your kernel

Some  updates, such  as  a kernel  upgrade, require  a  reboot of  the
virtual machines. Please schedule this into your regular maintenance.

#### Subscribe to security announcements for your OS

If there is a security problem with your Operating System, you need to
find it out as soon as possible. Find the appropriate mailing list and
keep an eye out for anything that requires urgent action.

#### Run a restrictive firewall

Your instances  should be  configured so that  they allow  the minimum
access required to run the  service. Please use a host-based firewall,
in conjunction with the cloud-provided firewall to manage access.

#### Disable/Remove unneeded accounts

Keep  an eye  on  the  user accounts  enabled  on  your system.   Some
applications  create default  accounts  which are  insecure. An  ideal
scenario  might be  3  accounts -  root (with  ssh  disabled), a  user
account for a sysadmin(key login only)  and a user-level account for a
service(login disabled).

#### Disable password login - use keys

Passwords  are possible,  with enough  time and  compute power,  to be
brute force attacked.  The average  SSH server deals with thousands of
such attacks every week, so use keys to have one less worry.

#### Don't store keys on the image

The cloud  provides a  metadata service  so you  can download  keys on
boot - do use this. This ensures  that if your key is compromised, not
all running instances of that image are compromised.

#### Use tools like denyhosts

Tools like denyhosts,  which look at log files  for attempted breaches
and then firewall out IP addresses  can take your security approach to
a more active level.

#### Disable unneeded services

Know what  services run on your  image, and disable the  unneeded ones
before you upload it. This reduces the attack surface.

#### Use Encrypted Communications

Wherever possible, use encrypted communications to avoid attacks which
intercept data.

#### Use best-practices for logging

Make sure that  services are logging to a secure  location, that is as
tamperproof as  possible. Keep  logs for a  reasonably long  period of
time.  Consider logging to a remote server too.

*Reused        with        kind       permission        from        <a
href="http://support.rc.nectar.org.au/technical_guides/security.html"
class="external-link">NeCTAR</a>.*
