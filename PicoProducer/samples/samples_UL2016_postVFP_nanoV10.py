from TauFW.PicoProducer.storage.Sample import MC as M
from TauFW.PicoProducer.storage.Sample import Data as D
storage  = "/eos/cms/store/group/phys_tau/TauFW/nanoV10/Run2_2016/$DAS"
url      = "root://cms-xrd-global.cern.ch/" #None #"root://eosuser.cern.ch/"
filelist = None 
samples  = [
  
  # DRELL-YAN
  M('DY','DYJetsToLL_M-50',
    "/DYJetsToLL_M-50-madgraphMLM",
    #"/DYJetsToLL_M-50-madgraphMLM_ext1",
    store=storage,url=url,files=filelist,opts="useT1=False,zpt=True"),
  M('DY','DYJetsToLL_M-10to50',
    "/DYJetsToLL_M-10to50-madgraphMLM",
    store=storage,url=url,files=filelist,opts="useT1=False,zpt=True"),
  M('DY','DY1JetsToLL_M-50',
    "/DY1JetsToLL_M-50-madgraphMLM",
    store=storage,url=url,files=filelist,opts="useT1=False,zpt=True"),
  M('DY','DY2JetsToLL_M-50',
    "/DY2JetsToLL_M-50-madgraphMLM",
    store=storage,url=url,files=filelist,opts="useT1=False,zpt=True"),
  M('DY','DY3JetsToLL_M-50',
    "/DY3JetsToLL_M-50-madgraphMLM",
    store=storage,url=url,files=filelist,opts="useT1=False,zpt=True"),
  M('DY','DY4JetsToLL_M-50',
    "/DY4JetsToLL_M-50-madgraphMLM",
    store=storage,url=url,files=filelist,opts="useT1=False,zpt=True"),
  
  # TTBAR
  M('TT','TTTo2L2Nu',
    "/TTTo2L2Nu",
    store=storage,url=url,files=filelist,opts="useT1=False,toppt=True"),
  M('TT','TTToSemiLeptonic',
    "/TTToSemiLeptonic",
    store=storage,url=url,files=filelist,opts="useT1=False,toppt=True"),
  M('TT','TTToHadronic',
    "/TTToHadronic",
    store=storage,url=url,files=filelist,opts="useT1=False,toppt=True"),
  
  # W+JETS
  M('WJ','WJetsToLNu',
    "/WJetsToLNu",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('WJ','W1JetsToLNu',
    "/W1JetsToLNu",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('WJ','W2JetsToLNu',
    "/W2JetsToLNu",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('WJ','W3JetsToLNu',
    "/W3JetsToLNu",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('WJ','W4JetsToLNu',
    "/W4JetsToLNu", 
    store=storage,url=url,files=filelist,opts="useT1=False"),
  
  # SINGLE TOP
  M('ST','ST_tW_antitop',
    "/ST_tW_antitop_5f_NoFullyHadronicDecays",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('ST','ST_tW_top',
    "/ST_tW_top_5f_NoFullyHadronicDecays",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('ST','ST_t-channel_antitop',
    "/ST_t-channel_antitop_4f_InclusiveDecays", 
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('ST','ST_t-channel_top',
    "/ST_t-channel_top_4f_InclusiveDecays", 
    store=storage,url=url,files=filelist,opts="useT1=False"),
  
  # DIBOSON
  M('VV','WWTo1L1Nu2Q',
    "/WWTo1L1Nu2Q",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('VV','WWTo2L2Nu',
    "/WWTo2L2Nu",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('VV','WWTo4Q',
    "/WWTo4Q",
    store=storage,url=url,files=filelist,opts="useT1=False"),

  M('VV','WZTo1L1Nu2Q',
    "/WZTo1L1Nu2Q",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('VV','WZTo2Q2L',
    "/WZTo2Q2L",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('VV','WZTo3LNu',
    "/WZTo3LNu",
    store=storage,url=url,files=filelist,opts="useT1=False"),

  M('VV','ZZTo2L2Nu',
    "/ZZTo2L2Nu",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('VV','ZZTo2Q2L',
    "/ZZTo2Q2L",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('VV','ZZTo2Q2Nu',
    "/ZZTo2Q2Nu",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('VV','ZZTo4L',
    "/ZZTo4L",
    store=storage,url=url,files=filelist,opts="useT1=False"),
  M('VV','ZZTo4Q',
    "/ZZTo4Q",
    store=storage,url=url,files=filelist,opts="useT1=False"),

  # SINGLE MUON
  D('Data','SingleMuon_Run2016F',"/SingleMuon_Run2016F",
   store=storage,url=url,files=filelist,opts="useT1=False",channels=["skim*",'mutau','mumu','emu']),
  D('Data','SingleMuon_Run2016G',"/SingleMuon_Run2016G",
    store=storage,url=url,files=filelist,opts="useT1=False",channels=["skim*",'mutau','mumu','emu']),
  D('Data','SingleMuon_Run2016H',"/SingleMuon_Run2016H",
   store=storage,url=url,files=filelist,opts="useT1=False",channels=["skim*",'mutau','mumu','emu']),
 
  # SINGLE ELECTRON
  D('Data','SingleElectron_Run2016F',"/SingleElectron_Run2016F",
    store=storage,url=url,files=filelist,opts="useT1=False",channels=["skim*",'etau','ee']),
  D('Data','SingleElectron_Run2016G',"/SingleElectron_Run2016G",
    store=storage,url=url,files=filelist,opts="useT1=False",channels=["skim*",'etau','ee']),
  D('Data','SingleElectron_Run2016H',"/SingleElectron_Run2016H",
    store=storage,url=url,files=filelist,opts="useT1=False",channels=["skim*",'etau','ee']),

  # TAU
  D('Data','Tau_Run2016F',"/Tau_Run2016F",
    store=storage,url=url,files=filelist,opts="useT1=False",channels=["skim*",'tautau']),
  D('Data','Tau_Run2016G',"/Tau_Run2016G",
    store=storage,url=url,files=filelist,opts="useT1=False",channels=["skim*",'tautau']),
  D('Data','Tau_Run2016H',"/Tau_Run2016H",
    store=storage,url=url,files=filelist,opts="useT1=False",channels=["skim*",'tautau']),

]
