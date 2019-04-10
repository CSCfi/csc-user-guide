## Pouta Object Storage Benefits

Object storage  is generally  used for a  different purpose  that many
other storage solutions.  It has  benefits but also limitations. These
are some of the  benefits, but once you start using  it, you are bound
to find more.

-   You do  not need to set  up a virtual machine to  serve or receive
    the data.
-   The data can be accessed from anywhere using the same URL.
-   The data can have different levels of access control.

### Limitations

-   Object  storage   can't   be  properly   mounted  on   virtual
    machines. There are  some tools to help this, but  they have their
    limitations.   For example  svfs can  be  used to  mount swift  as
    filesystem but it uses FUSE which is slow.
-   Unsuitable for  objects/files that  change during  their lifetime
    (e.g.  most databases).
