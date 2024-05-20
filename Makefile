# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build/

default: html
	@true  # this is needed, or the % rule below is done for default.
	@echo
	@echo "Build successful.  Run 'make check' to check for important warnings"

check:
	make html SPHINXOPTS="-w warnings.txt $(SPHINXOPTS)"
	python _meta/check-warnings.py --fail warnings.txt
	@echo
	@echo "OK: no errors"

autobuild:
	sphinx-autobuild . _build/html/

# Put it first so that "make" without argument is like "make help".
help:
	$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: default help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Autobuild with sphinx-autobuild
livehtml:
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)"/html $(SPHINXOPTS) $(O)

# Make a list of files by last modification date
find-old:
	@git ls-files -z | xargs -0 -n1 -I{} -- git --no-pager log -1 --date=format:'%s,%Y-%m-%d' --format='%ad,  {}' -- {}

# export TOKEN=your_plausible_token
# PLAUSIBLE=plausible.io SITENAME=my.site.eu
usage-report:
	make --silent find-old > _meta/edit-dates.txt
	python _meta/plausible-get-stats.py $(PLAUSIBLE) $(SITENAME) > _meta/pages-$$(date +%Y-%m-%d).csv
	python _meta/join-edit-dates-and-plausible.py _meta/pages-$$(date +%Y-%m-%d).csv _meta/edit-dates.txt > _meta/edit-dates-joined.csv
