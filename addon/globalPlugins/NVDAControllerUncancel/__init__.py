from globalPluginHandler import GlobalPlugin
from NVDAHelper import (
    _setDllFuncPointer,
    WINFUNCTYPE,
    c_long,
    localLib,
)


@WINFUNCTYPE(c_long)
def nvdaController_cancelSpeech():
    return 0

_setDllFuncPointer(localLib, '_nvdaController_cancelSpeech', nvdaController_cancelSpeech)
