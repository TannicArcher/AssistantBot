from aiogram.dispatcher.filters.state import State, StatesGroup


class CutterLink(StatesGroup):
	link = State()


class ScreenSite(StatesGroup):
	link = State()

class SearchIp(StatesGroup):
	ip = State()


class ParserGroup(StatesGroup):
	chat = State()



