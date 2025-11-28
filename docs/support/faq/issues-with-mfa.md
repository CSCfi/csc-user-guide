# How to solve issues with multi-factor authentication (MFA)

## Error: "The provided code is wrong or has been expired. Please try again."

To solve the problem:

1. Ensure that the date and time settings of your device are set to "Automatic"
   or synced with the network. Check the time from your phone settings:
    1. **Android**: *Settings* :material-arrow-right: *System*
       :material-arrow-right: *Date and time* :material-arrow-right:
       *Set time automatically* has to be *on*.
    2. **iPhone**: *Settings* :material-arrow-right: *General*
       :material-arrow-right: *Date & time* :material-arrow-right:
       *Set time automatically* has to be *on*.
2. If the previous step does not work, please delete the CSC MFA secret from
   your phone and start from the very beginning, including scanning the QR
   code (i.e. reset MFA completely).
    1. [See instructions](../../accounts/mfa.md#how-to-activate-csc-mfa).
