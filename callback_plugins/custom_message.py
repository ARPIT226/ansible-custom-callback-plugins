""" from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'custom_message'

    def v2_playbook_on_start(self, playbook):
        self._display.banner("Playbook is starting...!")

    def v2_playbook_on_stats(self, stats):
        self._display.banner("Playbook has completed successfully.") """


from ansible.plugins.callback import CallbackBase
from datetime import datetime 
class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'custom_callback'

    def v2_playbook_on_start(self, playbook):
        start_time = datetime.now()
        self._display.display("My Playbook is starting... at %s" % start_time)

    def v2_playbook_on_stats(self, stats):
        end_time = datetime.now()
        self._display.display("My Playbook is finished... at %s" % end_time)
