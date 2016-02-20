# -*- coding: utf-8 -*-
import zope.publisher.browser

import json


class Service(zope.publisher.browser.BrowserPage):

    stream = False

    def __call__(self):
        result = self.render()
        if not self.stream:
            self.request.response.setHeader("Content-Type", "application/json")
            return json.dumps(result, indent=2, sort_keys=True)
        else:
            return result
