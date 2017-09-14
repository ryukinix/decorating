Contributing
============

## Development install

I recommend using a virtualenv and installing the package in the `development`
mode. There is a set steps to accomplish that

```Bash
git clone https://www.github.com/ryukinix/decorating
cd decorating
virtualenv env && source env/bin/active
make develop
```

The develop mode creates a .egg-info (egg-link) as a symlink in your
standard `site-packages`/`dist-packages` directory. Don't worry with
the `decorating.egg-info`, it's only information for the package egg
to link with your `PYTHONPATH`. For that, the usage is dynamic, you
can modify the code in test on the command line always using absolute
imports in anywhere (like the first example)

### Make a feature branch

You can create a new branch `git checkout -b feature` based on the
`dev` and send a pull-request to me!  If you just want to know
something or give me a suggestion, create a new issue!

### Before send a PR

Please make sure that lint code is passing without warning. Run the tests before
sending a pull request. If you add something new, please, create new tests!

### Pre-commit (optional)

You can set up pre-commit to make testing + linting per commit more easy.
In the root of git repository, run these commands after cloning the project:

```shell
sudo pip install pre-commit pylint nose2
pre-commit install
```

If you don't know about pre-commit, check
the [pre-commit](http://pre-commit.com) website.
