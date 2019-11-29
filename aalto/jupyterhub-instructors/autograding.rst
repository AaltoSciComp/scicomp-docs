Autograding
===========

Autograding is sometimes seen as the "holy grail" of using Jupyter for
teaching.  But you need an appreciation of the level of the task at
hand and how to do it.

Autograding
-----------

.. warning::

   Running ``nbgrader autograde`` is not secure, because arbitrary
   student code is run with instructor permissions, including access
   to *all instructor files and all other student data*.  We have
   designed our own system to make it secure, but we must run it for
   you.  Contact us to use it.  **If you autograde yourself, you are
   making a choice to risk privacy of all students (probably violating
   Finnish law) and the integrity of your grades.** `This is a
   long-standing design flaw of nbgrader
   <https://github.com/jupyter/nbgrader/issues/483>`__ which we have
   fixed as best we can.

   The secure autograder has to be run manually, by us.  Fetch your
   assignments and contact us in good time.



How deep do you go?
-------------------

1. Normal Jupyter notebooks, no automation.  You might use our
   JupyterHub to distribute assignments and as a way for students to
   avoid running their own software, but that's all.

2. Use nbgrader facilities to generate a student version of
   assignments, but handle grading yourself ("manually using
   nbgrader" or via some other system).

3. Full autograding.

You may think "autograding will save me effort".  It *may*, but it
will make a whole lot of effort in another way: making your assignment
robust to autograding.  As someone once said: plan for one day to
write an assignment, one week to make it autogradeable, then weeks to
make it robust.  It doesn't help that most reference material you can
find is about basic programming, not about advanced data science
projects.

**If you use autograding, you have to test your notebooks with many
students of different levels.  Plan on weeks for this.**



What is autograding?
--------------------

nbgrader is *not* a fancy thing - it just copies files around.
Autograding is *only* running the whole notebook from top to bottom
and looking for errors.  If there are errors, subtract points.  There
is not some major platform running in the background that does things
*actually* automatically.  This is also the primary benefit: a simple
system allows your notebooks to be more portable and reusable, and
match more closely to real work.



Autograding at Aalto
--------------------
1. Design your notebook well
2. Collect your notebooks using the nbgrader interface.  Don't click
   any "autograde" buttons (unless you check the notebook yourself
   first).
3. Send an email to guru asking specifying your course and assignment
   and ask for autograding.  We will run *actually* secure autograding
   on our server soon, and send you a report on what worked or
   didn't.  Everything gets automatically updated in your environment.
4. Proceed as normal, for example...:
5. If autograding didn't work for some people, you can check them,
   modify if needed, and re-run the autograding yourself (since you
   just checked it).


Designing notebooks for autograding
-----------------------------------

(please contribute or comment on these ideas)

Check out the `upstream autograding hints
<https://nbgrader.readthedocs.io/en/stable/user_guide/autograding_resources.html>`__,
which include: hints on writing good test cases, checking if a certain
function has been used, checking how certain functions were called,
grading plots, and more.  But when reading this, not how these
examples are simple code - your cases will probably be more complex.

Understand the whole loop of transferring files from you, to student
versions, to students, and back.  Understand what the loop *is not* as
well.  Understand that there isn't actual *automatic autograding*.

Have an **assignment zero** with no content and worth zero (or one)
points, which students have to submit just to show they know how the
system works (for example, they don't forget to push "submit").  Maybe
it just has some trivial math or programming exercises.  This reduces
the cognitive load when doing the real assignments.

Design your notebook with a mindset of unit testing.  Note that this
isn't the way that notebooks are usually used, though.  Functions and
testable functions are good.  But note that if you put everything in
functions, you lose some of the main benefits of notebooks
(interactivity made possible by having things in the top-level scope)!
Such is life.

Have sufficient tests that are visible to the students, so that they
can tell if their answers are reasonable.  For example,
student-visible tests might check for the shape of arrays, hidden
tests check for the actual values.  This also ensures that they are
approaching it the way you expect.

Similarly, some instructors have found that you must have plenty of
structure so that students only have to fill in well-defined chucks,
with instructor code before and after.  This ensures that students do
"the right thing", but also means that students lose the experience of
the "big picture": loading, preprocessing, and finalization -
important skills for the future.  Instead, they learn to fill in
blanks and no more, no less.  So, in this way autograding is a
trade-off: more grade able, less realistic.

Within your tests, use variable names that won't have a conflict (for
example, a random suffix like ``testval_randomstring36456165`` instead of
``testval``).  This reduces the chance of one of your tests
conflicting/overwriting something that the students have added.

Expect students to do everything wrong, and fail in weird ways.  Your
tests need to be *robust*.

Consider if your assignment is more open-ended, or there is one
specific way to solve it.  If it's more open-ended, consider if you
think you'll be able to make it autogradeable.

nbgrader relies on metadata in order to do the autograding.  In order
for this to work, the cell metadata needs to be intact.  Normally, you
can't even see it for a cell, but it can be affected if: a) cells are
copied and pasted to another notebook file (metadata lost, autograding
fails), or b) cells are split (metadata duplicated, nbgrader halts
then).  You should ask students to copy the whole notebook file around
when needed.
