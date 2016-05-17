Decorating: A Meta Repo To Decorators
=================

Collection of decorators, a properly README will be write in soon. For now only have that functionality:

![animation](https://i.imgur.com/8mAXdhu.gif)

## Installation

**WARNING**: This project is still in current development at alpha! Don't use in serious/production application yet.


#### Users

stable:
`sudo pip install decorating`


bleeding-edge:
`sudo pip install git+https://www.github.com/ryukinix/decorating`


#### Developers

```Bash
sudo git clone https://www.github.com/ryukinix/decorating
cd decorating
sudo make develop
```

The develop mode creates a .egg-info (egg-link) as symlink with your standard `site-packages`/`dist-packages` directory. Don't be worry with the `decorating.egg-info`, is only information for the package egg to link with your `PYTHONPATH`. For that, the usage is dynamic, you can modify the code in test on the command line always using absolute imports in anywhere (like the first example)

## License

MIT