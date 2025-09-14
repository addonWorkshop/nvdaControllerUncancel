import buildVersion
from globalPluginHandler import GlobalPlugin
from NVDAHelper import (
    WINFUNCTYPE,
    _setDllFuncPointer,
    c_long,
    localLib,
)


@WINFUNCTYPE(c_long)
def nvdaController_cancelSpeech():
    return 0


if buildVersion.version_year < 2026:
    _setDllFuncPointer(
        localLib, "_nvdaController_cancelSpeech", nvdaController_cancelSpeech
    )
else:
    _setDllFuncPointer(
        localLib.dll, "_nvdaController_cancelSpeech", nvdaController_cancelSpeech
    )
