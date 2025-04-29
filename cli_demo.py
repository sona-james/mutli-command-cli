import click
import pyfiglet


@click.command()
@click.option('-n', '--name', default='from cli1.py', help='Name of user' +
              'to greet.')
@click.option('-c', '--count', default=1, help='Number of greetings.')
def cli(name, count):
    """DEMO: Simple program that greets NAME for a total of COUNT times.

    The first line is used to describe the program.  The remaining lines,
    like these, can be included in the docstring of the python file
    to provide more detailed help.

    """
    figlet = pyfiglet.Figlet()

    for _ in range(count):
        big_string = figlet.renderText(f'Hello, {name}!')
        click.echo(big_string)


if __name__ == '__main__':
    cli()
