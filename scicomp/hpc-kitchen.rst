HPC Kitchen metaphor
====================

This is a series of videos which compares HPC and more broadly
scientific computing with cooking or other things in real life.  The
goal is to make approaching computing easier and

* `Playlist on YouTube
  <https://www.youtube.com/playlist?list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB>`__
  (primary location)
* `Videos fetchable with git-annex <https://github.com/coderefinery/video-processing/>`__ (not there yet)
* `Further commentary without YouTube in this yaml file <https://github.com/coderefinery/video-processing/blob/master/hpc-kitchen/editlist.yaml>`__


.. warning::

   **This page is under construction and not all
   descriptions/transcripts are here yet**.  Currently, YouTube has
   the videos and full commentary, but I hope to make that available
   without YouTube.



[intro]: computing vs cooking
-----------------------------

https://www.youtube.com/watch?v=yqGtnA7CUtU&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB

Advanced computing resources like HPC (high-performance computing)
clusters may seem intimidating, but really all the pieces are the same
as a normal computer.  The difference is you have to be able to use
and coordinate all the resources.  This sets you an the path by
introducing you to a metaphor relating computing to cooking.



[data storage]: Understanding how data is stored and moved
----------------------------------------------------------

https://www.youtube.com/watch?v=JAR9xyy5rcE&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB

It's all about data these days, but where does it all go?  How do
understand what we have?  We compare storage in a HPC cluster (or
really, anywhere) to storage of food in a kitchen.  We'll see how the
hierarchy of size vs speed goes and how we access data on different
servers.  This doesn't teach details about storage but prepares you to
learn details in a future course.


[storage-performance]: Understanding the speed of data access and transfer
--------------------------------------------------------------------------

https://www.youtube.com/watch?v=9siGLV8pZ5A&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB

When using supercomputers, data movement can actually be what slows
you down surprisingly often.  A modern GPU can easily pull in data
faster than it can be delivered from storage, if you don't preprocess
it well.  In this video, we go over the basic aspects of storage
performance... with food.



[parallel]: methods to run on multiple processors
-------------------------------------------------

https://www.youtube.com/watch?v=I6fBq9HN3P4&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB

Running programs in parallel: that's what everyone thinks they want to
use a cluster for.  But there are actually different ways this can
work, and you need to be able to distinguish between them, so that you
can run them properly.  This broadly explains what these methods are,
so that you can understand later technical documentation.



[slurm]: the Slurm job scheduler spreads tasks to the cluster
-------------------------------------------------------------

https://www.youtube.com/watch?v=Y73A7lXISxU&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB

We have talked about running stuff in parallel, but how does it get
connected to hardware (processors, memory)?  If we have one cluster
for everyone, how do people share?  That's what this is all about.



[containers/environments]: Moving code around
---------------------------------------------

https://www.youtube.com/watch?v=Ag7wcAwU_Jw&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB

When you go to a different kitchen to cook, everything is different
and it slows you down.  This is a worse problem for computers, which
don't have a brain and thus the recipe has to be exact.  As you get
farther and farther into scientific coding, you'll see how hard of a
difficulty this "installing software and makin g it work" is.
Environments and containers solve this problem.



[how-to-learn]: Don't give up in learning computing
---------------------------------------------------

https://www.youtube.com/watch?v=evJV-02poDc&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB

This is more of a fireside chat, to encourage you not to give up in
learning computing.  It can often feel there is so much to learn and
it's almost impossible.  It can also feel like you can't do it
yourself.  Well, most people don't - all learning is somehow
collaborative.  Take the time to work together to share skills. Take
the time to follow others even in practical computing skills, not just
academic.  And help others.



[data-management]: Data management is as important as data storage
------------------------------------------------------------------

https://www.youtube.com/watch?v=Q5A7n7mu-AI&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB

People may think that getting a big enough storage space for your data
is all you need.  There's far more than that.  It's easy for data (and
kitchens) to become a huge mess without some care.  It's even worse
when you work together.  Unfortunately, it's far too common for people
to be too rushed to organize their stuff well, leading to worse
problems down the line.  Take care of your data and you data will
:strikeout:`take care of` be valuable to you.


[big-vs-small-jobs]: The pitfalls of big jobs
---------------------------------------------

.. role:: strikeout
   :class: strike

https://www.youtube.com/watch?v=Qrql8rGfRVo&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB


I was eating at a restaurant and their group policy said large groups
have a different menu.  Why is that?  Larger groups are a less
efficient use of tables, because of communication and synchronization
overhead.  In the same way, larger jobs on the cluster can be less
efficiency because of overheads.


[reading-docs]: Making sense of information overload
----------------------------------------------------

https://www.youtube.com/watch?v=E9w-MNaXkDw&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB

Have you ever been faced with on overwhelming amount of information
you need to go through before you can start something?  Often times,
it's because there is actually so much information, but there are
strategies for dealing with it.  Let me talk about how I approach
information overload...

.. admonition:: Transcript
   :class: dropdown

   Hello, and welcome to another low-quality HPC Kitchen video. This time
   we're talking about documentation, or generally finding information.

   So, my partner's just gotten back from traveling, and this time
   instead of going through the checklist myself, I printed it out and
   gave it to them and they looked at this and said "this is too long, I
   can't go through it all before traveling and well I mean partly yes
   that's true because this [sheet] has everything that I've ever needed
   to think about before traveling.  For the last 20 years or so, anytime
   I've forgotten something or had to do something before traveling, I
   would add it to the list, and it becomes long.

   So what does this mean? Is longer worse? So in some sense you might
   say so because it's too hard to read. But the point of the checklist
   is to have everything that you might need on it, so you can check
   through it, and once you've read it you make sure you've got
   everything.  And then you can go off and be confident you haven't
   forgotten anything. If it had less on it it would be easier to go
   through, but then you would still have to go think "what am I
   missing?", and then think of that, and maybe forget things. So it's
   actually longer than it would need otherwise. So actually the
   checklist needs to be long in order to be useful.

   So what's the metaphor here? The metaphor is the documentation to use
   all our computing resources. So if you try to print it out it would be
   around this long. Of course I didn't actually print it out just for a
   video. I'm not crazy like that [I'm crazy in other ways, like thinking
   of this topic]. I printed out the first page and then the rest is some
   other paper I've gotten. So this is long. What do we do? So, do we
   want it to be shorter or longer?

   So if you ask me the answer here is organization. So if you look at my
   packing list it's sorted into 13 categories with titles that tell you
   when you may need each of the different things in it. So for example
   right before you walk out the door you look at the "final check"
   section. When you're packing you would look at the "clothes" and maybe
   "information" section. If no one's staying at home and you need to
   turn stuff off and pack stuff up before leaving, there's a "if no one
   is staying section", and so on. So this allows you to sort of have
   something long, but also go through and be able to use it in a way
   that's possible for humans.

   So what are the lessons here? So first off, if something is long,
   don't be scared. So if it's long, first look for the organization. So
   before diving and trying to find an exact page you need, look at the
   table of contents. Look at any quick references. Maybe look at the
   index but that's not quite the organization you need. But get the big
   picture of it before you go and try to narrow down to the place to
   start because the first page you find or a search engine brings you to
   might not be the actual right starting place. Know that not everything
   is needed all the time. So be able to not be intimidated that way and
   look more in depth.  Ask for guidance. So if you ask me, part of the
   reason we've written this much stuff is not because we expect everyone
   to go read it all, but that when people come ask us a question,
   instead of needing to give everyone an individual answer, we can point
   them at the relevant page here. So the documentation is meant to be
   used along with us, not only instead of us [though we hope people can
   give it a try first!]. You can also ask your friends or colleagues,
   whoever that's doing the same kind of work, for information on
   [things] like "where to start?", what they actually use, and so on.
   Finally, realize a lot of the stuff in here may be old and may be out
   of date.  So if you're reading something and it looks a little bit off
   or not quite correct, well then don't just go and give up, but use it
   as a starting point. Maybe come and ask us to update it or ask how it
   may be old. You might need to add in other stuff you're finding online
   with that if you're able to do that, but it's better than removing
   something and next time someone needs to begin they're starting from
   the very beginning once again.

   Finally there's something that I've been thinking about and have made
   here. So I made this little diagram of finding information in the
   past, if you can see. So, in this [hypothesis], in the past we didn't
   have all these computer systems and so on.  So when you need to find
   information, you would have to go to this middle layer of, say, your
   supervisor or the team expert.  You have or a librarian or a research
   engineer, whatever, who can help you go and navigate the things and
   find whatever it is you're looking for.  And that's sort of made all
   the information more manageable.  But then these days we have
   computers, we have the internet, we have search engines, and so on.
   So since you can find everything yourself, it's sort of expected that
   you [*do*] try to find everything yourself.  And if you ask me this is
   not necessarily good.  I mean, it's good that we have access to
   information, but since there's this idea "oh, we don't need the team
   experts, we don't need people like that anymore, just let people find
   it all themselves" leads to information overload and there's just too
   much for people to be able to navigate themselves and actually slow
   things down. So make sure you keep this in mind and use your support
   networks. Don't try to go alone.

   If you're writing information, if you're writing documentation for
   your own equipment, don't go and just do it without paying attention
   to the organization. I'd say make a good table of contents, and try to
   have the table of contents be all on one page so it's easy to navigate
   and see everything in it, instead of having to click through different
   things.  It's like if you make a really deep hierarchy, where to know
   what's at the lower levels, you have to click down through several
   upper levels to see [what is] there.  That makes it a lot harder to
   get the overview and know if you're going to the right places or
   not. I like to try to have one page where it's possible to do a
   [search] with Control-F within a single page and get a summary of
   where some keywords are, and from there it should link you to the
   details. So first have a quick summary there which is useful for quick
   reference (like in our cluster documentation) with links to the
   details. So that way if someone genuinely knows what's going on, they
   can just use the quick reference and copy what they need.  If they're
   new they can get the overview and go to the more detailed pages.

   So with that being said I need to actually clean up this stuff now.
   So thank you for watching and see you perhaps in the next low quality
   HPC kitchen video. Bye.
