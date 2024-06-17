if ! which conda; then
    read -r -p "Conda not found. About to install conda in /var/scratch/$(whoami)/miniconda3. Do you want to continue? [yn] " yn
    case $yn in
    [Yy])
        mkdir -p ~/miniconda3
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
        bash ~/miniconda3/miniconda.sh -b -u -p "/var/scratch/$(whoami)/miniconda3"
        rm -rf ~/miniconda3/miniconda.sh
        set +u
        source "/var/scratch/$(whoami)/miniconda3/bin/activate"
        conda init bash
        set -u
        ;;
    *)
        exit
        ;;
    esac
fi

env_name="$(head -n 1 environment.yml | cut -d':' -f 2 | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"

if ! conda env list | grep -q -E "^$env_name\s+"; then
    read -r -p "Conda environment not found. About to create an environment with name '$env_name'. Do you want to continue? [yn] " yn
    case $yn in
    [Yy])
        conda env create --file environment.yml
        ;;
    *)
        exit
        ;;
    esac
fi

set +u
set +x
eval "$(conda shell.bash hook)"
conda activate "$env_name"
set -x
set -u

if ! conda compare environment.yml; then
    conda env create -q --file environment.yml --force
fi
conda init bash

ansible-playbook -e @experiment_configuration.yml -i 'localhost' before.yml

set +x
iterations=$(python3 -u -c '
import yaml
import datetime

curr_time = (datetime.datetime.now().strftime("%H:%M))

try:
    with open("experiment_configuration.yml", "r") as file:
        yaml_data = yaml.safe_load(file)

    yaml_data["timestamp"] = curr_time

    with open("experiment_configuration.yml", "w") as file:
        yaml.safe_dump(yaml_data, file)

    print(yaml_data["iterations"])
except FileNotFoundError:
    print("File experiment_configuration.yml not found.")
    exit(1)
except KeyError:
    print("Key iterations not found in the YAML file.")
    exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)
')

echo $iterations

set -x

for num  in $(seq 1 $iterations); do
    ansible-playbook  -e @experiment_configuration.yml -i 'localhost' run_all.yml
done