# Plotting

In order to produce Data/MC plots from the .coffea output file a dedicated `make_plots.py` script is implemented.

The plotting procedure is managed by several classes each targeting a specific task:

- `Shape`: for each histogram a `Shape` object is instantiated, storing all the relevant metadata and parameters.
- `SystUnc`: manages the systematic uncertainties. For each systematic uncertainty, a `SystUnc` object is instantiated. The up/down variations are stored in this object. These objects can be summed with each other to get their sum in quadrature.
- `PlotManager`: manages and stores several `Shape` objects to produce plots in all possible categories, exploiting multiprocessing.
- `SystManager`: manages several systematic uncertainties to get the total systematic uncertainty or MCstat only.

## Produce data/MC plots

Once the output `.coffea` file has been produced, plots can be generated by executing the plotting script. There are three possible way of executing it:
1. `make_plots.py`
By default, this command will read the output and configuration files from the current working directory (`./`): `output_all.coffea` is the default input file, `parameters_dump.yaml` is the default config file with all analysis parameters and `./plots` is the default output folder where the plots are saved.

2. `make_plots.py --input_dir $INPUT_DIR`
In this case, the input folder is passed as an input: `output_all.coffea`, `parameters_dump.yaml` are read from this folder and the plots are saved in the folder `$INPUT_DIR/plots`

3. `make_plots.py --input_dir $INPUT_DIR -i my_coffea_output.coffea --cfg parameters_dump.yaml -o plots_test -op plotting_style.yaml`
In this case, the default input files are overridden by providing the additional following arguments:

- `-i`: Input .coffea file with histograms.
- `--cfg`: `.yaml` file with all the analysis parameters (usually the `parameters_dump.yaml` file)
- `-o`: Output folder where the plots are saved.
- `-op`: `.yaml` file with plotting parameters to overwrite the default parameters (see details below).

Note that if `--input_dir` is not passed, the default value `./` will be assumed for the input folder.

Other optional arguments are:

- `-j`: Number of workers used for plotting
- `--only_cat`: Filter categories with a list of strings
- `--only_syst`: Filter systematics with a list of strings
- `--exclude_hist`: Exclude histograms with a list of regular expressions
- `--only_hist`: Filter histograms with a list of regular expressions
- `--split_systematics`: Split systematic uncertainties in the ratio plot
- `--partial_unc_band`: Plot only the partial uncertainty band corresponding to the systematics specified as the argument `only_syst`
- `--overwrite`: If the output folder is already existing, overwrite its content
- `--log`: Set y-axis scale to log
- `--density`: Set density parameter to have a normalized plot
- `--verbose`: Tells how much printing is done. 0 - for minimal, 2- for a lot (useful for debugging).

## Plotting parameters

The parameters of the default plotting style can be overwritten with a new config, provided with an additional argument to the script with `--overwrite_parameters plot_config.yaml` (also `-op` for short).

The structure of the additional `.yaml` config file has to be the following:
```
plotting_style:

    labels_mc:
        TTToSemiLeptonic: "$t\\bar{t}$ semilep."
        TTTo2L2Nu : "$t\\bar{t}$ dilepton"

    colors_mc:
        TTTo2L2Nu: [0.51, 0.79, 1.0]
        TTToSemiLeptonic: [1.0, 0.71, 0.24]

    samples_groups:
        ttbar:
           - TTTo2L2Nu
           - TTToSemiLeptonic

    exclude_samples:
        - TTToHadronic

    rescale_samples:
	    ttbar: 1.12
	    DY_LO: 1.33

```

User can define custom labels for the MC samples and a custom coloring scheme. Additionally, the Data and MC samples can be merged between each other by specifying a dictionary of samples in the `samples_groups` key. In the example above, a single sample `ttbar` will be plotted by merging the samples `TTTo2L2Nu` and `TTToSemiLeptonic`. Certain samples can be excluded from plotting with `exclude_samples` key.
One could also rescale certain samples by a multiplicative factor, using the `rescale_samples` keys.
