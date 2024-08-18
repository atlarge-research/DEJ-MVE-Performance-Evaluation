**Hardware dependencies**
The framework depends on the structure of DAS-5; it heavily relies on the presence of dedicated compute nodes with a shared file-system.

**Software dependencies**
The system must match the dependencies for Miniconda, Ansible, Prometheus, Jolakia, NodeJS, and Java.

**Installation**
Installation is done by cloning the GitHub repository~\cite{dilano390}, configuring the experiment using the experiment_configuration.yml file, and then running the 'run.sh' shell script on a reserved compute node.

**How to use**
Configure the experiment in the YML file, then execute the 'run' shell script on a reserved compute node. The experiment will be executed using Ansible. Ansible reserves nodes that are used for the bot simulation and the MVE server. After the experiment, results will be available in a time-stamped folder:
* The server log: The log created by the MVE server
* The configuration: A copy of the experiment configuration YML file used for the run.
* The information regarding the node: This contains information about the hardware and software on the node.
* Raw data: The raw data collected during the experiment is in a JSON file.
* Plots: The raw data turned into plots. Each plot is available in PDF and PNG format.

**Expected results**
The results heavily depend on the configuration and system used. On DAS-5, using the configuration provided in GitHub, the expectation is for the tick time to be around 22-25 ms on average. Peaks are expected to be around 35-40 at most.

**Experiment configuration**
The experiment can be customized in the experiment configuration file. This offers the following options: 
- experiment_duration_s: The period where metrics will be collected. Actual run time differs.
- server_runtime_s: The maximum length the server and monitoring programs can run. This is capped at 900 by the duration of the node reservation.
- iterations: Number of experiment iterations.
- node_count: Minimum 2, no maximum. One node will be the node that runs the MVE; the other nodes will be bot simulation nodes.
- players_per_node: The number of bots each bot simulation node simulates. Total players = (node_count - 1) * players_per_node
- bot_behavior_script: Selects the script the bot simulation nodes execute. Any script in the bot_scripts folder can be used. New behaviors can be added to this folder.
- world_name: Selects the world used during execution. Any world present in the worlds folder can be used. New worlds can be added to this folder.
- JVM_config_parameters: Contains the entire Java command executed to run the MVE. The JVM configuration can be configured here. Different MVE implementations can be used by altering the download link for the server JAR downloaded in the before.yml file. 
