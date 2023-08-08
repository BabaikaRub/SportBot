from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import dp, bot
from keyboards import inline_menu, inline_direction_menu, inline_finish_back, inline_gym_menu
from keyboards import inline_acr_menu
from handlers.messages import greeting, first_try, question, menu_message, gym_group, baby, amateur, professional
from handlers.messages import team_gym, acrobatics_choice, children, adults, cheerleading, personal, feedback


class FSMClient(StatesGroup):
    feedback = State()


# Общие функции и глобальные команды
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, greeting, reply_markup=inline_menu)


@dp.callback_query_handler(text='back_menu')
async def show_menu(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, '📋 Главное меню:', reply_markup=inline_menu)
        await message.answer()
    except TypeError:
        pass


# Направления подготвки
@dp.callback_query_handler(text='direction')
async def show_directions(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, menu_message, reply_markup=inline_direction_menu)
    await callback.answer()


@dp.callback_query_handler(text='baby')
async def show_baby(callback: types.CallbackQuery):
    photo = open('media/baby.jpeg', 'rb')

    await bot.send_message(callback.from_user.id, baby)
    await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=inline_finish_back)
    await callback.answer()


# Развилка для групп по спорт гимнастике
@dp.callback_query_handler(text='sport_gym')
async def show_gym_group(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, gym_group, reply_markup=inline_gym_menu)
    await callback.answer()


@dp.callback_query_handler(text='amateur')
async def show_amateur(callback: types.CallbackQuery):
    photo = open('media/amateur.jpg', 'rb')

    await bot.send_message(callback.from_user.id, amateur)
    await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=inline_finish_back)
    await callback.answer()


@dp.callback_query_handler(text='professional')
async def show_professional(callback: types.CallbackQuery):
    photo = open('media/professional.jpg', 'rb')

    await bot.send_message(callback.from_user.id, professional)
    await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=inline_finish_back)
    await callback.answer()


@dp.callback_query_handler(text='team_gym')
async def show_team_gym(callback: types.CallbackQuery):
    photo = open('media/team.jpg', 'rb')

    await bot.send_message(callback.from_user.id, team_gym)
    await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=inline_finish_back)
    await callback.answer()


# Развилка для групп по акробатике
@dp.callback_query_handler(text='acrobatics')
async def show_gym_acrobatics(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, acrobatics_choice, reply_markup=inline_acr_menu)
    await callback.answer()


@dp.callback_query_handler(text='children')
async def show_children(callback: types.CallbackQuery):
    photo = open('media/children.jpg', 'rb')

    await bot.send_message(callback.from_user.id, children)
    await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=inline_finish_back)
    await callback.answer()


@dp.callback_query_handler(text='adults')
async def show_adults(callback: types.CallbackQuery):
    photo = open('media/adults.jpg', 'rb')

    await bot.send_message(callback.from_user.id, adults)
    await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=inline_finish_back)
    await callback.answer()


@dp.callback_query_handler(text='cheerleading')
async def show_cheerleading(callback: types.CallbackQuery):
    photo = open('media/cheerleading.jpg', 'rb')

    await bot.send_message(callback.from_user.id, cheerleading)
    await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=inline_finish_back)
    await callback.answer()


@dp.callback_query_handler(text='personal')
async def show_personal(callback: types.CallbackQuery):
    photo = open('media/personal.jpg', 'rb')

    await bot.send_message(callback.from_user.id, personal)
    await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=inline_finish_back)
    await callback.answer()


# Короткие ветки
@dp.callback_query_handler(text='try')
async def show_try(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, first_try, reply_markup=inline_finish_back)
    await callback.answer()


@dp.callback_query_handler(text='question')
async def show_question(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, question, reply_markup=inline_finish_back)
    await callback.answer()


# Связь с администратором
@dp.callback_query_handler(text='admin', state=None)
async def show_feedback(callback: types.CallbackQuery):

    await bot.send_message(callback.from_user.id, feedback)

    await FSMClient.feedback.set()


@dp.message_handler(state=FSMClient.feedback)
async def get_feedback(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        msg = message.text

    await bot.send_message(998820262, f'Пользователь с id {message.from_user.id} оставил номер телефона для связи: {msg}')
    await bot.send_message(message.from_user.id, '✅ Информация передана администратору чата!', reply_markup=inline_finish_back)

    await state.finish()


# Регистрация команд
def registration_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(show_menu, commands=['menu'])
