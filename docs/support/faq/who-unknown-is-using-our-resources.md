# Who 'unknown' is using our resources

In the
[billing unit usage statistics displayed at MyCSC](../../accounts/how-to-view-billing-unit-usage.md)
you can often see resources used by an 'unknown' user. You and other project
members have also used these billing units.

There are two reasons why the usage is not associated with any particular user.
   
1. The resource belongs to the entire project, not to an individual user. Such
   resources are scratch directory quotas in Puhti and NetApp quotas in ePouta.
   Floating IP addresses in cPouta and ePouta are also shared resources.
1. The reporting database used by MyCSC loses information about who the real
   user is. Currently the user may remain unknown with shortlived virtual
   machines in cPouta and ePouta. In the case of Rahti, all use is currently
   recorded without user information.
