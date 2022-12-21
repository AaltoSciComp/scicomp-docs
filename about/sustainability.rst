Sustainability and Environment statement for the Triton HPC cluster
===================================================================

Building a sustainable future is the most important goal of our community and saving energy is one of the most significant actions that we can take to improve sustainability. Fast and large computational resources have high energy requirements, whether it is our Aalto High Performance Computing (HPC) cluster Triton or the workstation at your desk. At Aalto Scientific Computing / Science IT we take these things seriously and we believe that transparency in the energy consumption of our shared computational resources benefits both the users of our cluster as well as the general public.


In this statement, we first summarize the action points that we are implementing to improve Triton HPC energy efficiency and list what you can do as a Triton user to improve the environmental impact of your computations. Then we describe the energy consumption of the computational nodes that are forming our HPC cluster and we  explain the energy saving strategies that are implemented to optimize energy when the nodes are idle and also when the situation of the national energy demand from FinGrid requires everyone to be more careful with energy consumption. 


.. important:: **What Aalto Scientific Computing / Science IT is doing to reduce energy consumption**
  
   Here the main action points on what Aalto Scientific Computing / Science IT is doing to reduce energy consumption for the Triton HPC cluster.
   
   1. **Support for researchers to optimize their calculations**: Our 
      `daily SciComp garage <https://scicomp.aalto.fi/help/garage/>`__ session 
      and `Research Software Engineering service <https://scicomp.aalto.fi/rse/>`__ 
      provide ongoing support for making all computational and data-intensive 
      work as efficient as possible.
   2. **Switching off nodes when the national energy demand is high (coming during the winter)**: 
      Though the Triton HPC cluster will not be affected by Fingrid power cuts, 
      we will reduce the number of active computational resources during periods 
      of high demand according to Fingrid announcements.  Triton is too small to 
      directly participate in `Fingrid's relevant demand response program <https://www.fingrid.fi/sahkomarkkinat/reservit-ja-saatosahko/saatosahko--ja-saatokapasiteettimarkkinat/#saatotarjoukset>`__.   
   3. **Acquiring newer hardware with better energy efficiency (ongoing)**: More 
      energy efficient nodes are being acquired and they are already replacing 
      older hardware.
   4. **Moving to a new datacenter with better power usage effectiveness (2024)**: 
      A new colocation facility with better PUE has been chosen and we have 
      started the work needed to switch to the new location.
        

What Triton users can do to reduce their energy consumption
-----------------------------------------------------------

The most important thing you can do is to make your computations as efficient as practical.  Second, centrally-hosted compute infrastructure is generally much more efficient than standalone computing solutions.  **For any of the matters below, we offer extensive, immediate support** in our `daily garage (every day at 13:00) <https://scicomp.aalto.fi/help/garage/>`__. For significant cases, our Research Software Engineers can directly work with you to improve your workflow with minimal trouble to you.

1. **Make your computations efficient**. Make sure that a) your own code is as efficient as 
   reasonable, and b) it fully uses the reserved HPC resources. 
   
   a. Not all code deserves to be fully optimized, but the more resources you use, the 
      more you should think about optimizing.
   b. When you work with HPC resources, your starting point for looking at the efficiency 
      of your computations is ``seff <JOBID>``. For additional support, come to the daily 
      garage mentioned above.
2. **Save energy by using the centralized infrastructure**: HPC computations are more efficient 
   than your workstation - even before considering your workstation's idle during development. 
   Being a shared resource, you only use what you need to use.
3. **Do you always need a GPU?** While many computational tools are offering faster computing 
   times by using GPUs, one should consider how much is gained by using GPU versus CPU. 
   Roughly the most expensive GPUs need 5 times more energy than a full 40-core CPU node 
   (assuming that the efficiency of the computations is at 100%), so if your computation 
   over GPUs is not at least 5 times faster than running it on CPUs, you should consider 
   avoiding using GPU and accepting a 2-to-4 times slower computational time.



Controlled power cuts: the Triton HPC cluster will not be affected
------------------------------------------------------------------

As communicated by FinGrid `here <https://www.fingrid.fi/en/news/news/2022/several-uncertainties-in-the-adequacy-of-electricity-in-the-coming-winter--finns-should-be-prepared-for-possible-power-outages-caused-by-electricity-shortages/>`__, there are chances of national power cuts during the upcoming winter. The Triton cluster is colocated in a CSC machine room, which also hosts other nationally important infrastructure and is not expected to be affected by the power cuts.  In the case of unexpected outages, there is a backup generator. When it comes to the connectivity between the internet and Triton, Aalto IT Services has ensured that also the physical switches providing remote access are not going to be affected by power cuts.

Even though Triton should not be affected by power cuts, we will react to the national electricity supply and reduce the power consumed during these periods.


Energy consumption of Triton
----------------------------

For the first half of 2022, Triton's average power was 214 kW (long-run average).  This includes all compute nodes, GPUs, data storage, network, and other administrative servers.  It does not include cooling.

* A typical CPU node consumes around 450W when active and 60W when idling (Dell PowerEdge C6420, 40 CPU cores).
* The newest GPU nodes use 2200W at peak use and average 1200W (Dell PowerEdge XE8545, 48 CPU cores and 4 NVIDIA A100 cards).


In general, Triton has a relatively high usage factor (on average above 90% in the year 2022), so there is minimal waste from idling. While our current machine room does not recover waste heat for district heating, our new machine room will be able to do so.  Furthermore, we are constantly updating our hardware with new nodes with more efficient energy consumption. You can check `further details about Triton’s hardware at this page <https://scicomp.aalto.fi/triton/overview/>`__. 

For comparison, the minimum power to participate in Fingrid's demand-response frequency restoration reserve market is 1MW.


Energy efficiency of the CSC colocation
---------------------------------------

The energy efficiency of colocation facilities is described by the ratio Power Usage Effectiveness (PUE) determined by dividing the total amount of power entering a data center by the power used to run the IT equipment within it. In an ideal world PUE should be as close as 1 as possible, the most efficient datacenters in the world are reporting a PUE of 1.02 (`reference <https://www.sunbirddcim.com/blog/whats-best-pue-ratio-data-centers>`__) and the average datacenter has a PUE of 1.57 (`average from a survey in 2021 <https://www.statista.com/statistics/1229367/data-center-average-annual-pue-worldwide/>`__).

Triton is physically located at CSC colocation facilities with other servers supporting all researchers in Finland (e.g. the FUNET network). Our current colocation has a PUE of 1.3. This is not the state of the art, although it is better than the average datacenter around the world. Energy efficiency will be a very important criteria in the upcoming move to a new facility. The current tentative plan is to move Triton’s hardware in a new colocation during the year 2023 and be ready for 2024.


Impact of Triton hardware purchases
-----------------------------------

Unlike many clusters, Triton does not build a new cluster every few years.  Triton is continually upgraded, and old hardware is only discarded after it is actually obsolete (which usually comes due to excessive energy consumption relative to newer hardware).  This allows us to adjust the e-waste/power consumption tradeoff dynamically, depending on the circumstances.  We try to minimize the entire lifecycle impact of our cluster.  Yes, Triton is a metaphorical Ship of Theseus.
