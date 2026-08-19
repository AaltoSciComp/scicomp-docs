AI Agents on HPC
================

AI agents like `Claude Code <https://code.claude.com/docs/en/overview>`__ or
`OpenAI Codex <https://openai.com/codex/>`__ (via Command Line Interface or
`VSCode plugin <https://marketplace.visualstudio.com/search?term=ai%20code&target=VSCode&category=All%20categories&sortBy=Installs>`__)
are getting popular and some of our Triton users have started using them for coding assistance
or Slurm monitoring and job management. We want to encourage researchers to use these tools
responsibly, and to learn together how to use them well.

AI agents are powerful and can introduce security risks or disruptions for you and for other
users of the cluster. We want to develop good practices for working with AI agents on Triton,
and more broadly on any computer you use.


How do I run a coding agent? Am I running an agent on Triton?
--------------------------------------------------------------

It depends on your workflow. Here some of the most common setups:

#. **VS Code (or other editor) with coding agent running only on your computer:** You run
   VS Code on your computer with
   `coding agent extensions <https://marketplace.visualstudio.com/search?term=ai%20code&target=VSCode&category=All%20categories&sortBy=Relevance>`__
   (GitHub Copilot, Cline, Claude Code, etc) without any remote SSH to Triton. Queries are
   sent to an external Large Language Model (LLM) provider and you should have an account
   there (info on accounts at the bottom of this page). Nothing runs on Triton, so this is
   fine from a cluster perspective, but you can still face many of the risks listed in the
   table below.

#. **CLI agent only on your computer:** This is similar to the scenario above, but this time
   you use a command line interface tool like Claude Code or OpenAI Codex. You are running
   the agent locally on your computer and your code and data are sent to the remote LLM
   provider. Again, nothing runs on Triton.

#. **VSCode with remote SSH to Triton:** You open VS Code on your computer, but this time you
   connect to ``triton.aalto.fi`` via remote SSH. In this case VS Code server runs on Triton's
   login node and any coding agent extension also runs there.

#. **CLI agents over SSH on Triton:** You SSH into ``code.triton.aalto.fi`` and from the terminal
   start a command line agent such as Claude Code or OpenAI Codex. The agent runs on the
   login node and sends your code and other data it can access to the remote LLM provider.

*If you are not sure about these workflows, just come and chat with us at the daily zoom
garage.*

**NEW: If you are conneting to triton.aalto.fi with your coding tool (VScode, Claude code, 
Codex, PyCharm, ...) please use the new login server** ``code.triton.aalto.fi`` instead of ``triton.aalto.fi``.



I am running a coding agent, what should I do?
-----------------------------------------------

If you are running a coding agent, we ask for your cooperation and we would like you to:

#. Tell us which agent you use and how you use it at the `daily zoom garage
   <https://scicomp.aalto.fi/help/garage/>`__ or in the `Zulip chat
   <https://scicomp.zulip.cs.aalto.fi/>`__.
#. Be aware of what could go wrong. We summarised some of the risks in the table below.
#. Save your work frequently. Triton admins will have to kill agent processes (or other
   processes) if they affect system stability.
#. If you (or we) suspect that something went wrong with your agent, we are happy to check
   the logs with you.
#. Finally, keep in mind that responsibility always lies with the person operating the AI
   agent; if something goes wrong, the AI itself cannot be held accountable.

We will get in touch with those of you running AI agents.


Common problems with coding agents and how to avoid them
---------------------------------------------------------

The table below summarises some of the things that could go wrong and how you could mitigate
risks.

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Category
     - What could go wrong?
     - What should I do?
   * - Software & supply chain
     - Agents may install packages automatically from public registries (PyPI, npm, CRAN,
       Conda-Forge, etc.). Some may be malicious, compromised, or part of
       `typosquatting <https://en.wikipedia.org/wiki/Typosquatting>`__ /dependency confusion
       attacks.
     - Review what gets installed during and after sessions, or, even better, take care of
       installations *before* running the agent. For your own computers: never run agents with
       elevated privileges. In general: avoid using the most recent version of packages. Read
       more at the `OWASP website <https://owasp.org/www-community/Component_Analysis>`__.
   * - Prompt injection
     - Agents read files, documentation, and web pages as part of their work. A malicious
       package README, a GitHub comment, or webpage may contain hidden instructions that
       hijack the agent's behaviour — for example, causing it to execute unexpected commands.
       This is called prompt injection and is difficult to detect.
     - Be cautious about which URLs or repositories you let the agent browse. Some agents
       also use "skills" — installable extensions written as markdown files — which can
       contain malicious instructions. Review what the agent does after it reads external
       content and check which skills your agent is using. Prefer agents that ask for
       confirmation before taking actions following a web or file lookup. See also:
       `an extensive review article on prompt injection attacks
       <https://arxiv.org/html/2601.17548v1>`__.
   * - Code & data confidentiality
     - Code, file contents, and error messages are sent to an external LLM provider's servers.
       Sensitive data, unpublished results, personal data (GDPR), or secrets (passwords, API
       keys, tokens) may be exposed. You might also expose code to other users of the shared
       HPC node (e.g. login node).
     - Never process sensitive or confidential data through an agent: instead, work with
       synthetic data. Keep secrets out of files/folders the agent can access. Running the
       agent inside a container can limit its potential *blast radius*. CLI agents like Claude
       code also typically run ``python -c <long python code here>`` which are visible to other
       users of the cluster. 
   * - LLM provider data retention
     - The LLM provider may retain your queries according to their own privacy policy
       (`up to 5 years for Claude <https://code.claude.com/docs/en/data-usage>`__,
       `30 days for OpenAI <https://developers.openai.com/api/docs/guides/your-data>`__).
     - Read and understand the privacy policy of the AI tool you are using before your first
       session. Not sure? Get in touch with us.
   * - Triton cluster stability
     - Agents may submit batch jobs, run shell commands, spawn runaway loops, or consume
       excessive CPU/memory/I/O, affecting all users on shared infrastructure (e.g. login
       node). Patterns that are fine on a laptop can cause serious problems on a cluster:
       agents aggressively monitoring running jobs via squeue/sacct queries, submitting tens
       of thousands of small jobs instead of combining them, or aggressive I/O patterns can
       all cause instabilities for other users. Agents don't know Triton's specific setup:
       always verify Slurm job parameters against the Triton documentation before submitting.
     - Monitor your agent sessions actively; ideally don't run more than one agent. Terminate
       processes that behave unexpectedly. If agents become disruptive, we may introduce
       automations to moderate their activities so that other users are not affected.
   * - Login node availability
     - If the login node becomes unstable, Triton admins will stop active agentic processes
       without prior notice before attempting a reboot. In-progress work may be lost.
     - Save your work frequently. Do not rely on long-running unsupervised agent sessions on
       the Triton login node.
   * - Autonomous file actions
     - Agents can modify, overwrite, or delete files without asking for confirmation at each
       step.
     - Use version control (git) or take backups before and during agent sessions (remember:
       scratch is not backed up). Don't delegate git commands to your agent; instead ask which
       commands to run and run them in a separate terminal. Optimally the agent does not have
       access to your git credentials (keys or password).
   * - Agent mistakes & hallucinations
     - Agents may misinterpret instructions or produce plausible-looking but incorrect commands
       or code resulting in invalid research findings.
     - Review all agent-generated changes before using them in research or production
       workflows. Publishing results that are fabricated or falsified is academic misconduct
       and can result in retraction.
   * - Copyright & plagiarism
     - AI-generated code may incorporate patterns from copyrighted training data.
       `Finnish <https://tenk.fi/sites/default/files/2026-02/Use%20of%20Artificial%20Intelligence%20in%20Research_UNOFFICIAL%20TRANSLATION_DRAFT_0.pdf>`__
       and `European research integrity guidelines <https://allea.org/code-of-conduct/>`__
       require disclosure of AI assistance in publications and grant applications.
     - Check licensing of generated code. Disclose AI assistance as required by the
       `ALLEA European Code of Conduct for Research Integrity
       <https://allea.org/code-of-conduct/>`__.
   * - Third-party terms of service and support
     - Each AI coding tool (e.g., GitHub Copilot, Cursor, Cline, Continue.dev) has its own
       terms of service. Triton admins or IT services do not provide support for these tools.
     - Read and comply with the terms of service of each tool you use. Tool-specific issues
       should be discussed with the provider of the tool.
   * - Aalto approved tools
     - There are no officially approved ways to use AI agents on Aalto systems.
     - With some agents (e.g. Codex) it is possible to use endpoints hosted in the EU Azure
       datacentre similarly to what is done with `ai.aalto.fi <http://ai.aalto.fi>`__. This
       requires some extra set-up and is currently being tested. In general these tools can
       never be 100% secure, so it is best to work only with public data, or fake synthetic
       data.
   * - Ethical and responsible AI
     - Using generative AI systems built on
       `data scraped without explicit consent from creators or copyright holders
       <https://legalblogs.wolterskluwer.com/copyright-blog/the-bartz-v-anthropic-settlement-understanding-americas-largest-copyright-settlement/>`__
       and `significantly affecting the environment <https://arxiv.org/abs/2603.20897>`__
       might not align with your ethical principles.
     - Consider using AI tools which were built responsibly. Unfortunately this is easier said
       than done: let's work on this together!


Accounts to remote AI systems
------------------------------

The coding agent itself is just a script that packages your code, questions, plans, and data
into a clever "prompt" that is sent to a remote AI system — very similar to chatting with
ChatGPT or `duck.ai <http://duck.ai>`__, but this time you do not control what is sent to the
remote large language model. While some chatbots are free and require no accounts (e.g.
`duck.ai <http://duck.ai>`__), coding agents want you to register and in most cases you need
to buy the service from the provider (e.g. OpenAI for Codex or Anthropic for Claude Code).
GitHub Copilot allows some free credits for GitHub accounts that are
`registered as a teacher <https://docs.github.com/en/education/about-github-education/github-education-for-teachers/apply-to-github-education-as-a-teacher>`__
(in practice this is suitable for any Aalto researcher or academic staff, since they are all
teaching assistants or supervisors/mentors of other students or researchers). There are some
ways to use open-source large language models and we will document them later.

Practical guidance for configuring and using AI agents
-------------------------------------------------------


Large language model (LLM) agents are developing rapidly, so the practices in
this section are not necessarily the best or final approaches.
We will update our recommendations here based on users' feedback.
These are techniques we have found useful and good starting points.  We welcome
suggestions and reviews.  An agent's configuration does not make it safe by
itself: remain present, review proposed actions, and follow the precautions
above.

Restricting file-system access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Agents and their commands usually inherit your file permissions.  Selecting a
project directory does not necessarily prevent access to your home directory,
which may contain API keys, SSH configuration, and other secrets.

Use the harness's sandbox settings to restrict access to the workspace, prefer
read-only access where possible, and require approval for commands and file
changes.  Avoid ``full access`` and test what is actually blocked.  For stronger
isolation, use an operating-system sandbox, container, or virtual machine that
exposes only the required project directories.

The `vscode-apptainer <https://github.com/AaltoRSE/vscode-apptainer>`__
repository provides scripts for running VS Code inside an Apptainer container
with restricted access.  Isolation does not make sensitive data safe to send
to a model provider, so the data-handling requirements above still apply.  Ask
at the :ref:`daily garage help session <garage>` if you need help choosing an
isolation method for Triton.


Configuring AI agents to use a custom model API (often openAI-compatible API)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some agent harnesses can use a custom or OpenAI-compatible API instead of the
vendor's default service.  The exact setting names differ between agents, but
the setup usually requires:

* the API provider or protocol (often ``openai`` or ``openai-compatible``);
* the API base URL;
* a model or Azure deployment name; and
* an API key or other authentication token.

To configure one:

#. Request access to the service and obtain its current base URL, available
   model names, and authentication instructions.
#. Follow your agent's documentation for a custom provider or base URL.
   Azure OpenAI may additionally require a deployment name and API version.
#. Put credentials in environment variables or the agent's secret store, not
   in a repository, rule, skill, prompt, shell history, or command-line
   argument.  Restrict permissions on any file containing a credential.
#. Start with a small test.

The `ASC LLM examples <https://github.com/AaltoSciComp/llm-examples>`__
repository contains examples for connecting software to the `Aalto Azure
OpenAI API <https://www.aalto.fi/en/services/aalto-ai-apis>`__ and the `Aalto
LLM Gateway <https://github.com/AaltoSciComp/llm-gateway>`__.

If you are uncertain which service fits your use case or have problems
configuring the agent, contact the :ref:`daily garage help session <garage>`.

Recommended global rules and project rules for Triton projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Agent harnesses use different names and locations for persistent instructions.
Global rules should apply to every session on Triton, while project rules
should describe the conventions and resources of one repository.  Keep both
short enough that the agent can follow them reliably.

Suggested global rules:

* Use login nodes only for light interactive work.  Run computations through
  Slurm; see the :doc:`cluster shell guidance </triton/tut/cluster-shell>` and
  :doc:`Slurm tutorial </triton/tut/slurm>` before proposing resource requests.
* Ask before submitting or cancelling jobs, installing software, deleting
  files, changing permissions, or performing remote Git operations.
* Monitor jobs with bounded checks at least 15 seconds apart and stop watchers
  when they are no longer needed.  Prefer Triton's documented commands and use
  :doc:`job monitoring </triton/tut/monitoring>` to assess efficiency after a
  job finishes.
* Do not submit large numbers of small jobs individually.  Group short tasks
  or use :doc:`Slurm arrays </triton/tut/array>`.
* Never read, print, move, or commit credentials.
* Stop and ask the user when Triton documentation, project instructions, and
  the requested action disagree.

Suggested project rules:

* Read the project's documentation, existing job scripts, module setup, and
  environment files before creating or changing them.
* Reuse documented modules and environments.  Search with ``module spider``
  before installing software; see :doc:`software modules
  </triton/tut/modules>`.
* Use the storage location intended by the project.  Keep computation data out
  of ``$HOME`` and remember that ``$WRKDIR`` and scratch are not backed up; see
  :doc:`Triton storage </triton/tut/storage>`.
* Avoid producing large numbers of small files or unnecessarily frequent logs
  and checkpoints; see :doc:`small-file guidance </triton/usage/smallfiles>`.
* Make small, reviewable changes.  Test with a small input before scaling up,
  preserve important outputs, and report commands, job IDs, and generated
  files to the user.

Recommended skills for Triton projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skills are reusable instruction bundles, and some can also include scripts or
references.  Useful skills for Triton projects include:

* **Triton documentation lookup:** Find the relevant Triton page, extract the
  site-specific instructions, and cite them before proposing a command.
* **Slurm job preparation:** Select time, memory, CPUs, GPUs, and temporary
  storage; choose arrays or grouped jobs for many short tasks; validate an
  existing job script; and request approval before submission.
* **Job monitoring and diagnosis:** Check queue state without aggressive
  polling, inspect logs, use ``seff`` or ``slurm history`` after completion,
  and suggest resource adjustments based on evidence.
* **Software environment setup:** Discover installed software with
  ``module spider``, reproduce the project's module stack.

Treat every skill as executable third-party content: read all instructions and
scripts before adding it.  Do not use a skill that asks for credentials,
weakens confirmation settings, or sends project data elsewhere.

Example skills for Triton projects can be found in the `ASC LLM examples <https://github.com/AaltoSciComp/llm-examples>`__ repository.

