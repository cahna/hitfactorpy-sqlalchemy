def test_migrate_help(cli_invoke):
    result = cli_invoke(["migrate", "--help"])
    assert result.exit_code == 0
    assert result.stdout.lstrip().startswith("Usage:")


def test_migrate_check(cli_invoke, postgres_service):
    result = cli_invoke(["migrate", "check", "--sqlalchemy-url", f"postgresql+psycopg2://{postgres_service}"])
    assert result.exit_code == 0
    assert result.stdout == "yes"
