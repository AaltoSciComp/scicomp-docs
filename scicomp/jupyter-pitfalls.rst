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

Solutions:

- Slowly work towards functions/classes/etc where appropriate, but
  realize it's not as easy to inspect their insides as non-function
  code.
- Be aware of the transition to modules - do it when you need to.  See
  the next point.
- Try to plan so it's not too painful to make the conversion when the
  time comes.



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

Solutions:

- Remember that you will probably need to form a proper module
  eventually.  Plan for it and do it quickly once you need to.
- Make sure you notebooks aren't disconnected from your own Python
  code in modules/packages.
- You can set modules to automatically reload with ``%load_ext
  autoreload``, ``%autoreload 1``, and then ``%aimport module_name``.
  Then your edits to the Python source code are immediately used
  without restarting and your work is not slowed down much.  See more
  at the `IPython docs on autoreload
  <https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html>`__
  (note: this is Python kernel specific).
- `importnb <https://pypi.org/project/importnb/>`__ to import
  notebooks as modules - but maybe if you get to this, you need to
  rethink your goal.



Difficulty to test
------------------

For the same reasons modularity outlined above, it's hard to test
notebooks using the traditional unit testing means (if you can't
import notebooks into other modules, you can't do much).  Testing is
important to ensure the accuracy of code.

Solution: Include mini-tests / assertions liberally.  Split to modules
when it is necessary - maybe you only create a proper testing system
once you transition to modules.

Solutions:

- Various extensions to pytest that work with notebooks

  - `nbval <https://github.com/computationalmodelling/nbval>`__,
    `pytest-notebook
    <https://pytest-notebook.readthedocs.io/en/latest/>`__: run
    notebook, check actual outputs match outputs in ipynb.
  - `pytest-ipynb <https://github.com/zonca/pytest-ipynb>`__: cells
    are unit tests
  - This list isn't complete or a recommendation

- But just like with modularity above, a notebook designed to be
  easily testable isn't designed for interactive work.
- Transition to modules instead of testing in the notebook.



Version control
---------------

Notebooks can't be version controlled well, since they are JSON
format.  Of course, they *can* be version controlled (and should be),
and there are a variety of good solutions so this shouldn't stop you.

Solutions:

- Don't let this stop you.  Do version control your notebooks (and
  don't forget to commit often!), even if you don't use any of the
  other strategies.
- `nbdime <https://github.com/jupyter/nbdime>`__ - diffing and
  merging, VCS integration
- Jupyter `lab <https://github.com/jupyterlab/jupyterlab-git>`__ /
  notebook git integration work well.
- Notebooks in other plain-text formats: Rmarkdown, `Jupytext
  <https://jupytext.readthedocs.io/>`__ (pair notebooks with plain
  text versions).
- Remember, blobs in version control is still better than nothing.



Hidden state is opposed to reproducibility
------------------------------------------

This is a bit of an obscure one: people always say that notebooks are
good for reproducibility.  But they also allow you to *run cells in
different orders, delete cells after it has run, change code after you
run it*, and so on.  And this is the whole point of notebooks.  So
it's very easy to get into a state where you have variables defined
which aren't in your current code and you don't remember how you got
them.  Since old output is saved, you might not realize this until
it's too late.

Solutions:

- Use "Restart and run all" liberally.  Unless you do, you can't be
  sure that your code will reproduce your output.
- But wait... part of the point of notebooks is that you can keep data
  in memory instead of recalculating each time you run.  "Restart and
  run all" defeats the purpose of that, so... balance it out.)
- Design for modularity and clean interfaces, even within a notebook.
  Don't make a mess.



Notebooks aren't named by default
---------------------------------

This is really small, but notebooks aren't named by default.  If you
don't name them well, you will end up with a big mess.  Also somewhat
related, notebooks tend to purpose drift: they start for one thing
then end up with a lot of random stuff in them.  How do you find what
you need?  Obviously this isn't specific to notebooks, but the
interactive nature and modularity-second makes the problem more
visible.

Solutions:

- Remember to name notebooks wells, immediately after making them.
- Keep mind of when they start to feature drift too much, or have too
  many unrelated things in them.  Take some time to sort your code
  logically once that happens.



Difficult to integrate into other execution systems
---------------------------------------------------

A notebook is designed for interactive use - you *can* run them from
the command line with various commands.  But there's no good command
line interface to pass arguments, input and output, and so on.  So you
write one notebook, but can't easily turn it into a flexible script to
be used many times.

Solutions:

- Modularize your code and notebooks.  Use notebooks to explore,
  scripts to run in bulk.

- Create command line interfaces to your libraries, use that instead
  of notebooks.

- There are many different tools to parameterize and execute
  notebooks, if you think you can keep stuff organized:

  - `nbconvert <https://nbconvert.readthedocs.io/>`__

  - `papermill <https://github.com/nteract/papermill>`__

  - `nbscript <https://github.com/NordicHPC/nbscript>`__
    (:doc:`self-advertisement </scicomp/nbscript>`)

  - ... and plenty more



Jupyter disconnected from other computing
-----------------------------------------

This is also a philosophical one: some Jupyter systems are designed to
insulate the user from the complexities of the operating system.  When
someone needs to go beyond Jupyter to other forms of computing (such
as ssh on cluster), are they prepared?

Solutions:

- This is more of a mindset than anything else.

- System designers should not go through extra efforts to hide the
  underlying operating system, nor separate the Jupyter systems from
  other systems.

- Include non-Jupyter training, some intro to the shell, etc. in the
  Jupyter user training.



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
