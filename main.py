# main.py

import typer
import requests
from rich.console import Console
from rich.panel import Panel

# --- Key Decisions & Approach ---
# 1. Typer: We're using Typer to create our Command-Line Interface (CLI) app.
#    It's modern, easy to use, and automatically generates help text.
#    The `@app.command()` decorator turns a regular function into a CLI command.
# 2. Rich: This library is for making the output beautiful. We use `Console` to
#    handle printing and `Panel` to draw a nice box around our joke.
# 3. Requests: A standard, reliable library for making HTTP requests to the API.
# 4. API: We are using the "Official Joke API" which is free and requires no API key,
#    making our project simple and easy to run.

# Initialize the Typer app and Rich console
app = typer.Typer()
console = Console(force_terminal=True)

# Define the URL for the programming jokes API
API_URL = "https://official-joke-api.appspot.com/jokes/programming/random"


@app.command()
def joke():
    """
    Fetches a random programming joke and displays it in a formatted panel.
    """
    try:
        # Use a "spinner" to show the user that something is happening
        with console.status(
            "[bold green]Fetching a joke for you...", spinner="dots"
        ) as status:
            # Make the API request
            response = requests.get(API_URL)
            # Raise an exception if the request was unsuccessful (e.g., 404, 500)
            response.raise_for_status()

            # The API returns a list containing a single joke object
            joke_data = response.json()[0]

            # Extract the setup and punchline
            setup = joke_data["setup"]
            punchline = joke_data["punchline"]

            # Combine the setup and punchline into a single string
            joke_text = (
                f"[cyan]{setup}[/cyan]\n\n[bold magenta]{punchline}[/bold magenta]"
            )

        # Create a Rich Panel to display the joke
        joke_panel = Panel(
            joke_text,
            title="🃏 Here's a Joke! 🃏",
            border_style="green",
            expand=False,  # Panel will fit the content size
        )

        # Print the panel to the console
        console.print(joke_panel)

    except requests.exceptions.RequestException as e:
        # Handle network or HTTP errors gracefully
        console.print(
            f"[bold red]Error:[/bold red] Failed to connect to the joke API. Please check your internet connection."
        )
    except (KeyError, IndexError):
        # Handle unexpected API response format
        console.print(
            "[bold red]Error:[/bold red] Received an invalid response from the API."
        )


if __name__ == "__main__":
    # This makes the script runnable
    app()
