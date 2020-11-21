from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from src.functions import strip_list
from src.translate_shell import TranslateShell
from src.items import no_input_item, summary_item

class TranslateExtension(Extension):
    def __init__(self):
        super(TranslateExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()
        wikipedia.set_lang('fr')

        if len(query.strip()) == 0:
            return RenderResultListAction(no_input_item())
            
        return RenderResultListAction(summary_item(wikipedia.summary(query)))


if __name__ == '__main__':
    TranslateExtension().run()
