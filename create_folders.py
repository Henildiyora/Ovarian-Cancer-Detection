import os
import argparse
import subprocess

# Function to create folder structure
def create_folder_structure(project_name):
    # Define the folder structure with the project name
    folders = [
        f'{project_name}/data/raw',
        f'{project_name}/data/processed',
        f'{project_name}/data/external',
        f'{project_name}/notebooks',
        f'{project_name}/src/data',
        f'{project_name}/src/features',
        f'{project_name}/src/models',
        f'{project_name}/src/visualization',
        f'{project_name}/src/utils',
        f'{project_name}/tests',
    ]

    # Define the files to create within the folder structure
    files = [
        f'{project_name}/src/data/load_data.py',
        f'{project_name}/src/data/preprocess.py',
        f'{project_name}/src/features/build_features.py',
        f'{project_name}/src/models/train_model.py',
        f'{project_name}/src/models/evaluate_model.py',
        f'{project_name}/src/visualization/visualize.py',
        f'{project_name}/src/utils/helper_functions.py',
        f'{project_name}/.gitignore',
        f'{project_name}/README.md',
        f'{project_name}/requirements.txt',
        f'{project_name}/main.py',
    ]

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create empty files
    for file in files:
        with open(file, 'w') as f:
            pass

    print(f"Folder structure for '{project_name}' created successfully.")

# Function to create conda virtual environment
def create_conda_venv(venv_name, python_version="3.10"):
    # Run the conda command to create a virtual environment
    print(f"Creating conda virtual environment '{venv_name}' with Python {python_version}...")
    
    try:
        # Create the conda environment
        subprocess.run(['conda', 'create', '--name', venv_name, f'python={python_version}', '-y'], check=True)
        print(f"Conda virtual environment '{venv_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating conda environment: {e}")

# Main function to handle CLI
if __name__ == "__main__":
    # Argument parser for CLI input
    parser = argparse.ArgumentParser(description='Create ML project folder structure with conda virtual environment.')
    parser.add_argument('project_name', type=str, help='Name of the project')
    # parser.add_argument('venv_name', type=str, help='Name of the conda virtual environment')
    # parser.add_argument('--python_version', type=str, default="3.10", help='Python version for the conda environment (default: 3.10)')

    # Parse the project name, venv name, and optional Python version from CLI
    args = parser.parse_args()

    # Call the function to create the folder structure
    create_folder_structure(args.project_name)

    # Call the function to create the conda virtual environment
    # create_conda_venv(args.venv_name, args.python_version)