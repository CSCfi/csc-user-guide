# Known problems and limitations

## Instances

-   **Instance snapshots  sometimes fail. This leaves  the instance in
    the suspended state.  To work  round this issue we recommend users
    power off their VM before taking a snapshot.**
-   Child  instances launched  using the  snapshot of  existing parent
    instance  does not  have security  group predefined  as of  parent
    instance,   please  select   the appropriate security  group   for
    child instances before launching them.
-   Resizing  inside  a  flavor family  (so  within  standard.\*)  is
    possible   except  for   IO  flavors.   Resizing  between   flavor
    families mostly  do  not work  because  of  the different  storage
    backends. If you use a volume  for the root disk then some resizes
    between flavor  families work. If  you use  a image for  root disk
    then it's possibly  dangerous.  Always test resizes with  a VM you
    can spare  first. If your virtual  machines end  up in  an "error"
    state please contact us if this happens.
-   Network:  It's possible to  add the  same floating IP  to multiple
    instances using  the API. There is  no warning or error.  The last
    API call is the one which takes effect.
-   Volumes: There is no guarantee that device names will get the same
    name after a rebuild or reboot. If you want to be sure that the
    correct device gets mounted to the same path every time it is a good
    idea to use UUIDs instead of paths.

## EC2 tools (euca2ools)

-   EC2 is not supported at  this time. EC2 credentials can however be
    used with the Object Storage.

## [Pouta FAQ entries](../../../support/faq/#pouta)
