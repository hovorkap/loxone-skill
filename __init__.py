from mycroft import MycroftSkill, intent_file_handler


class Loxone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('loxone.intent')
    def handle_loxone(self, message):
        self.speak_dialog('loxone')


def create_skill():
    return Loxone()

