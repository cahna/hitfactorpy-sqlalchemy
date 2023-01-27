# CLI Usage

```console
$ hitfactorpy-sqlalchemy --help
$ python -m hitfactorpy-sqlalchemy --help
```

## `--version`

Prints the package version and exits.

```console
$ hitfactorpy-sqlalchemy --version
0.0.4
```

## Command Group: `migrate`

The default database connection string for alembic migrations is 
`postgresql+asyncpg://postgres:postgres@localhost:5432/hitfactorpy`. 
For information on overriding connection settings, run:

```console
$ hitfactorpy-sqlalchemy migrate --help
```

**NOTE**: An async driver is required for alembic to work. (Everything else should work regardless of chosen driver)

### Command: `migrate check`

Verify DB, migrations, and models are in-sync.

```console
$ hitfactorpy-sqlalchemy migrate check
```

### Command: `migrate upgrade`

Apply all pending migrations (default).

```console
$ hitfactorpy-sqlalchemy migrate upgrade <rev>
```

## Command Group: `import`

Commands for importing match data into database.

```console
$ hitfactorpy-sqlalchemy import --help
```

### Command: `import match-report`

Examples:

- Import a match report from a text file:
  ```console
  $ hitfactorpy-sqlalchemy import match-report ./report.txt
  ```

- Bulk import match reports:
  ```console
  $ find reports/ -type f -name "*.txt" | xargs hitfactorpy-sqlalchemy import match-report
  ```
