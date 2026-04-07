AI Agents on HPC
================

AI agents like `Claude Code <https://code.claude.com/docs/en/overview>`__ or OpenAI Codex are
getting popular and some of our Triton users have started using them for coding assistance or
Slurm monitoring and interactions. AI agents however can introduce security risks for both the
account that is using the agent and the rest of the cluster. They can also cause stability
issues if their requests put unexpected stress on the cluster management. Right now, our
attitude is to not prohibit such systems; instead we want to agree on good practices with
those users who are planning to run those systems on Triton, and more broadly on any computer
that they use.

Because of this, we ask you for your cooperation and we would like you to:

#. Tell us which agent you use and how you use it at the `daily zoom garage
   <https://scicomp.aalto.fi/help/garage/>`__ or in the `Zulip chat
   <https://scicomp.zulip.cs.aalto.fi/>`__.
#. Give us the permission to check the logs written by the agent in your home folder. Triton
   admins and Aalto IT security staff may inspect shell history, process logs, network logs,
   and any other log related to your agent sessions.
#. Be aware of what could go wrong — we wrote a list in the table below.
#. Accountability will always be on the person who runs the AI agent; we can never blame the
   AI if something goes wrong.

For now we are happy to just monitor things and contact directly those of you using AI agents
on Triton. If agents become disruptive, we might need to set up some automations to moderate
their activities.

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
       node).
     - Monitor your sessions actively; ideally don't run more than one agent. Terminate
       processes that behave unexpectedly.
   * - Login node availability
     - If the login node becomes unstable, Triton admins will stop active agentic processes
       without prior notice before attempting a reboot. In-progress work may be lost.
     - Save your work frequently. Do not rely on long-running unsupervised agent sessions on
       the Triton login node.
   * - Autonomous file actions
     - Agents can modify, overwrite, or delete files without asking for confirmation at each
       step.
     - Use version control (git) or take backups before and during agent sessions (remember:
       scratch is not backed up).
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
   * - Ethical and responsible AI
     - Using generative AI systems built on
       `mostly stolen data <https://legalblogs.wolterskluwer.com/copyright-blog/the-bartz-v-anthropic-settlement-understanding-americas-largest-copyright-settlement/>`__
       and `significantly affecting the environment <https://arxiv.org/abs/2603.20897>`__
       might not align with your ethical principles.
     - Consider using AI tools which were built responsibly. Unfortunately this is easier said
       than done: let's work on this together!
