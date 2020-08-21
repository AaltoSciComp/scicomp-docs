Practical git PRs small teams
=============================

This is the prototype of a mini-course about using git for pull
requests (PRs) within small teams that are mostly decentralized,
perhaps don't have test environments everywhere, and thus standard
review and CI practices don't directly apply.  The audience is
expected to be pretty good with git already, but wondering how PRs
apply to them.

The goal isn't to convince you to use PR-based workflows no matter the
cost, but instead think about how the tech can make your social
processes better.

Status: Alpha-quality, this is more a start of a discussion than a lesson.
Editor: rkdarst



Learning objectives
-------------------
- Why use pull requests?
- How do we adapt our team to use them?
- How does this improve our work?



Why pull requests?
------------------

pull request = **change proposal**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You have some work which should be reviewed before deploying.

- Someone is expected to give useful feedback
- Maybe a quick idea, easier to draft&discuss than talk about it

pull request = **review request**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You've made the change already, or you are already the expert.

- You edited it in deployment, or it is already live
- Or you are the expert, and others don't usually give suggestions
- Still, someone might have some comments to improve your integration
  with other services.

pull request = **change announcement**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- You don't expect others to ever make suggestions
- But you think others should know what you are doing, to distribute
  knowledge
- If no one comments, you might merge this yourself in a few hours or
  days.

Benefits of PRs
~~~~~~~~~~~~~~~
- Multiple sets of eyes

  - Everything should be seen by multiple people
  - Share knowledge about how our services work.
  - Encourages writing a natural-language description of what you
    are doing - clarify purpose to yourself and others

- Suggestion or draft

  - Unsure if good idea, make a draft to get feedback
  - Discuss and iterate via issue.  No pressure to make it perfect
    the first time, so writing is faster

- CI

  - Run automated tests before merging
  - Requires a test environment

- Discussion

  - Structured place for conversation about changes
  - Refer to and automatically close issues



How do you make a pull request
------------------------------
- We don't really need to repeat existing docs
- A PR starts with a **branch** pushed to the remote.  Then, the
  platform registers a **pull request** which means "I want to merge
  this branch into master".  (Yes, a bit misnamed)
- Go to the repo page and you see a button, or a link to make one is
  printed when you push
- `git-pr <https://github.com/NordicHPC/git-pr>`__ makes it easy - fewest
  possible keystrokes, no web browser needed, and I use the commit
  message also as the PR message to save even more time.



Semantics around PRs
--------------------

How do you actually make and handle a PR once it comes in?

Actions
~~~~~~~
Actions you can do from the web (Github):

- **merge**: accept it
- **comment**: add a message
- **approve/request changes**: "review" you can do from "file list"
  view
- **line comments** (*): from diff view, you can select ranges of
  lines and comment there
- **suggestions** (*): from diff, you can select ranges of lines then
  click "suggest" button to make a suggestion.  This can easily be
  applied from web.
- **commit suggestion** (*): from diff view, you can accept the
  suggestion and it makes a commit out of it.
- (*) items can be done in batch from file view, to avoid one mail for
  every comment.
- **draft** pull request can't be merged yet.  There is a Github flag
  for this, or sometimes people prefix with ``WIP:``.

My usual procedure
~~~~~~~~~~~~~~~~~~
- If it's good as-is, just click "merge"

  - If it's a new contributor I usually try to say some positive
    words, but in long-term efficient mode, I don't see a need to.

- Otherwise, comment in more detail.  Line-based views are really
  useful here.  Commenting can be a pure comment, or a "accept" or
  "request changes" (see above)
- If you aren't sure if you are supposed to merge it merge (yet), but
  it looks good, just "approve" it.

  - This cas be a sign to the original author that it looks sane to
    you, they merge when they are ready.

- If someone else suggested changes, I've done the changes, and I
  think there's not much more to discuss, I will just merge it myself
  without another round of review.
- If someone marks my PR "approve" but don't merge it, I will merge
  it myself as soon as I am ready.
- You can both make suggestions and approve (usually with some words
  saying no need to accept hte suggestions if they don't make sense).



How do humans use PRs?
----------------------

Who should merge them?
~~~~~~~~~~~~~~~~~~~~~~
- What happens when the person making the PR is the only one (or main
  one) who can merge it?
- Discuss as part of your team.

When do you merge a pull request?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- How much review do you need to give, if you aren't the expert?
- My proposal:

  - If you are aren't the author, and can evaluate it, merge it ASAP
  - If you aren't an expert, but no one else has merged it after a
    few days, merge it yourself.  Or if you are the original author
    and need it.
  - If no one else has after a week, anyone does it (mainly relevant
    to external contributors).

How do you keep up to date with PRs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`this view lists open Github PRs in an organization <https://github.com/pulls?utf8=%E2%9C%93&q=is%3Aopen+is%3Apr+archived%3Afalse+user%3AAaltoSciComp>`__



How can our team adapt to PRs?
------------------------------

Traditional software project or utility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- PRs make a lot of sense

Deployments: There is no testing environment!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Yes, there should be a test environment, but let's be real: many thing
start off too small to have that.  What do we do about it?

- "If the change has already been made, it's not really a change
  proposal"
- PRs don't work too well here, but when you think about it, it would
  be nice to be able to test before deploying!

  - Maybe this gives us encouragement to use more PRs

- Make a PR anyway even though it's in productive, as a second-eyes
  formality.

All of our projects are independent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Is this good for knowledge transfer?

What advantages would we see with more PRs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Other
-----
These things can make our work a bit soother, and something we can discuss.


Shared git alias
~~~~~~~~~~~~~~~~
- How can we deploy some shared aliases to all hosts we manage?
- This makes some keystrokes faster

Blocking authorless commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- To block authorless commits, run this to set a pre-commit hook::

    echo 'git var GIT_AUTHOR_IDENT | grep root && echo "Can not commit as root!  Use --author" && exit 1 || exit 0' >> .git/hooks/pre-commit ; chmod a+x .git/hooks/pre-commit ```

- Can this be made automatic?
