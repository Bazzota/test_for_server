from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from lexicon import lexicon_ru



buttons = [InlineKeyboardButton(text=text, callback_data=callback) for text, callback in lexicon_ru.start_commands.items()]

kb = InlineKeyboardBuilder()
kb.row(*buttons, width=1)