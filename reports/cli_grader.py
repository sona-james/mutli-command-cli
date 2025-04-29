# Grade Calculator
import click


@click.command()
@click.option('--n', prompt='Number of Categories', help='Enter the total' +
              'number of categories (hws, tests, etc) that needs to be'
              + 'calculated to find the final grade.')
def cli(n):
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


if __name__ == '__main__':
    cli()
