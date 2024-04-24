FROM python:3.11-slim-bookworm

# This is a multi-stage build.  First stage:

# COPY: copies stuff into the image (relative to the first path on the
# build command line)
# RUN: run something in the image to set it up.

COPY _meta/search/requirements.txt ./
COPY requirements.txt ./scicomp-docs/
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt beautifulsoup4 markdownify
COPY ./ ./scicomp-docs/

# This builds the database.  Make the HTML files and then `search.py
# create` makes a `search.db` file.

RUN \
    pwd && ls && \
    cd scicomp-docs && \
    rm -f search.db _build/dirhtml/ && \
    sphinx-build -b dirhtml . _build/dirhtml/ && \
    python _meta/search.py create --db=search.db



# Make final image.  Only copy search.db and search.py into it, since
# that's all that's needed - search.py has no dependencies in `serve`
# mode.  What the below means: make a new image, copy (`--from=0`)
# from the temporary image above.

FROM python:3.11-slim-bookworm
WORKDIR /

COPY --from=0 scicomp-docs/search.db scicomp-docs/_meta/search.py ./
RUN mkdir search && \
    mv search.db search/ && \
    chown -R 1000 search/ && \
    chmod -R a+rwX search/

# This is the command that will happen when you `docker run IMAGE`
# with no arguments.
USER 1000
CMD ["python", "search.py", "serve", "--db=search/search.db", "--bind=0.0.0.0:8000"]
# This documents and sets up for port 8000 to be forwarded into the
# container.
EXPOSE 8000/tcp
