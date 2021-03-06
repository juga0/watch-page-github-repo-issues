# watch_page_github_repo_issues

Work in progress...

## Installation in Debian/Ubuntu

### System dependencies

`sudo apt-get install python-dev`

For lxml package:
 `sudo apt-get install libxml2-dev libxslt1-dev`

### With virtualenv

#### Obtain virtualenv

Check https://virtualenv.pypa.io/en/latest/installation.html or if Debian equal/newer than jessie (virtualenv version equal or greater than 1.9)

    sudo apt-get install python-virtualenv

#### Create a virtualenv

    mkdir ~/.virtualenvs
    virtualenv ~/.virtualenvs/oiienv
    source ~/.virtualenvs/oiienv/bin/activate

#### Install dependencies in virtualenv
    git clone https://meta.openintegrity.org/agents/watch-page-github-repo-issues.git
    cd watch-page-github-repo-issues
    pip install -r requirements.txt

## Configuration

To change the host/port in which this agent listen, modify `config.yml` or
create the environment variables:
    ```
    WATCH_PAGE_HOST='watchhost'
    WATCH_PAGE_PORT='watchport'
    ```
and run `set_ip_port.py`

To change the host/port in which the fetch agent listen, modify `config.py` or
create the following environment variables:
    ```
    FETCH_PAGE_HOST='fetchhost'
    FETCH_PAGE_PORT='fetchport'
    ```

## Running

    cd watch_page_github_repo_issues
    nameko run watch_page_github_repo_issues
