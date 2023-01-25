def test_migrate_check(cli_invoke, hitfactory_postgres_url):
    result = cli_invoke(["migrate", "check", "--sqlalchemy-url", f"postgresql+asyncpg://{hitfactory_postgres_url}"])
    assert result.exit_code > 0
    assert "target database is not up to date" in result.stdout.strip().lower()


def test_migrate_upgrade(cli_invoke, hitfactory_postgres_url):
    result = cli_invoke(["migrate", "upgrade", "--sqlalchemy-url", f"postgresql+asyncpg://{hitfactory_postgres_url}"])
    assert result.exit_code == 0
    assert "OK" in result.stdout
