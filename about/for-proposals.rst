Boilerplate text for grant proposals
====================================

Below are various texts which describe Aalto Science IT, Aalto ITS, and CSC resources, suitable for
inclusion in grant applications an the like.  There are various types
suitable for different purposes.

If you create your own texts and would like to share them, send them
to us.

.. warning::

   These texts are starting points, not something that should be
   included as-is. The texts need to be adapted and tailored to fit
   your particular proposal - if you need help with proposal writing
   you can contact the Grant Writer or Research Liaison Officer of
   your School for advice (`contact information is available here
   <https://www.aalto.fi/en/services/research-and-innovation-services#3-school-teams-helping-researchers>`__).



Focus on Triton
---------------

Computing and modelling are strategic areas of Aalto University. To
support research in these scopes the university is committed to
provide proper hardware resources and supporting personnel on long
term basis. Currently Aalto Science-IT provides a system with about 10000 computing
cores. The System also contains over 200 NVIDIA cards for
GPU computing and over 5 PB of fast storage capacity suitable for Big
Data needs. All parts are connected with a fast Infiniband network to
support parallel computing and fast data access. To keep the resources
competitive Aalto Science-IT annually upgrades the system based on the needs of
researchers.

All resources are integrated with the national resources allowing easy
migration to even larger resources when necessary. These include
e.g. University dedicated OpenStack based cloud resources and access
to thousands of servers via the national computing grid. Furthermore
Aalto Science-IT provides much preconfigured software and hands on support to make
the usage for researchers as effective as possible. On the personnel
side Science-IT has ten permanent Ph.D. level staff to keep the system
running and providing teaching and consultation for researchers.


Acknowledging Triton in publications
------------------------------------


Remember you need to acknowledge Aalto Science-IT in your papers if you 
use Triton and its scratch filesystem.  See the
:doc:`acknowledging Triton page </triton/acknowledgingtriton>` for
instructions on how to do that and some boilerplate text.



Focus on data
-------------


Computing and data are strategic areas in Aalto University.

The university provides data management and computing solutions
throughout the data lifecycle.  The university provides free storage
to researchers of essentially unlimited size, provided that the data
is managed well.  Data storage includes 5PB of high-performance 
non-backed-up Lustre filesystem space connected directly to the Triton computing 
cluster for efficient and secure analysis, and 1PB of reliable backed-up 
storage space for longer-term storage. Expert staff, both technical and 
administrative, provide advice and hands-on support in data storage,
computation, FAIR principles, data management planning, as well as
computation.

Data management is designed with a focus on security.  Recommended
storage locations are centrally located for security.  Computing nodes 
and Lustre data storage servers are physically located at CSC, Keilaranta 
14, Espoo. The server room is certified security level 3 (VAHTI-3) i.e. 
only authorized personnel with clearance are given access to it and there 
is continuous camera surveillance. All data is access controlled by passwords 
and individual-level authorization, and firewalled to university networks.

Aalto ITS data storage is directly integrated into Aalto’s sustainable 
computing environment. Storage is double-redundant and includes the possibility 
to roll back to previous points in time, with disaster recovery management. 
In addition to confidential data processing, there are multiple encrypted and/or 
audited storage environments for sensitive data processing. For IoT, Aalto ITS 
utilizes public cloud computing providers for case-specific construction of services. 
Aalto has IT infrastructure personnel, who can help researchers with building the relevant 
solution for the use case.  


Focus on sensitive data
-----------------------

Aalto university provides secure solutions for data management and computing throughout the data lifecycle. The university has an Information Security Management System (ISMS) in place, adapted from the ISO 27001 standard. These processes govern how all our IT systems are being acquired, developed, implemented, operated and maintained. Based on the information classification, we use only selected systems that comply with high security requirements and have been approved for use with sensitive data. 

We use encryption technologies to safeguard sensitive data in transit and ensure secure collaboration. Our secure network storage is encrypted at rest, includes the possibility to roll back to previous points in time, and supports encrypted backups for disaster recovery. 

We operate a dedicated secure computing environment SECDATA to enable research with most sensitive data. The environment has been audited to comply with the Act on the Secondary Use of Health and Social Data and Findata requirements. Each research project will get a separate virtual desktop environment with customized amounts of memory, disk space, and computing power with a possibility to use GPUs for computational tasks. To safeguard data, transfers are limited and done only through specific audited process and the environment is disconnected from the public internet. 

Our technical, administrative, and legal experts provide advice and hands-on support for handling sensitive data. The Aalto Research Software Engineer (RSE) team and Data Agents help with essential privacy techniques such as minimization, pseudonymization, and anonymization. Aalto's Data Protection Officer provides guidance and oversight on the processing of data and ensuring privacy. 

Confidential data (shorter, for CS)
-----------------------------------

Aalto CS provides secure data storage for confidential data. This data
is stored centrally in protected datacenters and is managed by dedicated
staff. All access is through individual Aalto accounts, and all data is
stored in group-specific directories with per-person access control.
Access rights via groups is managed by IT, but data access is only
provided upon request of the data owner. All data is made available only
through secure, encrypted, and password-protected systems: it is
impossible for any person to get data access without a currently active
user account, password, and group access rights. Backups are made and
also kept confidential. All data is securely deleted at the end of life.
CS-IT provides training and consulting for confidential data management.




Focus on connectivity  
---------------------


Aalto researchers can use the Low Power Wide Area Network (LoRaWAN), a data network for Internet of things (IoT) devices with nationwide coverage, free of charge. Using this network, a device can send a small amount of data with minimal power which makes batteries last long. LoRaWAN is suitable for static and mobile sensors that are operated by batteries. Aalto IT services provide support and configure the network together with the user. In Finland, public mobile networks support also NB-IoT (Narrowband IoT) technology. 

Aalto campus area has a specific research environment for 5G connectivity, that can be used for developing and testing 5G technology and applications.  
On the campus area connectivity is ensured via a 100 Gbit/s fault-tolerant internet connection, 1 – 10 Gbit/s connections to workstations and servers, and extensive wireless coverage. Secure connectivity outside Aalto-campus is also possible by various technologies, e.g. VPN.  


Research environment: research software engineers
-------------------------------------------------

The Aalto Research Software Engineer (RSE) team provides a specialized
advice and service in research software, data, and computing so that
any researcher can accomplish the best science without being held back
by technological problems.  Typical tasks including implementing a
method bettor or faster than could otherwise be done, or ensuring that
results are as open and reusable as possible so that the full impact
of the work can be realized.  RSE staff are professional researchers
with years of experience in computational sciences, and work
seamlessly with the rest of the Science-IT team.  For the School of
Science, basic services are included as part of overheads, or
longer-term services can be funded from specific research projects.



Research software engineering services
--------------------------------------

.. seealso::

   :doc:`/rse/grant-applicants`

(this text must be tuned to your grant, replace the parts in CAPITAL LETTERS)

This grant will make use of the Aalto Research Software Engineer
program to hire high-quality TOPIC specialists.  This program provides
PhD-level personnel to work on THINGS, which allows the other staff
on this project to focus on YYY.  Research software engineers do not need to be
independently recruited, and are available for consultation also before and
after the project.  This service is provided by Aalto Scientific
Computing, which also provides high-performance computing resources for your project.
The Research Software Engineering service is integrated into computing
services as a consistent package.

(for basic service, for now only SCI) The service is available as a
basic consulting service for free.

(for paid services) This project receives dedicated service from the
Research Software Engineering group, funded as researcher salary from
this grant.  During this period, one of the Aalto research software engineers joins this
project as a researcher, equal to all other project employees.



Research infrastructure: Aalto University Data Hub (AUDH)
---------------------------------------------------------

Aalto University Data Hub (AUDH - datahub.aalto.fi/en) is a research
infrastructure providing access to reusable data sources, including
both licensed datasets and open source data. AUDH facilitates Aalto
researchers with access to commercial and unique, high-quality
datasets with register data on energy and electricity markets,
transportation, and telecommunication, as well as important business
and finance related datasets.

AUDH services include data acquisition and contracting support, data
stewardship (data curation, provision, encouragement for use, and
dissemination), data development (such as creating pre-processed
datasets), data-related technical advice, and maintaining a data
catalogue at datahub.aalto.fi. AUDH also acts as center of excellence
for research projects using Statistics Finland data.

AUDH works under the principles of open data: all datasets purchased
with university-wide licenses are disseminated with no further charge
to end users. AUDH also monitors access and usage to the datasets to
comply with contracts written with the data providers and to ensure
FAIR (Findable, Accessible, Interoperable, and Reusable) use of the
data.

*Inspirational quote:* British mathematician Clive Humby said "like
oil, data is valuable... but if unrefined it cannot really be used."
Data is an essential ingredient for empirical research in many fields
of science. However, relevant and refined data is a scarce and
expensive resource and access to high-quality datasets is typically
restricted. In top universities worldwide, availability of relevant
and refined research data for empirical social science research with
dedicated support is a norm. AUHD serves this purpose at Aalto
University.



Other computing and IT solutions
--------------------------------

Please note that the boilerplate texts for the computing solutions listed below are not 
about the Aalto Triton HPC cluster. Please familiarize with the `Aalto cloud computing services <https://www.aalto.fi/en/services/cloud-computing>`__ and `CSC services <https://research.csc.fi/service-catalog>`__ before you include them in your grant application. Please also refer to their terms
of service and pricing if you need to mention these in your  application.


Focus on cloud computing  
~~~~~~~~~~~~~~~~~~~~~~~~

Aalto University has agreements with major public cloud service providers (e.g. Microsoft Azure, Google Cloud Platform and Amazon Web Services), and the platforms have been integrated into the Aalto digital environment in a secure and well-governed manner. The platforms provide scalable, collaborative, and integrated computing tooling with software for rapid iteration on data using for example machine learning or access to ready-made AI API’s for [YOUR TOPIC / IMAGE DETECTION / TEXT ANALYSES].

Aalto has private and secure network connectivity between on-premises environment and the cloud platforms, and access is managed through a central identity management system. Expert staff provide solution consultation and hands-on support for end-user needs.


Focus on CSC 
~~~~~~~~~~~~

Aalto researchers have access to services from the Finnish IT Center for Science (CSC), a government owned center which provides internationally high-quality ICT expert services. These services include multiple use-case specific components – such as containers, databases, HPC and machine-learning utilities - for storing and processing data. The CSC and Aalto services are connected through a high-speed Funet network (Finnish University and Research Network). The CSC coordinates the Finnish Grid and Cloud Infrastructure and has the largest known clusters in Finland.   

CSC’s data center in Kajaani, Finland houses the pan-European pre-exascale supercomputer `LUMI <https://www.lumi-supercomputer.eu/>`__. This is one of the most eco-efficient data centers in the world. LUMI is using 100% hydro powered energy. The waste heat of LUMI will produce 20 percent of the district heat of the area and reduce the city’s annual carbon footprint by 12,400 tons. Further info at https://www.lumi-supercomputer.eu/sustainable-future/.  


Focus on IT solution for remote and hybrid work  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aalto University provides IT solutions for remote and hybrid working. Secure digital workspaces for remote working are created through virtual and remote desktop infra and cloud tools, as well as online support and secure use of one’s own devices and applications. Aalto campus has specially designed (class)rooms with integrated and automated audiovisual technologies in support of hybrid meetings and teaching. 


See also
--------

* `Aalto research services school teams
  <https://www.aalto.fi/en/services/research-and-innovation-services#3-school-teams-helping-researchers>`__
