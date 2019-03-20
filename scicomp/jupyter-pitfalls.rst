Pitfalls of Jupyter Notebooks
=============================

Jupyter Notebooks are a great tool for research, data science type
things, and teaching.  But they are not perfect - they support
exploration, but not other parts of the coding phase such as
modularity and scaling.  This page lists some common limitations and
pitfalls and what you can do to avoid them.

*Do* use notebooks if you like, but *do* keep in mind their
limitations, how to avoid them, and you can get the best of both
worlds.

None of the limitations on this page are specific to notebooks - in
fact we've seen most of them in scripts long before notebooks were
popular.



Modularity
----------

We all agree that code modularity is important - but Jupyter
encourages you to put most code directly into cells so that you can
best use interactive tools.  But to make code the most modular, you
want lots of functions, classes, etc.  Put another way, the most
modular code has nothing except function/class/variable/import
definitions touching the left margin - but in Jupyter, almost
everything touches the left margin.

Solution: be aware of the transition to modules - do it when you need
to.  See the next point.  Try to plan so it's not too painful to do
this.



Transitioning to modules
------------------------

You may start coding in notebooks, but once your project gets larger,
you will need to start using your code more places.  Do you copy and
paste?  At this point, you will want to split your core code into
regular Python modules, import them into your notebooks, and use the
notebooks as an interface to them - so that modules are somewhat
standard working code and notebooks are the exploration and
interactive layer.  But when does that happen?  It is difficult to
make that transition unless you really try hard, because it's easier
to just keep on going.

Solution: remember that you will probably need to form a proper module
eventually.  Plan for it and do it quickly once you need to.  You can
set modules to automatically reload with ``%load_ext autoreload``,
``%autoreload 1``, and then ``%aimport module_name``.  Then your edits
to the Python source code are immediately used without restarting and
your work is not slowed down much.  See more at the `IPython docs on
autoreload
<https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html>`__
(note: this is Python kernel specific).



Difficulty to test
------------------

For the same reasons modularity outlined above, it's hard to test
notebooks using the traditional unit testing means (if you can't
import notebooks into other modules, you can't do much).  Testing is
important to ensure the accuracy of code.

Solution: Include mini-tests / assertions liberally.  Split to modules
when it is necessary - maybe you only create a proper testing system
once you transition to modules.



Version control
---------------

Notebooks can't be version controlled well.  Of course, they *can* be
version controlled (and should be), and tools like `nbdime
<https://github.com/jupyter/nbdime>`__ (notebook diff and merge) work
well for what they try to do.

Solution: don't let this stop you.  Do version control your notebooks
(and don't forget to commit often!), and use nbdime, Jupyter git
integration, and so on well.



Hidden state is opposed to reproducibility
------------------------------------------

This is a bit of an obscure one: people always say that notebooks are
good for reproducibility.  But they also allow you to run cells in
different orders, delete cells after it has run, change code after you
run it, and so on.  And the whole point of notebooks is to be able to
re-edit and re-run.  So it's very easy to get into a state where you
have variables defined which aren't in your current code and you don't
remember how you got them.  Since old output is saved, you might not
realize this until it's too late.

Solution: Use "Restart and run all" liberally.  Unless you do, you
can't be sure that your code will make your output.  So do that when
needed.  (But wait... part of the point of notebooks is that you can
keep data in memory because it might take a while to calculate... so
"Restart and run all" defeats the purpose of that, so... balance it
out.)



Notebooks aren't named by default
---------------------------------

This is really small, but notebooks aren't named by default.  If you
don't name them well, you will end up with a big mess.  Also somewhat
related, notebooks tend to purpose drift: they start for one thing
then end up with a lot of random stuff in them.  How do you find what
you need?  Obviously this isn't specific to notebooks, but the
interactive nature and modularity-second makes the problem more
visible.

Solution: Remember to name notebooks well.  Keep mind of when they
start to feature drift too much, and take some time to sort your code
logically once that happens.



Difficult to integrate into other execution systems
---------------------------------------------------

A notebook is designed for interactive use - you *can* run them all
with ``nbconvert --to notebook --execute input.ipynb --output
executed.ipynb``.  But there's no good command line interface to pass
arguments, input and output, and so on.  So you write one notebook,
but can't easily turn it into a flexible script to be used many
times.

Solution: Probably a lot of the solution is the same as modularizing.
Use notebooks to explore, scripts to run in bulk.  Run notebooks in
batch using nbconvert if you think you can manage it well enough and
not have it become a mess.  I've had an idea that environment
variables could be used to pass parameters into notebooks for batch
execution, but could that be trying too hard?


Summary
-------

..
    todo: this was copied from elsewhere and can be merged into the
    above.

The notebooks can be great for starting projects and interactive
exploration.  However, as a project gets more advanced, you will
eventually find that the linear nature of notebooks is a limitation
because code can not really be reused.  It is possible to define
functions/classes within the notebook, but you lose the power of
inspection (they are just seen as single blocks) and can't share code
across notebooks (and copy and paste is bad).  This doesn't mean to
not use notebooks: but do keep this in mind, and once your methods are
mature enough (you are using the same code in multiple places), try to
move the core functions and classes out into a separate library, and
import this into the day-to-day exploration notebooks.  For more about
problems with notebooks and how to avoid them, see this fun talk `"I
don't like notebooks" by Joel Grus
<https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit>`__.
These problems are *not* specific to notebooks, and will make your
science better.

In a cluster environment, notebooks are inefficient for big
calculations because you must reserve your resources in advance, but
most of the time the notebooks are not using all their resources.
Instead, use notebooks for exploration and light calculation.  When
you need to scale up and run on the cluster, separate the calculation
from the exploration.  Best is to create actual programs
(start, run, end, non-interactive) and :doc:`submit those to the queue
</triton/tut/serial>`.  Use notebooks to explore and process the
output.  A general rule of thumb is "if you would be upset that your
notebook restarted, it's time to split out the calculation".

Notebooks are hard to :doc:`version control </scicomp/git>`, so you
should look at the `Jupyter diff and merge tools
<https://github.com/jupyter/nbdime>`__.  Just because notebooks is
interactive doesn't mean version control is any less important!  The
"split core functions into a library" is also related: that library
should be in version control at least.

Don't open the same notebook more than once at the same time - you
will get conflicts.



References
----------

* This funny talk `"I don't like notebooks" by Joel Grus
  <https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI>`__
  provided a starting point of this list.
