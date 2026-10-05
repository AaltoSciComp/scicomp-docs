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

With moat, symlink under the fake home (for example
``~/moat-home/.codex/skills``) and mount
``/scratch/shareddata/triton-skills`` read-only so the links resolve.

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

Put the pieces from the sections above together.  Do the shared steps once,
then choose whether to run the agent **directly** or **inside moat**.

The commands below use **Codex** as the worked example.  The same steps
apply to other harnesses; swap config paths and MCP/skills install commands
for your tool (see the relevant tabs above).
 
Shared setup
~~~~~~~~~~~~

#. **Connect.**  SSH to the coding-agent login node::

      ssh <username>@code.triton.aalto.fi

   See :doc:`connecting` if you are new to Triton.

#. **Configure the harness.**  Point your agent at the Aalto LLM Gateway (or
   another endpoint from *Configuring harnesses to use LLM endpoints*
   above).  Write the config under your real home first (for running without
   moat)::

      mkdir -p ~/.codex
      cat > ~/.codex/config.toml <<'EOF'
      model = "zai-org/GLM-5.3-Flash"
      model_provider = "aalto"
      approval_policy = "on-request"

      [model_providers.aalto]
      name = "Aalto LLM Gateway"
      base_url = "https://llm-gateway.k8s.aalto.fi/api/v1"
      env_key = "AALTO_LLM_API_KEY"
      wire_api = "responses"
      EOF

      export AALTO_LLM_API_KEY="paste-your-key-here"

   Keep the key in the environment, not in the config file.
   ``approval_policy = "on-request"`` asks before acting — a good default on
   a shared cluster.  For moat, use a separate config under the fake home
   (see below) — a plain copy of this file is not enough.

#. **Teach.**  Add the always-on rule and symlink the skills as described
   under `Triton skills`_ and `Triton agent rules`_ above.

#. **Ground.**  Enable the SciComp docs MCP::

      codex mcp add scicomp-docs --url https://docs.triton.aalto.fi/mcp/

   Verify later with ``/mcp`` inside Codex.  Details are under
   `MCP server`_ above.

#. **Pick a project directory**::

      mkdir -p ~/demo && cd ~/demo
      # … add or clone a small project …

Then choose one of the paths below.

Without moat
~~~~~~~~~~~~

Run the agent directly on the login node.  Simpler, but the agent inherits
your full file permissions::

   export AALTO_LLM_API_KEY="paste-your-key-here"
   codex

Give a concrete task, approve actions on request, and review every change.

.. warning::

   Without a sandbox the agent can read anything you can, including SSH keys
   and credentials under ``$HOME``.  Prefer moat for anything beyond a quick
   test.  See :doc:`/triton/usage/ai-agents`.

With moat
~~~~~~~~~

Install moat, put the agent config into a fake home, create an env that mounts
only the project (and skills), then run.  See *Using moat to secure your
harnesses* above and the `moat README <https://github.com/AaltoRSE/moat>`__.

#. **Install and init moat** (once)::

      mkdir -p ~/tools/moat && cd ~/tools/moat
      curl -sL https://github.com/AaltoRSE/moat/releases/download/v0.1.0/moat_Linux_x86_64.tar.gz | tar xz
      export PATH="$HOME/tools/moat:$PATH"
      moat init

   On Triton, ``/tmp`` is small — point Apptainer's cache at scratch before
   the first run, for example
   ``export APPTAINER_CACHEDIR=$WRKDIR/moat-cache TMPDIR=$WRKDIR/moat-cache``.

#. **Prepare the fake home.**  The agent inside moat uses ``~/moat-home`` as
   ``$HOME``, not your real home.  Copy skills and MCP settings from your
   real ``~/.codex``, then write a **moat-specific** ``config.toml``.  Codex
   must not run its own nested sandbox inside moat — set
   ``sandbox_mode = "danger-full-access"`` so isolation comes from moat
   alone::

      mkdir -p ~/moat-home/.codex
      cp -a ~/.codex/. ~/moat-home/.codex/
      cat > ~/moat-home/.codex/config.toml <<'EOF'
      model = "zai-org/GLM-5.3-Flash"
      model_provider = "aalto"
      approval_policy = "on-request"
      sandbox_mode = "danger-full-access"

      [model_providers.aalto]
      name = "Aalto LLM Gateway"
      base_url = "https://llm-gateway.k8s.aalto.fi/api/v1"
      env_key = "AALTO_LLM_API_KEY"
      wire_api = "responses"
      EOF

   Skills under ``~/moat-home/.codex/skills`` must still resolve to
   ``/scratch/shareddata/triton-skills``, so mount that tree read-only in the
   next step.

#. **Create the env and run.**  Mounts and the fake home are stored in the env
   config and reused on every ``moat run`` — they do not follow a later
   ``cd`` unless you set ``mountcwd``::

      cd ~/demo
      moat env create -n demo -H ~/moat-home -m ~/demo \
          -r /scratch/shareddata/triton-skills -y
      export AALTO_LLM_API_KEY="paste-your-key-here"
      moat run -n demo codex

   The API key still comes from the host shell (``passenv``).  Verify MCP with
   ``/mcp`` and skills with ``/skills`` inside the Codex session.

Either way, give a concrete task (finish a half-written script, run it, report
what changed), approve actions on request, and review every change before you
rely on it.

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
* Triton skills on the cluster: ``/scratch/shareddata/triton-skills``
