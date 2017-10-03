# Setting up env using conda


### Following are the steps that will install Anaconda

>Anaconda is actually a distribution of software that comes with conda, Python, and over 150 scientific packages and their dependencies. The application conda is a package and environment manager.

#### Installation

- Downlaod [Anaconda](https://www.continuum.io/downloads) installer
- Once downloaded, make installer executable in the download directoryby
  `chmod +x AnacondaX-X.sh`
- Run `./AnacondaX-X.sh` to install

It's best practice to upgrade all the packages before running, so for that execute
```
conda upgrade conda
conda upgrade --all
```

#### Avoiding conflict with current python versions

Create alias for Anaconda in bash file
- Open `.bashrc` file with any editor, and find the blocks with _some more aliases_
- Add following line
  `alias anaconda='export PATH="home/user/anacondaX/bin:$PATH"'`

This will create an alias for Anaconda, and using the keyword `anaconda` in the particular terminal it will be activated.

#### Creating Packages

- To install a package, type `conda install package_name` in your terminal.
- To uninstall, use `conda remove package_name`
- To update a package `conda update package_name`

#### Creating _conda_ environment

- To create an environment, use
```
conda create -n env_name list of packages
```
in terminal.
- Here `-n env_name` sets the name of the environment (`-n` for name) and `list of packages` is the list of packages to be installed in the environment.

#### Activate environment

Once the environment is created, it can be activated by
```
source activate env_name
```

- `conda list` will give list of packages installed in particular environment.
- To leave the environment, type `source deactivate`

#### Saving and loading environment

 The packages can be saved to a **YAML** file with
 ```
 conda env export > environment.yaml
 ```
- The first part `conda env export` writes out all the packages in the environment, including the Python version.
- The second part of the export command, `> environment.yaml` writes the exported text to a YAML file environment.yaml

- To create an environment from an environment file use
`conda env create -f environment.yaml`
 This will create a new environment with the same name listed in environment.yaml.

- `conda env list` to list out all the environments available

- `conda env remove -n env_name` will remove the specified environment


##### References

- This document summarizes conda environment setup, largely inspired by this [course](https://classroom.udacity.com/courses/ud1111) at [Udacity](https://www.udacity.com/)
- Also  [Anaconda documentation](https://docs.anaconda.com/anaconda/install/linux)


Complied by [Deep Doshi](mailto:deepdoshi@live.in)
