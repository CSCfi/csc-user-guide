# Known problems and limitations

## Instances

-   **Instance snapshots sometimes fail. This leaves the instance in
    the suspended state. To work around this issue, we recommend the users
    power off their VM before taking a snapshot.**
-   Child instances launched using the snapshot of an existing parent
    instance do not have a security group predefined. 
    Please select the appropriate security group for
    child instances before launching them.
-   Resizing inside a flavor family (within standard.\*) is
    possible  except for IO flavors. Resizing between flavor
    families mostly does not work because of the different storage
    backends. If you use a volume for the root disk, some resizes
    between flavor families do work. If you use a image for the root disk,
    it is possibly dangerous. Always test resizes with an expendable VM you
    first. If your virtual machines end up in an "error"
    state, please contact us.
-   Network: It is possible to add the same floating IP to multiple
    instances using the API. There is no warning or error. The last
    API call is the one which takes effect.
-   Volumes: There is no guarantee that device names will get the same
    name after a rebuild or reboot. If you want to be sure that the
    correct device gets mounted to the same path every time it is a good
    idea to use UUIDs instead of paths.
-   Ubuntu-20.04 images and hpc.6 flavor are unable to boot. A bug prevents
    instances with Ubuntu 20.04 (created or updated) and flavor hpc.6.*
    from booting. We expect a future update to fix this, but in the meantime
    avoid this combination.

## EC2 tools (euca2ools)


-   EC2 is presently not supported. EC2 credentials can, however, be
    used with the object storage.

## [Pouta FAQ entries](../../../support/faq/#pouta)

