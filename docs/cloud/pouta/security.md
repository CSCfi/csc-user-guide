## Pouta security guidelines

!!! warning
    The users are responsible for managing
    the security of their virtual machines as they are in control of the
    firewalls, user accounts and all other access control methods of
    their virtual machines. The users are also responsible for maintaining
    the operating system and application security. 

The virtual machines
running in cPouta can be connected to the public internet by the
users. The users should use strict firewall rules for
securing their virtual machines.

We recommend the following guidelines for all Pouta users to follow, to
ensure the safe running of virtual machines. If
you have discovered a critical security flaw or believe your machine
has been compromised, please contact us immediately at
<servicedesk@csc.fi>.

[TOC]

#### Enable automatic updates

All operating systems have the ability to apply updates automatically,
and it is easy to turn this on. Please do so, and ask us if you need
help.

#### No Mail Servers

We hate spam as much as you do. Unfortunately, it is very easy to
configure a mail server so that it can be used by spammers. So, please
instead use an existing SMTP server outside the cloud (see
section 6.1).

#### Upgrade your kernel

Some updates, such as kernel upgrades, require rebooting the
virtual machines. Please schedule this into your regular maintenance.

#### Subscribe to security announcements for your OS

If there is a security problem in your operating system, you need to
find it out as soon as possible. Find the appropriate mailing list and
keep an eye out for anything that requires urgent action.

#### Run a restrictive firewall

Your instances should be configured so that they allow the minimum
access required to run the service. Please use a host-based firewall,
in conjunction with the cloud-provided firewall to manage access.

#### Disable/remove unneeded accounts

Keep an eye on the user accounts enabled in your system. Some
applications create default accounts which are insecure. An ideal
scenario might be three accounts: root (with ssh disabled), a user
account for a sysadmin (key login only) and a user-level account for a
service (login disabled).

#### Disable password login – use keys

Passwords can be, with enough time and compute power, attacked with brute force. 
The average SSH server deals with thousands of
such attacks every week, so use keys to have one less worry.

#### Do not store keys on the image

The cloud provides a metadata service so that you can download keys on
boot. This is recommended. It ensures that if your key is compromised, not
all running instances of that image are compromised.

#### Use tools like denyhosts

Tools such as _denyhosts_, which look at log files for attempted breaches
and then firewall out IP addresses, can take your security approach to
a more active level.

#### Disable unneeded services

Know what services run on your image and disable the unnecessary ones
before you upload it. This reduces the attack surface.

#### Use encrypted communications

Wherever possible, use encrypted communications to avoid attacks which
intercept data.

#### Use the best practices for logging

Make sure that the services are logging to a secure location, that is as
tamper-proof as possible. Keep the logs for a reasonably long. 
Consider logging to a remote server as well.

*Reused with kind permission from <a
href="https://support.ehelp.edu.au/support/solutions"
class="external-link">NeCTAR</a>.*
