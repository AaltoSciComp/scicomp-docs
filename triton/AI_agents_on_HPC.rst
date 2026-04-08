AI Agents on HPC
================

AI agents like `Claude Code <https://code.claude.com/docs/en/overview>`__ or
`OpenAI Codex <https://openai.com/codex/>`__ (via Command Line Interface or
`VSCode plugin <https://marketplace.visualstudio.com/search?term=ai%20code&target=VSCode&category=All%20categories&sortBy=Installs>`__)
are getting popular and some of our Triton users have started using them for coding assistance
or Slurm monitoring and job management. We want to encourage researchers to use these tools,
and to learn together how to use them well.

AI agents are powerful and can introduce security risks or disruptions for you and for other
users of the cluster. We want to develop good practices for working with AI agents on Triton,
and more broadly on any computer you use.

We ask for your cooperation and we would like you to:

#. Tell us which agent you use and how you use it at the `daily zoom garage
   <https://scicomp.aalto.fi/help/garage/>`__ or in the `Zulip chat
   <https://scicomp.zulip.cs.aalto.fi/>`__.
#. Be aware of what could go wrong, we summarised some of the risks in the table below.
#. Save your work frequently. Triton admins will have to kill agent processes (or other
   processes) if they affect system stability.
#. If you (or we) suspect that something went wrong with your agent, we are happy to check
   the logs with you.
#. Finally, keep in mind that responsibility always lies with the person operating the AI
   agent; if something goes wrong, the AI itself cannot be held accountable.

We will get in touch with those of you running AI agents.


Common problems and how to avoid them
--------------------------------------

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
   * - Code & data confidentiality
     - Code, file contents, and error messages are sent to an external LLM provider's servers.
       Sensitive data, unpublished results, personal data (GDPR), or secrets (passwords, API
       keys, tokens) may be exposed.
     - Never process sensitive or confidential data through an agent: instead, work with
       synthetic data. Keep secrets out of files/folders the agent can access. Running the
       agent inside a container can limit its potential *blast radius*.
   * - LLM provider data retention
     - The LLM provider may retain your queries according to their own privacy policy
       (`up to 5 years for Claude <https://code.claude.com/docs/en/data-usage>`__,
       `30 days for OpenAI <https://developers.openai.com/api/docs/guides/your-data>`__).
     - Read and understand the privacy policy of the AI tool you are using before your first
       session. Not sure? Get in touch with us.
   * - Triton cluster stability
     - Agents may submit batch jobs, run shell commands, spawn runaway loops, or consume
       excessive CPU/memory/I/O, affecting all users on shared infrastructure (e.g. login
       node). Agents can also aggressively monitor running jobs via squeue/sacct queries,
       which put heavy load on the Slurm controller and cause instabilities for all users.
     - Monitor your agent sessions actively, ideally don't run more than one agent. Terminate
       processes that behave unexpectedly. If agents become disruptive, we might need to set
       up some automations to moderate their activities so that other users are not affected.
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
       requires some extra set-up and is currently being tested.
   * - Ethical and responsible AI
     - Using generative AI systems built on
       `data scraped without explicit consent from creators or copyright holders
       <https://legalblogs.wolterskluwer.com/copyright-blog/the-bartz-v-anthropic-settlement-understanding-americas-largest-copyright-settlement/>`__
       and `significantly affecting the environment <https://arxiv.org/abs/2603.20897>`__
       might not align with your ethical principles.
     - Consider using AI tools which were built responsibly. Unfortunately this is easier said
       than done: let's work on this together!


Recommendations for specific agents
-------------------------------------

We will update our recommendations here based on users' feedback.
