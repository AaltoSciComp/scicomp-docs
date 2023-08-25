FROM python:3.11-slim-bookworm

COPY _meta/search/requirements.txt ./
COPY requirements.txt ./scicomp-docs/
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt beautifulsoup4 markdownify
COPY ./ ./scicomp-docs/
RUN \
    pwd && ls && \
    cd scicomp-docs && \
    sphinx-build -b dirhtml . _build/dirhtml/ && \
    python _meta/search.py create --db=search.db

FROM python:3.11-slim-bookworm

WORKDIR /
USER 1000

COPY --from=0 scicomp-docs/search.db scicomp-docs/_meta/search.py ./

CMD ["python", "search.py", "serve", "--db=search.db", "--bind=0.0.0.0:8000"]
EXPOSE 8000/tcp
