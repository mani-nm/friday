## FRIDAY: PDF Document summarizer
Environment setup and configuration
We will be using pipenv for python virtualenv management. Pipenv automatically creates and manages a virtualenv for our project, as well as adds/removes packages from the Pipfile as we install/uninstall packages. It also generates a project Pipfile.lock, which is used to produce deterministic builds.
*Installation steps:
>1. If using defualt python: `pip install --user pipenv`
>2. If using conda (like me): `conda install conda-forge::pipenv`

Create virtualenv for the project: `pipenv shell`
---------------------------------------
Steps:
1. Ollama:
>1) Download and install Ollama
>2) Pull LLama3.1 model 
>3) \bye
2. Clone the repo: https://github.com/mani-nm/friday.git
3. Create virtual conda env and install the requirements
4. Move the source pdf in the data (create it if not present) folder.
5. Execute and generate the summary
6. Edit it and play around. :)
--------------------------------
