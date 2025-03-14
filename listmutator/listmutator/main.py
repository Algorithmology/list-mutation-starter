"""Conduct experiments to evaluate performance of list concatenation."""

# ruff: noqa: PLR0913

import typer
from rich.console import Console

from listmutator import approach, benchmark

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()

# TODO: Make sure that you implement all of the required functions in the other
# files that will ensure that these function(s) work correctly.

# TODO: Add all of the required features for each of the steps that are documented
# with additional TODO markers inside of the main function provided below.


@cli.command()
def main(
    listtype: approach.ListType = typer.Option(
        approach.ListType.singlylinked,
    ),
    listdata: approach.ListData = typer.Option(
        approach.ListData.ints,
    ),
    strategy: approach.BenchmarkStrategy = typer.Option(
        approach.BenchmarkStrategy.double,
    ),
    operation: approach.BenchmarkOperation = typer.Option(
        approach.BenchmarkOperation.removefirst,
    ),
    startsize: int = typer.Option(1000),
    runs: int = typer.Option(10),
):
    """Evaluate the performance of list operations."""
    # display details about the configuration of the benchmarking tool
    console.print(
        "\n[bold red]Benchmarking Tool for List Operations[/bold red]\n"
    )
    console.print(f"Type of list: {listtype}")
    console.print(f"Data stored in list: {listdata}")
    console.print(f"Benchmarking strategy: {strategy}")
    console.print(f"Benchmarking operation: {operation}")
    console.print(f"Number of runs: {runs}\n")
    # TODO: perform the benchmarking operation
    # TODO: display the results concerning the minimum execution time
    # --> minimum value
    # TODO: display the results concerning the maximum execution time
    # --> maximum value
    # TODO: display the results concerning the average execution time
    # --> average value
    # TODO: make sure that all of the output from running the benchmarks
    # is formatted, justified, and aligned in a consistent and helpful fashion
    # TODO: see the README.md file for an example of correctly formatted output
