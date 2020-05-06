# Increasing the storage capacity in Puhti

The quotas of the scratch and projappl directories of Puhti server can be increased if needed.

You can use MyCSC to manage these quotas.

1.    Login to [MyCSC](https://my.csc.fi) and **select the project** you want to modify.
2.    In the Services list, click open the settings for **Puhti** service. This opens a page 
      where the project manager can modify the quotas.

Note that the extended scratch quota consumes your CSC billing units regardless of how much 
data you actually have in the scratch directory. See billing for details. Furthermore, 
even after the quota is increased, the automatic cleaning process will continue removing idle 
files from the scratch directory.
