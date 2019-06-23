To contribute to this project, first fork this project in your own GitHub account.

Then follow the guidelines to setup the development environment.

```bash
# Clone from your GitHub repo locally
git clone https://github.com/$USER/htmldoom
cd htmldoom

# Create and activate virtual environment. You need Python version > 3.6
python3 -m venv .venv
source .venv/bin/activate

# Install library in edit mode with tools for testing
pip install -r dev-requirements.txt

# Create your branch. Use prefix such as fix/ or add/ based on the contribution type. e.g.
git checkout -b fix/my-patch
```

Then make the changes and format using `black .`. Or even better, use editor integration for [black](https://github.com/python/black).

Test the changes locally using `pytest` or `tox` (if you have the supported python versions installed).

Commit your changes. Each commit and pull request should solve a specific problem. Use `rebase`, `squash` or `--amend` to squash your commits.
 Check out the [git commit guidelines](https://chris.beams.io/posts/git-commit/).

After that push the changes to your repo and raise a pull request to the [master branch](https://github.com/sayanarijit/htmldoom/tree/master).
