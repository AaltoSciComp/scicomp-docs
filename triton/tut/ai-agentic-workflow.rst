==========================================
Getting started with AI assisted workflows
==========================================

.. admonition:: Abstract

  Quick summary of this page

What are the key pieces in agentic workflows?
---------------------------------------------

Large language models
~~~~~~~~~~~~~~~~~~~~~

Harnesses
~~~~~~~~~

Connecting to Triton while using agents
---------------------------------------

Configuring harnesses to use LLM endpoints
------------------------------------------

.. tabs::

   .. tab:: Aalto ITS provided LLMs

   .. tab:: Aalto SciComp provided local LLMs

.. tabs::

   .. tab:: Codex

      Instructions for Codex

   .. tab:: Claude

      Instructions for Claude

   .. tab:: OpenCode

      Instructions for Opencode

   .. tab:: Pi

      Instructions for Pi

Using moat to secure your harnesses
-----------------------------------

Triton-specific skills and agentic instructions
-----------------------------------------------

Agents do not know Triton's documentation, tools, or policies by
default.  Give them these kinds of local knowledge so they look things up
instead of guessing.


MCP server
~~~~~~~~~~

An MCP (`Model Context Protocol
<https://modelcontextprotocol.io>`__) server can expose tools to your agent
harness.  On Triton, you can connect to the hosted SciComp Docs MCP.  It provides a documentation lookup tool, ``search_scicomp_docs``, which searches relevant
pages and returns excerpts with published ``https://scicomp.aalto.fi/`` URLs.

Each harness has its own MCP settings location and syntax.  Examples for
connecting to the SciComp Docs MCP:

.. tabs::

   .. tab:: Codex

      From the shell::

         codex mcp add scicomp-docs --url https://docs.triton.aalto.fi/mcp/

      Then verify inside Codex with ``/mcp``.

   .. tab:: Cursor

      Add this to your MCP servers config (Cursor Settings → MCP)::

         {
           "mcpServers": {
             "scicomp-docs": {
               "url": "https://docs.triton.aalto.fi/mcp/"
             }
           }
         }

      Reload MCP if Cursor asks you to, then confirm ``search_scicomp_docs``
      appears in the tool list.

   .. tab:: Claude Code

      ::

         claude mcp add --transport http scicomp-docs https://docs.triton.aalto.fi/mcp/

      Verify with ``claude mcp list`` or ``/mcp``.  Use ``--scope user`` for
      all projects.  If you configure via JSON, include ``"type": "http"`` —
      a bare ``url`` entry is treated as stdio and skipped.

   .. tab:: Other (JSON)

      Many OpenAI-compatible / MCP clients accept a JSON block like this —
      place it in that client's MCP config file::

         {
           "mcpServers": {
             "scicomp-docs": {
               "url": "https://docs.triton.aalto.fi/mcp/"
             }
           }
         }

Ask a docs question in chat (for example “How do I request a GPU on
Triton?”) and check that the agent calls ``search_scicomp_docs`` and cites
the returned URLs.  In agent / auto mode it may call the same tool whenever
it needs Triton or SciComp facts.

Full client notes are in the `docs MCP guide
<https://github.com/AaltoSciComp/llm-examples/blob/main/triton-mcp/docs-mcp.md>`__.


Triton skills
~~~~~~~~~~~~~

`triton-skills <https://github.com/AaltoSciComp/triton-skills>`__ provides
agent skills for Triton-specific workflows and safety posture — not generic
Slurm or Python tutorials.  On Triton, use the shared tree
``/scratch/shareddata/triton-skills/``.

These skills are recommended for all Triton projects:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Skill
     - Use when
   * - ``triton-agent-hygiene-skill``
     - Agent etiquette, ``code.triton``, secrets, job storms
   * - ``triton-sbatch-drafting-skill``
     - Draft ``#SBATCH`` scripts (serial / array / GPU / MPI)
   * - ``triton-job-monitoring-skill``
     - ``slurm q``, ``seff``, right-sizing
   * - ``triton-modules-envs-skill``
     - Lmod, conda/mamba, central envs
   * - ``triton-llms-skill``
     - Hugging Face / LLMs, shared model cache, ``scicomp-llm-env``
   * - ``triton-storage-io-skill``
     - ``$HOME`` / ``$WRKDIR`` / project scratch, quotas, I/O
   * - ``triton-containers-skill``
     - Apptainer/Singularity, binds, GPU / ``--nv``, ARM

Install the full set by **symlinking** (do not copy) so shared-tree updates
apply automatically::

   REPO=/scratch/shareddata/triton-skills

.. tabs::

   .. tab:: Cursor

      Personal::

         mkdir -p ~/.cursor/skills
         for d in "$REPO"/triton-*-skill; do
           ln -sfn "$d" ~/.cursor/skills/"$(basename "$d")"
         done

      Project-local::

         mkdir -p .cursor/skills
         for d in "$REPO"/triton-*-skill; do
           ln -sfn "$d" .cursor/skills/"$(basename "$d")"
         done

   .. tab:: Claude Code

      ::

         mkdir -p ~/.claude/skills   # or .claude/skills in a project
         for d in "$REPO"/triton-*-skill; do
           ln -sfn "$d" ~/.claude/skills/"$(basename "$d")"
         done

   .. tab:: Codex

      ::

         mkdir -p ~/.codex/skills
         for d in "$REPO"/triton-*-skill; do
           ln -sfn "$d" ~/.codex/skills/"$(basename "$d")"
         done

Triton agent rules
~~~~~~~~~~~~~~~~~~

Agent harnesses store persistent rules under different names
(``CLAUDE.md``, ``AGENTS.md``, Cursor/Codex user rules, and so on).  Use
**global rules** for every session on Triton, and **project rules** for one
repository's modules, data paths, and job conventions.  Keep both short
enough that the agent can follow them.

The maintained Triton HPC rules lives in
(`triton-rules.md
<https://github.com/AaltoSciComp/triton-skills/blob/main/triton-rules.md>`__).
On Triton the same file is at
``/scratch/shareddata/triton-skills/triton-rules.md``.

No need to replace your ``AGENTS.md`` / ``CLAUDE.md`` with that file.  Keep
your own harness instructions, and add an additional line that points the
agent at the shared policy when it works on Triton, for example::

   When working on HPC, read
   /scratch/shareddata/triton-skills/triton-rules.md
   and follow the policies there.

Put that in ``AGENTS.md``, ``CLAUDE.md``, Cursor rules, or the equivalent
your agent loads.

.. admonition:: Current ``triton-rules.md`` (live from GitHub)
   :class: dropdown

   .. raw:: html

      <div data-triton-rules
           data-rules-url="https://raw.githubusercontent.com/AaltoSciComp/triton-skills/main/triton-rules.md">
        <p>Loading current Triton agent rules...</p>
      </div>
      <noscript>
        <p>This live copy requires JavaScript.  Read
        <a href="https://github.com/AaltoSciComp/triton-skills/blob/main/triton-rules.md">triton-rules.md on GitHub</a>
        or <code>/scratch/shareddata/triton-skills/triton-rules.md</code> on Triton.</p>
      </noscript>

For project rules, tell the agent which modules or containers to reuse,
where data and job output go (not ``$HOME``), and the usual partition /
time / memory / CPU or GPU and array layout for this repository.

Testing out your new workflow
-----------------------------

Put the pieces from the sections above together and run the agent **inside
moat**.

On Triton, load the ``moat-agents`` module.  It provides `moat
<https://github.com/AaltoRSE/moat>`__ (the container sandbox) and
`moat-install <https://github.com/AaltoRSE/moat-install>`__ (one-shot
configuration of the harnesses in moat's image: Codex, Claude Code,
OpenCode, pi, and others).  One shared fake home holds every agent's
config; the directory you start ``moat run`` from is mounted into the
container.

**Host vs container.**  ``module load moat-agents`` and ``moat-install``
run on the **login node** (the host).  Only ``moat run`` starts the
Apptainer container.  Endpoint checks, API-key prompts, and writing
configs under the home base all happen on the host before any container
starts.

#. **Connect.**  SSH to the coding-agent login node::

      ssh <username>@code.triton.aalto.fi

   See :doc:`connecting` if you are new to Triton.

#. **Load the module**::

      module load moat-agents

#. **First-time setup with** ``moat-install``::

      moat-install --no-verify

   It reads API keys from the env vars named in the specification (or
   prompts for them) and writes harness configs under the home base.
   Re-runs with the same inputs are safe.  On Triton, include
   ``--no-verify``: the optional Python reachability probe often fails
   on SSL / CA trust even when ``curl`` to the gateway works.  That
   probe runs on the host, not inside moat.

#. **Teach and ground in the fake home.**  Enable the SciComp docs MCP
   under the home base, as
   described under `MCP server`_ above.  Do this in the fake home, not
   your real ``$HOME``. 

#. **Pick a project directory**::

      mkdir -p ~/demo && cd ~/demo
      # … add or clone a small project …

#. **Quick test**::

      moat run -n agents "codex --no-daemon --sandbox danger-full-access"

   Codex needs ``--no-daemon`` inside moat, because a background daemon
   would be orphaned when the container exits. Give a small concrete
   task (finish a half-written script, run it, report what changed),
   approve actions on request, and check ``/mcp`` inside the session.
   Review every change before you rely on it. 

   Other harnesses use the same environment::

      moat run -n agents opencode
      moat run -n agents pi

   ``moat run -n agents`` without a command opens a ``bash`` shell in the
   container.

You are responsible for what the agent does.  Keep heavy compute off the
login node, keep secrets out of agent-readable trees, and save work often.
Full policy: :doc:`/triton/usage/ai-agents`.


See also
--------

* :doc:`AI agents on Triton </triton/usage/ai-agents>` — risks, accounts,
  sandboxing with moat, custom LLM APIs, and longer configuration notes
* `docs MCP guide
  <https://github.com/AaltoSciComp/llm-examples/blob/main/triton-mcp/docs-mcp.md>`__
* `ASC LLM examples <https://github.com/AaltoSciComp/llm-examples>`__
* `moat <https://github.com/AaltoRSE/moat>`__ — container sandbox for AI tools
* `moat-install <https://github.com/AaltoRSE/moat-install>`__ — configure
  harnesses under a moat home base from one provider specification
* Triton skills on the cluster: ``/scratch/shareddata/triton-skills``
