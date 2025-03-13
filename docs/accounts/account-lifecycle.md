# CSC user account lifecycle

The password of your CSC user account is valid for one year. You will receive
notifications from CSC when your password is about to expire. An expired
password will not lock you out of your CSC user account if you use one of the
following three login methods: Haka, Virtu, or an SSH key pair. These three login
methods effectively bypass the need for a CSC user account password.
Nevertheless, **we strongly recommend you to change your password in time**.

If your CSC user account password expires and you cannot login via Haka, Virtu
or using SSH keys, please [contact CSC Service Desk](../support/contact.md).

[MyCSC](https://my.csc.fi) is our customer portal from where our customers can
see the state of their projects and details of their user accounts. In MyCSC
you may also
[change the password of your CSC user account](how-to-change-password.md).
MyCSC and other services of CSC offer one or more of the login methods
mentioned below.

## CSC user account

In this login method you use the user account created for you by CSC and the
password you have set for the user account. All users who have been granted
access to CSC's services have a CSC user account, even if they only use one of
the login methods mentioned below.

## Haka

This login method is available to Finnish universities, polytechnics and
research institutions. In this login method you use the user account and
password of your home organization instead of the user account provided by CSC.
This works because a unique user ID from your home organization is linked to
your CSC user account.

If you use this login method, you will have to login to CSC services via Haka
at least once every 6 months to keep your CSC user account active.

## Virtu

This login method is available to government agencies. Similar to Haka, in this
login method you use the user account and password of your home organization
instead of the user account provided by CSC. This works because a unique user
ID from your home organization is linked to your CSC user account.

If you use this login method, you will have to login to CSC services via Virtu
at least once every 6 months to keep your CSC user account active.

## LS Login

LS Login is an authentication service of the European Life Science Research
Infrastructures (LS RI), which is a community platform established via the
EOSC-Life project and operated by Masaryk University, Brno, CZ. Also here, a
unique user ID from LS Login is linked to your CSC user account that allows
authentication in CSC services.

## SSH keys

SSH keys are functionally similar to usernames and passwords and provide means
to access CSC systems in a secure manner, but without having to manually type
your username and password each time. Only a specific subset of CSC services
support SSH keys. For example, they are not supported in any web browser-based
login methods.

SSH keys are linked to your CSC user account, and they work based on a
comparison of the public key you've uploaded to a certain CSC system with the
private key you keep safely stored on your local computer.

[See instructions for how to set up SSH keys](../computing/connecting/ssh-keys.md).

## Expiration of user accounts

If you have been granted an account for a fixed period, the account expires
when the period ends. Accounts created with Haka or Virtu are validated
periodically. The following methods can be independently used to login
depending on the service: Haka, Virtu, password, or SSH keys.

User accounts may be closed if their owner is not reachable, i.e. emails bounce
back.

!!! Note
    If you want to terminate your account, please
    [contact CSC Service Desk](../support/contact.md).
