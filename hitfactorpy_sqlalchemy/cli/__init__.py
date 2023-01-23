import typer

from .migrate import cli as migrate_cli

CLI_NAME = "hitfactorpy_sqlalchemy"

cli = typer.Typer()
subcommand_import = typer.Typer()
cli.add_typer(subcommand_import, name="import")
cli.add_typer(migrate_cli, name="migrate")


@subcommand_import.command("match-report")
def import_match_report():
    """Import a match report"""
    typer.echo("TODO")


if __name__ == "__main__":
    cli()
