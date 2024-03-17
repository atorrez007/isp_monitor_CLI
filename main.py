import click


@click.command()
def main():
    option = click.prompt(
        "Choose an option",
        type=click.Choice(["hello", "speedtest"]),
    )
    if option == "hello":
        hello()
    elif option == "speedtest":
        run_speedtest()


def hello():
    click.echo("Hello!")


def run_speedtest():
    click.echo("running continuous speedtest... To end test, press Ctrl+Z")
    from monitor import run_speed_test

    run_speed_test()


if __name__ == "__main__":
    main()
