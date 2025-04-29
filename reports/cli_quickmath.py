# Basic Calculator
import click


@click.command()
@click.option('--n1', prompt='First number', help='First number to' +
              'use the operator on.')
@click.option('--n2', prompt='Second number', help='Second number to' +
              'use the operator on.')
@click.option('--op', prompt='Operator', help='Enter operator' +
              '(+ , -, *, /).')
def cli(n1, n2, op):
    """A basic arithmetic calculator"""
    # click.echo(f"Enter First Number: {n1}!")
    # click.echo(f"Enter Second Number: {n2}!")
    # click.echo(f"Enter First Number: {op}!")
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


if __name__ == '__main__':
    cli()
