import time
import appModuleHandler
from NVDAObjects.IAccessible import IAccessible
import textInfos
import ui
from keyboardHandler import KeyboardInputGesture
from logHandler import log
import speech
import api

class AppModule(appModuleHandler.AppModule):

	def script_speakDebugLine(self, gesture):
		gesture.send()
		time.sleep(.025)
		new = api.getFocusObject().makeTextInfo(textInfos.POSITION_CARET)
		new.move(textInfos.UNIT_LINE, 0, endPoint = "start")
		new.expand(textInfos.UNIT_LINE)
		log.info(new.text)
		speech.speakMessage(new.text)


	__gestures={
		"kb:F6":"speakDebugLine",
		"kb:F5":"speakDebugLine",
		"kb:F7":"speakDebugLine",
		"kb:F8":"speakDebugLine"
	}