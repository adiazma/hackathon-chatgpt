# Web Scraping

### Repository Purpose

The purpose of this repository is to create a versatile environment that can run and persist various projects. Projects can be managed using the --project flag during testing or deployment in a job function.

### Setting Up the Environment Locally

To run the environment on your local machine, please ensure that you have all the necessary libraries installed. You can install them using the following command:

```ssh
python -m pip install -r requirements.txt
```

### Windows Users and Virtual Environment

If you are using Windows and want to utilize a virtual environment, follow these steps:

1. Create a folder named `.venv`.
2. Navigate to `.venv` using the command `cd .venv`.
3. Run the command `python -m venv venv` to create a virtual environment named `venv`.
4. Navigate to `.venv/venv/Scripts` and execute `.\activate`.
5. Return to the main root and run the command to install the necessary libraries.

### Python Version Compatibility

This repository is designed to work with any version of Python. However, as a reference, you can use `Python 3.9` or a higher version.

### Configuration with Environment Variables

To configure the necessary variables such as connections, tokens, etc., create a `.env` file using `.env.dev` as a reference. Populate the `.env` file with all the required information.

### Testing with Visual Studio Code

To debug the project using Visual Studio Code, follow these steps:

1. Create a folder named `.vscode` in the project root.
2. Inside the `.vscode` folder, add a file named `launch.json`.
3. Populate launch.json with the following configuration:

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug Script",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/debug.py",
            "args": [
                "--project=demo_scraper"
            ],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        }
    ]
}
```

After creating `launch.json`, ensure you define the necessary variables. For instance, if your project is `demo_scraper` and requires a username and password, create a `config.json` file with the following content:

```
{
    "username": "My demo username",
    "password": "My demo password"
}
```

The project will detect the config.json file and use it as input for the integration. For specific configuration requirements for `config.json` and `launch.json`, refer to the project's individual README.

### Adding a New Project

To add a new project, follow these steps:

1. Select a name for your project (e.g., my_cool_project).
2. Create a folder named `my_cool_project` within `src/projects`.
3. Inside `src/projects/my_cool_project`, create a file named model.py.
4. Copy the contents of` src/projects/model_template.txt` and paste them into `model.py`. Be sure to replace `NameOfYourProject` with `MyCoolProject`.
5. Congratulations! Now you can run your project using the `--project=my_cool_project` argument.
