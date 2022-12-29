import typer
import uvicorn

typer_app = typer.Typer(
    help="To-do app with a heavy emphasis on NLP-based interaction "
)


@typer_app.command()
def run(port: int = typer.Option(8000, help="Port the app should listen on.")) -> None:
    """Start Todorate."""
    uvicorn.run("todorate:app", port=port)
