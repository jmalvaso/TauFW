# TauFW

Framework for tau analysis using NanoAOD at CMS. Three main packages are
1. [`PicoProducer`](PicoProducer): Tools to process nanoAOD and make custom analysis ntuples.
2. [`Plotter`](Plotter): Tools for further analysis, auxiliary measurements, validation and plotting.
3. [`Fitter`](Fitter): Tools for measurements and fits in combine. [Under development.]

## Installation

### Table of Contents  
* [CMSSW environment](#CMSSW-environment)<br>
* [TauFW](#TauFW-1)<br>
* [PicoProducer](#PicoProducer)<br>
* [Combine](#Combine)<br>
* [TauID](#TauPOG-corrections)<br>

### CMSSW environment
First, setup a CMSSW release, for example,
```
export CMSSW=CMSSW_11_3_4
export SCRAM_ARCH=slc7_amd64_gcc900
cmsrel $CMSSW
cd $CMSSW/src
cmsenv
```
Which CMSSW release should not really matter for post-processing of nanoAOD,
but if you like to use `combine` in the same repository, it is better to use at least the
[recommended release for the latest Combine version](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/#setting-up-the-environment-and-installation),
see below.

### TauFW
To install `TauFW`:
```
cd $CMSSW_BASE/src/
git clone https://github.com/cms-tau-pog/TauFW TauFW
scram b -j4
```
With each new session, do
```
export SCRAM_ARCH=slc7_amd64_gcc900
cd $CMSSW/src
cmsenv
```

### PicoProducer
If you want to process nanoAOD using `PicoProducer`, install [`NanoAODTools`](https://github.com/cms-nanoAOD/nanoAOD-tools):
```
cd $CMSSW_BASE/src/
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
scram b -j4
```
If you want to use tau ID SF, please install [`TauIDSFs` tool](https://github.com/cms-tau-pog/TauIDSFs):
```
cd $CMSSW_BASE/src
git clone https://github.com/cms-tau-pog/TauIDSFs TauPOG/TauIDSFs
cmsenv
scram b -j4
```

### Combine
If you want to use the `combine` tools in `Fitter`, install combine following the
[latest instructions](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/#setting-up-the-environment-and-installation),
for example
```
cd $CMSSW_BASE/src
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
git fetch origin
git checkout v8.1.0 # for CMSSW_10_X
git checkout v9.1.0 # for CMSSW_11_X
```
and then [`CombineHarvester`](https://github.com/cms-analysis/CombineHarvester),
```
cd $CMSSW_BASE/src
git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester
scramv1 b clean; scramv1 b
git checkout v2.0.0 # for CMSSW_11_X only
```

### TauPOG corrections
For TauPOG-internal work: To create JSON files with TauPOG corrections for
[`correctionlib`](https://github.com/cms-nanoAOD/correctionlib),
please follow the instructions
[here](https://gitlab.cern.ch/cms-tau-pog/jsonpog-integration/-/blob/TauPOG_v2/POG/TAU/README4UPDATES.md).
From at least `CMSSW_11_3_X`, `correctionlib` should be pre-installed.

To create ROOT files including the measured SFs please install [`TauIDSFs` tool](https://github.com/cms-tau-pog/TauIDSFs).
Modify the `TauIDSFs/utils/createSFFiles.py` script to include your measured SFs into the script. 
Finally, run the `TauFW/scripts/tau_createROOT.sh` to generate your ROOT files. They will be created into `TauFW/scripts/data/`
IMPORTANT: please comment and do not delete older SFs
