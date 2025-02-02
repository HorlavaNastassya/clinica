# Installation

You will find below the steps for installing Clinica on Linux or Mac. Please do
not hesitate to contact us on the
[forum](https://groups.google.com/forum/#!forum/clinica-user) or
[GitHub](https://github.com/aramis-lab/clinica/issues)
if you encounter any issues.


## Prepare your Python environment
You will need a Python environment to run Clinica. We advise you to
use [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
Miniconda allows you to install, run, and update Python packages and their
dependencies. It can also create environments to isolate your libraries.
To install Miniconda, open a new terminal and type the following commands:

- If you are on Linux:
```{.sourceCode .bash}
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda-installer.sh
bash /tmp/miniconda-installer.sh
```

- If you are on Mac:
```{.sourceCode .bash}
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o /tmp/miniconda-installer.sh
bash /tmp/miniconda-installer.sh
```

Miniconda will ask you where to install it. Do not forget to copy the `export
PATH` given at the end of the installation. If everything went
fine, open a new terminal and type `conda info`, it will verify if Conda is
installed, check the version and show your Miniconda path.

## Install Clinica

The latest release of Clinica can be installed by using the conventional
[PyPI package manager](https://pypi.org/project/clinica/) as follows:

```bash
conda create --name clinicaEnv python=3.7
conda activate clinicaEnv
pip install clinicaml
```

!!! info
    Since Clinica `v0.3.5`, Conda installation is not proposed anymore (i.e.
    `conda create --name clinicaEnv python=3.6 clinica -c Aramislab -c conda-forge`
    will only install Clinica `v0.3.4`). Pip is now the
    only way to install latest versions of Clinica.

??? info "Developer installation (Advanced)"
    If you plan to contribute to Clinica or if you want to have the current development
    version, you can either:

    * Download the tarball for a specific version from our
    [repository](https://github.com/aramis-lab/clinica/releases).
    Then decompress it.
    * Clone Clinica's repository from GitHub:
    ```bash
    git clone https://github.com/aramis-lab/clinica.git
    ```

    We suggest creating a custom Conda environment and installing Clinica inside it:
    ```bash
    cd clinica
    conda create --name clinicaEnv python=3.7
    conda activate clinicaEnv
    pip install -r requirements-dev.txt
    pip install -e .
    ```

## Installation of the third-party software packages
Depending on the pipeline that you want to use, you need to install
**pipeline-specific interfaces**. Not all the dependencies are necessary to run
Clinica.
Please refer to [this section](../Third-party) to determine which third-party
libraries you need to install.


## Run the Clinica environment
### Activation of the Clinica environment

Now that you have created the Clinica environment, you can activate it:

```{.sourceCode .bash}
conda activate clinicaEnv
activate-global-python-argcomplete --user # Only the first time you activate the environment
eval "$(register-python-argcomplete clinica)"
```

!!! success
    Congratulations, you have installed Clinica! At this point, you can try the
    basic `clinica` command and get the help screen:
    ```bash
    (clinicaEnv)$ clinica
    usage: clinica [-v] [-l file.log]  ...

    clinica expects one of the following keywords:

        run                 To run pipelines on BIDS/CAPS datasets.
        convert             To convert unorganized datasets into a BIDS hierarchy.
        iotools             Tools to handle BIDS/CAPS datasets.
        visualize           To visualize outputs of Clinica pipelines.
        generate            To generate pre-filled files when creating new
                            pipelines (for developers).

    Optional arguments:
      -v, --verbose         Verbose: print all messages to the console
      -l file.log, --logname file.log
                            Define the log file name (default: clinica.log)
    ```

    If you have successfully installed the third-party software packages, you are ready
    to run any of the pipelines proposed by Clinica.

    You can now learn how to [interact with Clinica](../InteractingWithClinica).

### Deactivation of the Clinica environment
At the end of your session, remember to deactivate your Conda environment:
```{.sourceCode .bash}
conda deactivate
```
