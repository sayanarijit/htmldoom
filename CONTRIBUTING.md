To contribute to this project, first clone this project in your own GitHub account.

Then follow the guidelines to setup the development environment.

```bash
# Clone from your GitHub repo locally
git clone https://github.com/$USER/htmldoom
cd htmldoom

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install library in edit mode with tools for testing
pip install -e '.[testing]'

# Create your branch. Use prefix such as fix/ or add/ based on the contribution type. e.g.
git checkout -b fix/my-patch
```

Then make the changes and format using `black $filename`.

Also test the changes locally using `pytest`.

Commit your changes. Each commit and pull request should solve a specific problem. Use `rebase`, `squash` or `--amend` to squash your commits.
 Check out the [git commit guidelines](https://chris.beams.io/posts/git-commit/).

After that push the changes to your repo and raise a pull request to [master branch](https://github.com/sayanarijit/htmldoom).
