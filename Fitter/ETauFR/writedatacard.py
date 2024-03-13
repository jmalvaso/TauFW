#! /usr/bin/env python
# Authors: Andrea Cardini, Lorenzo Vigilante and Yiwen Wen (Feb 2021) edited by Paola Mastrapasqua
# Description: Create datacards for combine
import sys
from CombineHarvester.CombineTools import ch
import os
import ROOT as R
from ROOT import RooWorkspace, TFile, RooRealVar
import CombineHarvester.CombinePdfs.morphing as morphing
from CombineHarvester.CombinePdfs.morphing import BuildRooMorphing
from CombineHarvester.CombinePdfs.morphing import BuildCMSHistFuncFactory
import math
import json

def ensureDirectory(dirname):
    """Make directory if it does not exist."""
    if not os.path.exists(dirname):
      os.makedirs(dirname)
      print ">>> made directory " + dirname
    return dirname

##Def of eta regions, dm bins, VSele WPs 
eta = ['0to1p46','1p56to2p5']
dms = [0,1,10,11]
wp = ['VVLoose','Tight']

#### IMPORTANT: change era HERE #####
era='2022_postEE'

tag=''

### IMPORTANT: True = combined fit with FES templates, False = simple fit for FR SF only #####
fesVar=True

dict_prefitFR = {}
for iwp in wp:
    dict_prefitFR[iwp]={}
    for ieta in eta:
        dict_prefitFR[iwp][ieta]={}
        for idm in dms:
            dict_prefitFR[iwp][ieta][str(idm)]={}

#print(dict_prefitFR)

for ieta in eta :
   print('<<<<<<< eta range: ', ieta)
   for idm in dms:
      print('<<<<<<< dm range: ',  idm)
      for iwp in wp :
          print('<<<<<<<<<<<<<< working point: ', iwp)
          cb = ch.CombineHarvester()
          #cb.SetFlag('workspaces-use-clone', True)
          mc_backgrounds = ['ZTT','ZJ','W','VV','ST','TTT','TTL','TTJ']
          data_driven_backgrounds = ['QCD']
          backgrounds = mc_backgrounds + data_driven_backgrounds
          signals = ['ZL']

          categories = {

              'et' : [( 1, '%s_pass'%(iwp) ) ,( 2, '%s_fail'%(iwp) )],
          }

         
          cb.AddObservations(['*'], ['ETauFR'], ['%s'%(era)], ['et'],              categories['et']) # adding observed data
          cb.AddProcesses(   ['*'], ['ETauFR'], ['%s'%(era)], ['et'], backgrounds, categories['et'], False) # adding backgrounds

          if fesVar:
            ##FESvariation!!!
            variation = [0.75,0.80,0.85,0.90,0.95,1.00,1.05,1.10,1.15,1.20,1.25]
            fesshifts = ["%.2f"%fes for fes in variation ]
            print(fesshifts)
            cb.AddProcesses(fesshifts, ['ETauFR'], ['%s'%(era)], ['et'], signals, categories['et'], True)
          else: 
            cb.AddProcesses(   ['90'], ['ETauFR'], ['%s'%(era)], ['et'], signals, categories['et'], True) # adding signals

          cb.cp().process(mc_backgrounds+signals).AddSyst(cb,'lumi_%s'%(era), 'lnN', ch.SystMap()(1.05)) 
          cb.cp().process(['TTT','TTL','TTJ','ST']).AddSyst(cb, 'xsec_top', 'lnN', ch.SystMap()(1.10))
          cb.cp().process(['VV']).AddSyst(cb, 'normalizationVV', 'lnN', ch.SystMap()(1.10))
          cb.cp().process(['ZL','ZTT','ZJ']).AddSyst(cb, 'normalizationDY', 'lnN', ch.SystMap()(1.10))
          cb.cp().process(['W']).AddSyst(cb, 'normalizationW', 'lnN', ch.SystMap()(1.20))
          cb.cp().process(['ZJ','TTJ']).AddSyst(cb, 'jet_to_tauFR', 'lnN', ch.SystMap()(1.20))
          cb.cp().process(['QCD']).AddSyst(cb, 'normalizationQCD', 'lnN', ch.SystMap()(1.20))
          cb.cp().process(mc_backgrounds+signals).AddSyst(cb, 'CMS_eff_e', 'lnN', ch.SystMap()(1.10))
          #cb.cp().process(['ZTT','VV','ST','TTT','TTL','TTJ']).AddSyst(cb, 'CMS_eff_t', 'lnN', ch.SystMap()(1.05))
          
          cb.cp().process(['ZTT']).AddSyst(cb, 'shape_tes', 'shape', ch.SystMap()(1.0))
          if not fesVar: #if not performing combined fit, FES is taken as shape syst in the FR fit 
             cb.cp().process(['ZL']).AddSyst(cb, 'shape_fes', 'shapeU', ch.SystMap()(1.0))
          #cb.cp().process(mc_backgrounds+signals).AddSyst(cb, 'shape_ees', 'shape', ch.SystMap()(1.0))
          #['ZTT','ZJ','W','VV','ST','TTT','TTL']
          cb.cp().process(['ZTT','ZJ','W','VV','ST','TTT','TTL']+signals).AddSyst(cb, 'shape_ees', 'shape', ch.SystMap()(1.0))
          cb.cp().process(['ZL']).AddSyst(cb, 'shape_res', 'shape', ch.SystMap()(1.0))
         
          filepath = os.path.join(os.environ['PWD'],'input', "zee_fr_m_vis_eta%s_dm%s_et-%s%s.inputs.root")%(ieta,str(idm),era,tag)
          processName = '$BIN/$PROCESS'
          systematicName = '$BIN/$PROCESS_$SYSTEMATIC'
          if fesVar:  
            processName_FES = '$BIN/$PROCESS_FES$MASS'
            systematicName_FES = "$BIN/$PROCESS_FES$MASS_$SYSTEMATIC"
          else:
            processName_FES = processName
            systematicName_FES = systematicName
          cb.cp().backgrounds().ExtractShapes(filepath, processName, systematicName)
          cb.cp().signals().ExtractShapes(filepath, processName_FES, systematicName_FES)
          ch.SetStandardBinNames(cb, '$BIN') # Define the name of the category names
         


##############################################################################################################
#Save pre-fit FR in a dict

          fakeratePrefit = cb.cp().bin(['%s_pass'%(iwp)]).process(['ZL']).GetRate() / ((cb.cp().bin(['%s_pass'%(iwp)]).process(['ZL']).GetRate()+cb.cp().bin(['%s_fail'%(iwp)]).process(['ZL']).GetRate()))

          sigRatePassPre = cb.cp().bin(['%s_pass'%(iwp)]).process(['ZL']).GetRate()
          sigRateFailPre = cb.cp().bin(['%s_fail'%(iwp)]).process(['ZL']).GetRate()
          sigErrPassPre = cb.cp().bin(['%s_pass'%(iwp)]).process(['ZL']).GetUncertainty()
          sigErrFailPre = cb.cp().bin(['%s_fail'%(iwp)]).process(['ZL']).GetUncertainty()

          dfdxPre = sigRateFailPre /((sigRatePassPre+sigRateFailPre)*(sigRatePassPre+sigRateFailPre))
          dfdyPre = -sigRatePassPre / ((sigRatePassPre+sigRateFailPre)*(sigRatePassPre+sigRateFailPre))
          errfakeratePrefit = math.sqrt((dfdxPre*sigErrPassPre)*(dfdxPre*sigErrPassPre)+(dfdyPre*sigErrFailPre)*(dfdyPre*sigErrFailPre))

          dict_prefitFR[iwp][ieta][str(idm)]["prefitFR"] = fakeratePrefit
          dict_prefitFR[iwp][ieta][str(idm)]["prefitFRErr"] = errfakeratePrefit         
##############################################################################################################
          if fesVar: 
            bins = cb.bin_set()
            workspace = RooWorkspace("ETauFR","ETauFR") 
            pois = []
            fesname = "fes"
            fes = RooRealVar(fesname,fesname, min(variation), max(variation))
            fes.setConstant(True)
            #print(min(variation))
            #print(max(variation))

            ## MORPHING
            print(">>> morphing...")
            BuildCMSHistFuncFactory(workspace, cb, fes, "ZL")
            # EXTRACT PDFs
            #print(">>> add workspace and extract pdf...")
            cb.AddWorkspace(workspace, False)
            cb.ExtractPdfs(cb, "ETauFR", "$BIN_$PROCESS_morph", "")  # Extract all processes (signal and bkg are named the same way)
            cb.ExtractData("ETauFR", "$BIN_data_obs")  # Extract the RooDataHist
            cb.SetAutoMCStats(cb, 0, 1, 1)
 
          #print(">>> cardwriter..")
          datacardPath = 'input/%s/ETauFR/%s_eta%s_dm%s.txt'%(era,iwp,ieta,str(idm))
          shapePath = 'input/%s/ETauFR/common/%s_eta%s_dm%s.root'%(era,iwp,ieta,str(idm))
          writer = ch.CardWriter(datacardPath,shapePath)
          writer.SetWildcardMasses([])
          writer.WriteCards('cmb', cb) # writing all datacards into one folder for combination
          
          #cb.PrintAll()
          #print("\033[1;32;40m >>> print observation \n")
          #print("\033[0;37;40m \n") 
          #cb.PrintObs()
          #print("\033[1;32;40m >>> print processes \n")
          #print("\033[0;37;40m \n")
          #cb.PrintProcs()
          #print("\033[1;32;40m >>> print systematics \n")
          #print("\033[0;37;40m \n")
          #cb.PrintSysts()
          #print("\033[1;32;40m >>> print parameters \n")
          #print("\033[0;37;40m \n")
          #cb.PrintParams()
          #print "\n"
          #print("Done writing")
          
          ##adding rateParam
          with open('input/%s/ETauFR/%s_eta%s_dm%s.txt'%(era,iwp,ieta,str(idm)),'a') as f:
               f.write("normalizationZEE rateParam * ZL 1.000 [0.0,10.0]\n")
               f.write("vsjetsf rateParam * ZTT 1.000 [0.0,10.0]\n")
               f.write(" ")
               print '>> Done!'


          print 'pre-fit fake rate:'
          print fakeratePrefit
          print 'pre-fit fake rate errors:'
          print errfakeratePrefit

#Save pre-fit FR dict in a json
with open("input/%s/ETauFR/prefitFR.json"%(era), "w") as outfile:
    json.dump(dict_prefitFR, outfile, indent=6)
