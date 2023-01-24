# hitfactorpy_sqlalchemy

[![Main](https://github.com/cahna/hitfactorpy-sqlalchemy/actions/workflows/main.yaml/badge.svg)](https://github.com/cahna/hitfactorpy-sqlalchemy/actions/workflows/main.yaml)

Manage practical match reports in a database with SQLAlchemy

## Status

**Work in progress...**

## CLI Usage

The default database connection string is `postgresql+asyncpg://postgres:postgres@localhost/hitfactorpy`. Changes to connection settings are made via `--sqlalchemy-url` option, or by setting `HITFACTORPY_SQLALCHEMY_URL` environment variable.

1. Run migrations on an empty database to create tables and types:
    ```console
    $ hitfactorpy-sqlalchemy migrate upgrade
    ```
2. Verify DB status:
    ```console
    $ hitfactorpy-sqlalchemy migrate check
    ```
3. Import a match report from a text file:
    ```console
    $ hitfactorpy-sqlalchemy import match-report ./report.txt
    ```
4. Bulk import match reports:
    ```console
    $ find reports/ -type f -name "*.txt" | xargs hitfactorpy-sqlalchemy import match-report
    ```
