import click


@click.group(short_help="latex CLI.")
def latex():
    """latex CLI.
    """
    pass


@latex.command()
@click.argument("name", default="latex")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [latex]
