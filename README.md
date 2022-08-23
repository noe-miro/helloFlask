# helloFlask
Web-based application

## Installation and usage of pyenv
* ```sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev
sudo apt-get install libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev 
sudo apt-get install xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev ``

* ```curl https://pyenv.run | bash```

* ```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc 
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc 
echo 'eval "$(pyenv init -)"' >> ~/.bashrc```

* Uncomment conda activation lines in ```~/.bashrc```

* ```pyenv install 3.10.4```

*  ```pyenv virtualenv 3.10.4 testEnv310```

* ```pyenv activate testEnv310```

* Set up a default python version: 
```pyenv global 3.10.4```

* Check current python version:
```pyenv which python```

* Set up local version
``` 
cd my/path/
pyenv local 3.10.6
```
