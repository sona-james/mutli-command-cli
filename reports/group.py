import click
import datetime


@click.group()
def cli():
    """Main calculator group for the other calculator subcommands."""
    pass


@cli.command()
@click.option('--n1', prompt='First number', help='First number to' +
              'use the operator on.')
@click.option('--n2', prompt='Second number', help='Second number to' +
              'use the operator on.')
@click.option('--op', prompt='Operator', help='Enter operator' +
              '(+ , -, *, /).')
def quickmath(n1, n2, op):
    """A basic arithmetic calculator"""
    num1 = float(n1)
    num2 = float(n2)
    opf = op.strip()
    result = 0

    if (opf == '+'):
        result = num1 + num2
    elif (opf == '-'):
        result = num1 - num2
    elif (opf == '*'):
        result = num1 * num2
    elif (opf == '/'):
        if num2 == 0:
            click.echo("Divison by zero")
        else:
            result = num1/num2
    else:
        click.echo('Not a valid operator. Operator must be +, -, *, or /')

    click.echo(f"Result: {result}")


@cli.command()
@click.option('--n', prompt='Number of Categories', help='Enter the total' +
              'number of categories (hws, tests, etc) that needs to be'
              + 'calculated to find the final grade.')
def grader(n):
    """A final grade calculator"""
    grades = []
    weights = []
    num = int(n)

    for count in range(1, num+1):
        number = int(click.prompt("\nEnter the number of assignments in " +
                                  f"category {count}"))
        l1 = []
        for item in range(1, number + 1):
            grade = float(click.prompt(f"Enter grade #{item} for category " +
                                       f"{count}"))
            l1.append(grade)
        grades.append(l1)
        weight = float(click.prompt(f"\nEnter weight for category {count}" +
                                    "(round decimal to 2 places)"))
        weights.append(weight)

    result = 0
    for i in range(num):
        avg = sum(grades[i]) / len(grades[i])
        result += avg * weights[i]

    click.echo(f"\nFinal Grade: {result}")


@cli.command()
@click.option('--m', prompt='Enter your birth month (1-12)', help='Your '
              + 'birth month')
@click.option('--d', prompt='Enter your birth day (1-31)', help='Your ' +
              'birth date')
@click.option('--y', prompt='Enter your birth year (year number)',
              help='Your birth year')
def lifeline(m, d, y):
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
