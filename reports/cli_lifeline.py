# Age Calculator
import click
import datetime


@click.command()
@click.option('--m', prompt='Enter your birth month (1-12)', help='Your '
              + 'birth month')
@click.option('--d', prompt='Enter your birth day (1-31)', help='Your ' +
              'birth date')
@click.option('--y', prompt='Enter your birth year (year number)',
              help='Your birth year')
def cli(m, d, y):
    """An age calculator that provides the current age"""
    m1 = int(m)
    d1 = int(d)
    y1 = int(y)
    # m = int(click.prompt("Enter your birth month (1-12)"))
    if m1 < 1 or m1 > 12:
        click.echo("Invalid input")
        exit()
    # d = int(click.prompt("Enter your birth day (1-31)"))
    if d1 < 1 or d1 > 31:
        click.echo("Invalid input")
        exit()
    # y = int(click.prompt("Enter your birth year (year number)"))
    if y1 > datetime.datetime.now().year:
        click.echo("Invalid input")
        exit()
    birth_date = datetime.date(y1, m1, d1)
    date_today = datetime.date.today()

    result = date_today.year - birth_date.year

    if (birth_date.month, birth_date.year) > (
            date_today.month, date_today.year):
        result -= 1

    click.echo(f"You are {result} years old today")


if __name__ == '__main__':
    cli()
