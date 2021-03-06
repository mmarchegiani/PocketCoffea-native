from PocketCoffea.parameters.cuts.baseline_cuts import dilepton_presel, passthrough
from PocketCoffea.workflows.pileup_variations import pileupVariationsProcessor

cfg =  {

    "dataset" : {
        "jsons": ["datasets/RunIISummer20UL18_local.json"],
        "filter" : {
            "samples": ["ttHTobb", "TTTo2L2Nu"],
            "samples_exclude" : [],
            "year": ["2018"]
        }
    },

    # Input and output files
    "workflow" : pileupVariationsProcessor,
    "output"   : "output/pileup/test_pileup_variations",

    # Executor parameters
    "run_options" : {
        "executor"       : "futures",
        "workers"        : 12,
        "scaleout"       : 10,
        "partition"      : "standard",
        "walltime"       : "12:00:00",
        "mem_per_worker" : None, # GB
        "exclusive"      : True,
        "chunk"          : 50000,
        "max"            : None,
        "skipbadfiles"   : None,
        "voms"           : None,
        "limit"          : 4,
    },

    # Cuts and plots settings
    "finalstate" : "dilepton",
    "preselections" : [dilepton_presel],
    "categories": {
        "SR" : [passthrough],
        "CR" : [passthrough]
    },
    
    "variables" : {
        "muon_pt" : {'binning' : {'n_or_arr' : 200, 'lo' : 0, 'hi' : 2000}, 'xlim' : (0,500),  'xlabel' : "$p_{T}^{\mu}$ [GeV]"},
        "muon_eta" : None,
        "muon_phi" : None,
        "electron_pt" : None,
        "electron_eta" : None,
        "electron_phi" : None,
        "jet_pt" : None,
        "jet_eta" : None,
        "jet_phi" : None,
        "nmuon" : None,
        "nelectron" : None,
        "nlep" : None,
        "nmuon" : None,
        "nelectron" : None,
        "nlep" : None,
        "njet" : None,
        "nbjet" : None,
    },
    "variables2d" : {},
    "scale" : "log"
}
