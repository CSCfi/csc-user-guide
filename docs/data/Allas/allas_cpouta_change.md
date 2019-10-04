# Allas and cPouta object storage, what changes?

We have releases a new object storage service, **Allas**, which will be central for data management at CSC.

You might wonder how this affects cPouta object storage users?

In short, Allas is an evolution of cPouta object storage. If you are already using cPouta object storage, you can keep using it as you are currently doing. All your data will be carried over to Allas.

## What should I know about this change?

Allas will be a new service at CSC. All existing projects with cPouta access will also have Allas access by default. Any projects requesting cPouta access after the service launch will only get access to cPouta, not Allas. Allas access will have to be requested separately.

Any data uploaded to Allas is by default found under the "_a3s.fi_" domain instead of "_object.pouta.csc.fi.fi_" domain. The old domain name can still be used to access data.

The _billing unit_ costs of Allas will drop significantly compared to Pouta. The performance of the service is also much improved.

In the future, the documentation of Allas can be found here. The old cPouta object storage documentation will be deprecated.

When is Allas released, and what happens then?

The technical release date for the Allas service was 29.9.2019. The following things changed:

 * The default domain name for that data will change from _a3s.fi_ to _a3s.fi_. The old names will keep working.
 * The default URLs to access the service will change. The old URLs will keep working.
 * When a project request service access to cPouta, they no longer get Allas access automatically.
