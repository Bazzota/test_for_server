from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards import inline_kb
from database import database_func
router = Router()


@router.message(CommandStart())
async def process_start(message: Message):
    await message.answer(text='start', reply_markup=inline_kb.kb.as_markup())


@router.callback_query(F.data == 'one')
async def process_one(callback: CallbackQuery):
    database_func.add_entry(link='database/base.db', name=callback.from_user.first_name, old=10)
    await callback.message.answer(text='this is one')


@router.callback_query(F.data == 'two')
async def process_two(callback: CallbackQuery):
    data = database_func.select_entry(link='database/base.db', id=1)
    print(data)
    await callback.message.answer(text=data[0][0])


@router.callback_query(F.data == 'three')
async def process_one(callback: CallbackQuery):
    await callback.message.answer(text='this is three')