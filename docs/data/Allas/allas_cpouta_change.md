# Allas and cPouta object storage, what changes?

We are releasing a new object storage service, Allas, which will be central for data management at CSC.

You might wonder how this affects cPouta object storage users?

In short, Allas is an evolution of cPouta object storage. If you are already using cPouta object storage, you can keep using it as you are currently doing. All your data will be carried over to Allas.

CAVEAT: VERSIONED BUCKETS

## What should I know about this change?

Allas will be a new service at CSC. All existing projects with cPouta access will also have Allas access by default. Any projects requesting cPouta access after the service launch, will only get access to cPouta, not Allas. Allas access will have to be requested separately.

Any data uploaded to Allas is by default found under the "a3s.fi" domain instead of "object.pouta.csc.fi" domain. The old domain name can still be used to access data.

The Billing Unit cost of Allas will drop significantly compared to Pouta. The performance of the service is also much improved.

The documentation of Allas can in the future be found here: INSERT LINK. The old cPouta object storage documentation will be deprecated.

When is Allas released, and what happens then?

The release date for the Allas service is x.y.2019. The following things will change at that time:

 * The default domain name for that data will change from object.pouta.csc.fi to a3s.fi. The old names will keep working.
 * The default URLs to access the service will change. The old URLs will keep working.
   * ENTER EXACT CHANGES HERE
 * When a project request service access to cPouta, they no longer get Allas access automatically.

