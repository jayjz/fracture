"""CLI entrypoint for Fracture."""

import typer

app = typer.Typer(
    name="fracture",
    help="Chaos engineering harness for graph agents.",
    add_completion=False,
)


@app.command()
def version() -> None:
    """Print the current version."""
    from fracture import __version__
    typer.echo(f"fracture {__version__}")


@app.command()
def info() -> None:
    """Show project status and roadmap phase."""
    typer.echo("Fracture — Phase 0 complete (scaffold). See ROADMAP.md")


if __name__ == "__main__":
    app()
