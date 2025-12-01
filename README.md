# Earworm 🎵

This is earworm! A simple application that lets you search and view music releases and their information via the [MusicBrainz](https://musicbrainz.org) API. This is a little project I worked on to get my toes into using Tkinter alongside communicating with APIs.

## What does it do?

You can search for any music release using the search bar on the top of the application. Upon hitting `Enter` or clicking the `Search` button on the right, it will display your search results.

If you want to view more information on the release, you can click the `View` button below every item. This will let you view the release's cover image (if it exists), and a list of its tracks and their duration.

## How to run?

### Using uv

The easiest way to get this application running is with [uv](https://github.com/astral-sh/uv), which installs all the prerequisites for you (even sets Python up properly).

1. Make sure you have `uv` installed on your machine.
2. Clone this repository into any folder
3. Open the `earworm` folder with your terminal and run:

```sh
uv run main.py
```

**For Windows users:** if the above command doesn't work in PowerShell, try using the command prompt (cmd)

After running this command, `uv` will install the appropriate version of Python, all the dependencies listed under `pyproject.toml`, and then run the program once everything's installed.

### Manual setup

If you prefer the usual method, A `requirements.txt` is provided. Just follow these steps:

1. Make sure you have Python installed (at least version `3.12`. You could probably get away with a little bit of an older version but let's play it safe).
2. Clone this repository
3. Open the `earworm` folder with your terminal
4. Set up a virtual environment (optional, but **highly** recommended)

   1. Enter this command to create the virtual environment

    ```sh
    python -m venv .venv
    # if the command above doesn't work, try the one below
    python3 -m venv .venv
    ```
    This should create a hidden folder called `.venv`

   2. Once you've confirmed that the `.venv` folder is there, activate the virtual environment using this command.
    ```sh
    # MacOS and Linux
    source .venv/bin/activate

    # Windows
    .\.venv\Scripts\activate
    ```

5. Install the dependencies from `requirements.txt` by running this command:

```sh
pip install -r requirements.txt
```

6. Run the application with the command:
```sh
python main.py
```