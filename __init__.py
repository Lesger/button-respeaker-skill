from mycroft import MycroftSkill, intent_file_handler


class ButtonRespeaker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('respeaker.button.intent')
    def handle_respeaker_button(self, message):
        self.speak_dialog('respeaker.button')


def create_skill():
    return ButtonRespeaker()

