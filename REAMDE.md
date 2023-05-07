# Overlaying Text on an Image with Python

## Prerequisites

Tested with Python 3.11.1 on a Macbook Pro

##  Set up

Python virtualenv

```zsh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Write your quotes

In [quotes.json](./quotes.json), update the array of quotes to be whatever you want.

## Generate you images

```zsh
python overlay_text.py
```

You'll see a directory called `posts` has been created, with a directory for each of the backgrounds you have, with images overlayed with quotes inside.
