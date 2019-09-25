# Rahti Container Cloud Service Service Level Agreement

## General

This Service Level Agreement (hereafter called "SLA") is made between you (the "User"), Rahti Container Cloud Service ("Rahti") and the service provider, CSC - IT Center for Science Ltd. ("CSC"), to cover the provision and support of the service as described hereafter. Amendments, comments and suggestions must be addressed using the communication channels defined in the section [Communication, reporting and escalation](#communication-reporting-and-escalation). The service provider retains the right to introduce changes to the service. If the User does not accept the changes, this service subscription can be terminated.

## Scope and description of the service

Rahti is a cloud computing service that allows Users to host applications and
make them accessible over the web. The Rahti service is based on OKD, which is a
distribution of Kubernetes. The main features of Rahti are:

* Hosting of containerized applications
* Storage services
* Virtual networks for connecting container instances
* Load balancing of traffic to User Applications
* An application catalog with templates for ready-to-use common applications
* Features for replication, rolling updates, auto-recovery and auto-scaling of User Applications
* Basic default domain name and TLS for hosted User Applications (under rahtiapp.fi)

Users can manage their resources using a web interface accessible through a web
browser and through a set of APIs which allow programmatic management of
resources. In order to access and use the service the User must have a CSC user
account.

The User's applications are isolated from other Users’ applications from a
network, storage and computational view.

## Service hours & exceptions

The service is designed to run continuously. However, the following exceptions apply:

* Planned service breaks - announced to Users at least three weeks in advance.
* Downtimes caused due to upgrades for fixing critical security issues are not considered SLA violations. In the case of critical security upgrades CSC reserves the right to apply the upgrades with minimal notice.
* Any other causes outside the service provider’s direct control.

## Service components & dependencies

The Rahti service depends on the following services:

* Kajaani datacenter infrastructure
* Funet network
* The cPouta service
* CSC user administration
* CSC Servicedesk for user support

## Support

Support for the services covered by the scope of this SLA are provided through CSC Service Desk channels and under CSC Service Desk policies:

| CSC Service Desk ||
--- | ---
Operating hours | Mon-Fri (excluding Finnish public holidays), see [CSC's contact information page](https://www.csc.fi/en/contact-info)
Phone |  +358 (0) 94 57 2821
Email | servicedesk@csc.fi
Webpage and contact form | https://research.csc.fi/cloud-computing https://research.csc.fi/support
Response time target | Within three working days

### Incident handling

Disruptions to the agreed service functionality or quality will be handled according to an appropriate priority based on the impact and urgency of the incident. In this context, the following general priority guidelines apply:

1. Ensuring normal levels of security
2. Restoring normal service operation
3. Restoring User Applications where possible

Response and resolution times are provided as [Service level targets](#service-level-targets).

### Fulfilment of service requests

In addition to resolving incidents, the following standard service requests are defined and will be fulfilled through the defined support channels:

* Issues regarding CSC’s identity management service
* Issues using this service’s web interface
* Issues using the provided APIs
* Issues deploying applications
* Issues using application templates
* Changes to quotas

Response and fulfilment times are provided as [Service level targets](#service-level-targets).

## Service level targets

The Rahti service level targets adhere to JHS 174 as follows:

Service level targets ||
--- | ---
Service Level | A (basic)
Service time / incident handling | P1 Weekdays 8.00-16.00
Availability | K1 97%
Response | V1 reaction: 4h, solution: 2 BD

Availability is calculated by subtracting the service break time from the ideal availability during service time. This information is obtained from internal monitoring systems and defined as Users’ ability to manage their User Applications, and the availability of the User Applications.

The normal functioning of the service is defined as:

* the ability to launch new User Applications.
* the availablility and integrity of the storage services.
* the functioning of the network, and the accessibility of User Applications.
* the functioning of replication, auto-recovery and auto-scaling of User Applications.

The Service Provider commits to inform the User if this SLA is violated or a violation is anticipated. For this, email as a communication channel will be used.

A User contacts the CSC Service Desk for the case of a possible SLA violation. The case will be analysed internally and, if the violation is confirmed, CSC will inform the User about the reasons for the violation, planned mitigation actions and expected resolution time.

## Limitations and constraints

The provisioning of the service under the agreed service level targets is subject to the following limitations and constraints:

* Support is provided primarily in English and Finnish.
* A technical failure which affects individual Users does not count as downtime.
* Failures of single container instances is expected behaviour and do not count as downtime.

## Communication, reporting and escalation

### General communication

The following contacts will be generally used for communications related to the service in the scope of this SLA:

| Communication channels ||
--- | ---
Contact for Users | servicedesk@csc.fi
Security incident reporting | (CSC’s Head of Security) security@csc.fi +358 (0) 94 57 2253

### Reporting

Service reports regarding availability will be available from the servicedesk by request. The information provided will be limited to service availability and by data security and privacy constraints.

### Escalation and complaints

For escalation and complaints, the defined contact point shall be used, and the following rules apply:

1. First contact shall be established, preferably by email, to Contact for Users address (See section [Communication, reporting and escalation](#communication-reporting-and-escalation)) explaining the reason for the complaint with a sensible level of detail and clarity. Please also include, if possible, the following information:
    * Name of the service
    * Date and time of the events
    * Usernames of affected Users
    * Channel to use on following communications (if other is preferred)
1. CSC Service Desk will contact you within three working days with information about the incident and which procedures will be adopted.

## Information security & data protection

CSC has approved a security policy and also follows security best practices. For CSC's customers, partners and staff there are detailed security guidelines. Many items in our security policies and guidelines refer to external compliance requirements. CSC also has procedures for risk and security management. For more information, please refer to:

* [CSC’s Security Policy](https://www.csc.fi/security)
* [The Rahti documentation](https://rahti.csc.fi)

The handling of personal information on the Rahti service is described here: https://research.csc.fi/rahti

## Additional responsibilities of the Service Provider

Additional responsibilities of the Service Provider are as follows:

* Adhere to all applicable operational and security policies and procedures defined in CSC’s Security Policy ([Information security & data protection](#information-security--data-protection)) and to other policy documents referenced therein.
* Use communication channels defined in the agreement.
* Provide monitoring data to measure fulfillment of agreed service level targets.

## User responsibilities

The User agrees to follow the [General Terms of Use for CSC's Services for Research](https://www.csc.fi/general-terms-of-use), [User policy and terms of use for the Rahti container cloud service](https://rahti.csc.fi/introduction/terms_of_use/) and [CSC’s Security Policy](http://www.csc.fi/security).

## Review

There will be reviews of the service performance against service level targets and of this SLA at planned intervals according to the following rules:

* Annual reviews are done internally and based on User feedback.
* Major changes to the service may trigger a review.

## Glossary of terms

For the purpose of this SLA, the following terms and definitions apply:

* *SLA*: Service Level Agreement (this document)
* *Response time*: Time spent between the arrival of a User's support request and the first response from CSC Staff
* *Working days*: Monday to Friday (excluding Finnish public holidays)
* *Working hours*: as defined in customer service opening hours in [CSC's contact information page](https://www.csc.fi/en/contact-info)
* *Rahti container cloud service ("Rahti")*: a cloud platform that can be used by *Users* to run their own *User Applications*.
* *Rahti User ("User")*: a user of *Rahti*.
* *User Application*: an application running in *Rahti* managed by one or more *Users*.

An extended list of term definitions adopted on this document can be found in the [FitSM-0: Overview and vocabulary document](https://fitsm.itemo.org/wp-content/uploads/sites/3/2018/05/FitSM-0_Overview_and_vocabulary.pdf).

## Document revision

This document was last updated 30.4.2019

