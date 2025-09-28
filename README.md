# Dev-Joke CLI 🃏

A simple and fun command-line tool to fetch and display random programming jokes directly in your terminal.

This project was built to learn and demonstrate two powerful Python libraries for building CLIs: **Rich** and **Typer**.

## Features

-   Fetches a random programming joke from a public API.
-   Displays the joke in a beautifully formatted and colored panel.
-   Clean, modern CLI structure.
-   Handles network errors gracefully.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/aayush-0131/dev-joke-cli.git](https://github.com/aayush-0131/dev-joke-cli.git)
    cd dev-joke-cli
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install rich typer requests
    ```

## Usage

Simply run the `main.py` script from your terminal:

```bash
python main.py


Example Output
Fetching a joke for you... ✔
╭─────────────────── 🃏 Here's a Joke! 🃏 ────────────────────╮
│                                                             │
│ Why do programmers prefer dark mode?                        │
│                                                             │
│ Because light attracts bugs.                                │
│                                                             │
╰─────────────────────────────────────────────────────────────╯
