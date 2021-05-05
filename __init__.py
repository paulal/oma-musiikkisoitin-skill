from mycroft import MycroftSkill, intent_file_handler


class OmaMusiikkisoitin(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('musiikkisoitin.oma.intent')
    def handle_musiikkisoitin_oma(self, message):
        self.speak_dialog('musiikkisoitin.oma')


def create_skill():
    return OmaMusiikkisoitin()

