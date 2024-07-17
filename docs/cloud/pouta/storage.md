# Pouta storage

There is at least one type of storage available on every virtual machine, which
is the file system defined by the virtual machine image. This is the primary
disk of the virtual machine, also called root disk. Nevertheless, the space
available is typically limited and the lifetime of the data in it is limited by
the virtual machine, i.e., the data is erased once the virtual machine is
deleted. This article introduces the storage options available in CSC's cloud
environment. Using the storage requires an account, a project, and a virtual
machine.

## Ephemeral storage

Depending on the chosen flavor, a virtual machine may have a certain amount of
additional local disk space, called **ephemeral storage** in the OpenStack
terminology. This storage is visible on the virtual machine as a second hard
disk.

The main advantage of the ephemeral storage is performance, as the data is
stored in the hard disk of the server where the virtual machine is running.
Nevertheless, the ephemeral storage is available only when the virtual machine
is running. In addition, similarly to the data in the primary disk, the data in
the ephemeral storage is lost too when you delete the virtual machine. Given
that the data in the ephemeral storage is not replicated, you should not store
any persistent data there, and the ephemeral storage should not be considered
reliable.

You can find additional information on the
[ephemeral storage page](ephemeral-storage.md).

## Persistent volumes

If you are looking for a storage space which can be accessed like an additional
hard disk, and which is not tied to a single virtual machine, you are looking
for **persistent volumes**. You can attach a persistent volume to a virtual
machine, and use it as you would use the ephemeral storage. Nevertheless, you
can also detach it from the virtual machine and attach it to another virtual
machine. In other words, you are free of deleting and recreating your virtual
machines using the persistent volume, as a persistent volume is not tied to the
lifetime of a single virtual machine. Moreover, persistent volumes represent a
reliable storage option as the data in them is replicated.

You can find additional information on the
[persistent volumes page](persistent-volumes.md).

## Object storage

In case you need a storage space where your data can be easily accessed over
the Internet, e.g., using URLs, **object storage** is the storage solution you
are looking for. By using object storage, you are free to create and delete
your virtual machines as the object storage is not tied to any virtual machine.
Moreover, your data is replicated, thus object storage represent a reliable
storage option.

At CSC, we offer Allas as our object storage solution.
You can find additional information on the
[Allas page](../../data/Allas/index.md).

## Snapshots

Sometimes you just want to have a backup copy of the data in a virtual machine
or in a persistent volume. Alternatively, you might be interested to save the
current state of a virtual machine, so that you can start other virtual
machines cloning the same state. In these cases, you can use **snapshots**.

You can find additional information on the [snapshots page](snapshots.md).
