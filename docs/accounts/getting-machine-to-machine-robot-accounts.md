# Getting machine-to-machine robot accounts

## Background

API access to different services is getting more and more
popular. Especially most flavours of cloud services have an API. CSC
is running more and more services where APIs are used. The main
examples are Pouta and Rahti. One idea behind APIs is to
programmatically react to situations, e.g. grow resources, deploy
continuous integration and testing workflows, register new data, etc.

The common thing behind these is that:

* They need authenticated access to the platform they're talking to
* There is no human in the loop

Many users have are using their personal accounts to this
purpose. This isn't optimal, since they will be stored somewhere for
automation use, and the same credentials have a much wider access than
they need, which is a security risk. They are also personal
credentials, and they should not be shared in this way.

Some products have ways of handling machine to machine interactions by
themselves, by e.g. generating tokens for a project, which are outside
of IdM. These tokens can be used to access the service's APIs. The
documentation for the robot accounts should have pointers towards
product specific machine to machine token/service account
instructions. Users should primarily use the machine user mechanisms
of the product they are using, as context specific role based access
control can be applied. IdM robot accounts should only be used if no
better alternative exists.

Also, it should still be possible to create robot accounts even if the
service provides some machine to machine method of its own, but that
doesn't cover the intended use case of the robot account in IdM.

## How to get a robot account?

To get a robot account, send us the following details by email:

* 

Our email address is servicedesk@csc.fi.
