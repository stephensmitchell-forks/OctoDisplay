# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class OctoDisplayPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World! - OctoDisplay")
