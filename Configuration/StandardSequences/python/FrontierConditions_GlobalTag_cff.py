import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.FrontierConditions_GlobalTag_cfi import *

# the following is needed for non PoolDBESSources (fake calibrations)
#
from CalibCalorimetry.EcalLaserCorrection.ecalLaserCorrectionService_cfi import *
from CalibTracker.Configuration.Tracker_DependentRecords_forGlobalTag_cff import *
es_prefer_GlobalTag = cms.ESPrefer("PoolDBESSource","GlobalTag")

hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)

es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    toGet = cms.untracked.vstring('GainWidths', 
        'channelQuality', 
        'ZSThresholds')
)
