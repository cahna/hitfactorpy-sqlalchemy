from sqlalchemy.engine.url import URL


def test_migrate_help(cli_invoke):
    result = cli_invoke(["migrate", "--help"])
    assert result.exit_code == 0
    assert result.stdout.lstrip().startswith("Usage:")


def test_migrate_check(cli_invoke, postgres_service: URL):
    invoke_args = [
        "migrate",
        "--host",
        postgres_service.host,
        "--username",
        postgres_service.username,
        "--port",
        postgres_service.port,
        "--database",
        postgres_service.database,
        "check",
    ]
    result = cli_invoke(invoke_args)
    assert result.exit_code > 0
    assert "not up to date" in result.stdout.lower()
