import copy
import yaml
import sys
import tempfile


def main():
    config_file = sys.argv[1]

    with open(config_file, "r") as cf:
        try:
            experiment = yaml.safe_load(cf)
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit(1)

    if experiment["config"]["type"] == "one_by_one":
        res = []
        parameters = experiment["config"]["params"]
 
        l = len(configs_expanded)
        for i in range(experiment["iterations"] - 1):
            configs_expanded += copy.deepcopy(configs_expanded[:l])
        for i, c in enumerate(configs_expanded):
            iter = i // l
            c["_iteration"] = iter

        for x in configs_expanded:
            with tempfile.NamedTemporaryFile(
                mode="w+", delete=False
            ) as exp_config_file:
                res.append(exp_config_file.name)
                for k in x:
                    exp_config_file.write(f"{k}: {x[k]}\n")

        for p in res:
            print(p)


if __name__ == "__main__":
    main()
