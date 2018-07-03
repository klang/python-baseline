# Python3


## virtual environment using `virtualenv` on mac

    brew install python3
    pip3 install --upgrade pip setuptools
    pip3 install virtualenv

    virtualenv -p $(which python3) venv
    source venv/bin/activate


## virtual environment using `venv` on mac

https://medium.com/@henriquebastos/the-definitive-guide-to-setup-my-python-workspace-628d68552e14

    brew install pyenv
    brew install pyenv-virtualenv
    brew install pyenv-virtualenvwrapper
    pyenv install 3.6.5
    
    pyenv virtualenv 3.6.5 baseline
    pyenv activate baseline
    pyenv global 3.6.0 baseline
    pyenv deactivate
    
    
    pyenv virtualenv 3.6.5 baseline-flask
    pyenv activate baseline-flask
    export PYENV_VIRTUALENV_DISABLE_PROMPT=1
    pip install -r requirements.txt
    FLASK_ENV=development FLASK_APP=tools/hello.py flask run
    

# intellij evironment

"File" -> "Project Structure..." -> "Project"

![file project_structure project](./docs/1.project-structure-add-local-sdk.png)

Under Project SDK, "New"

![select python for project](./docs/2.select-python-for-project.png)


Write the path to the environment you want

    /Users/klang/.pyenv/versions/baseline/bin/python3
    
    
If an `requirements.txt` file is present, IntelliJ will install the requirements in the environment selected.

