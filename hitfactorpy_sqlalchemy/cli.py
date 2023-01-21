import typer

CLI_NAME = "hitfactorpy_sqlalchemy"

cli = typer.Typer()


@cli.command()
def foo():
    """TODO"""
    typer.echo("TODO")


@cli.command()
def bar():
    """TODO"""
    typer.echo("TODO")


if __name__ == "__main__":
    cli()
