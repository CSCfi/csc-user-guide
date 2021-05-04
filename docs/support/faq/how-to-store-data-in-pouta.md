# How to store data on Pouta?

Pouta provides two choices which are [not backed up by CSC](is-pouta-backed-up.md):

*   Temporary storage via local disks attached to virtual machines. OpenStack calls this ephemeral (meaning "lasting for a very short time") storage.
*   Longer term storage via _Volumes_. Volumes appear as raw disks attached to virtual machines. See:
    *   [What are volumes? How to use them?](what-are-volumes-and-how-to-use.md)

Alternatives:

Users are free to use any other storage outside of Pouta, either directly or on ephemeral storage or volumes. It's also possible to use other CSC storage services. See:

*   [Allas object storage](/data/Allas/)
*   [How do I access the CSC archive service?](how-to-access-csc-archive-services-from-cpouta.md)
