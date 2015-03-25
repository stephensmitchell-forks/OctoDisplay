# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class OctoDisplayPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.EventHandlerPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World! - OctoDisplay")

    def on_event(self, event, payload):
        #if event == "PrintStarted":
        if event == "Connected":
            self._logger.info("OctoDisplay - Printer Connected")
            self._logger.info(payload['port'])






__plugin_implementations__ = [OctoDisplayPlugin()]
