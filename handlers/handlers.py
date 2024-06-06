from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards import inline_kb
router = Router()


@router.message(CommandStart())
async def process_start(message: Message):
    await message.answer(text='start', reply_markup=inline_kb.kb.as_markup())


@router.callback_query(F.data == 'one')
async def process_one(callback: CallbackQuery):
    await callback.message.answer(text='this is one')


@router.callback_query(F.data == 'two')
async def process_two(callback: CallbackQuery):
    await callback.message.answer(text='this is two')


@router.callback_query(F.data == 'three')
async def process_one(callback: CallbackQuery):
    await callback.message.answer(text='this is three')