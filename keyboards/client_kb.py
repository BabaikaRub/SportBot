from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Главное меню
inline_button_try = InlineKeyboardButton(text='Пробное занятие', callback_data='try')
inline_button_direction = InlineKeyboardButton(text='Направления подготовки', callback_data='direction')
inline_button_questions = InlineKeyboardButton(text='Частые вопросы', callback_data='question')
inline_button_admin = InlineKeyboardButton(text='Позвать администратора', callback_data='admin')

inline_menu = InlineKeyboardMarkup(row_width=1)
inline_menu.add(inline_button_try).add(inline_button_direction).add(inline_button_questions).add(inline_button_admin)

# Направления подготовки
inline_button_baby = InlineKeyboardButton(text='Baby gym (малыши)', callback_data='baby')
inline_button_sport_gym = InlineKeyboardButton(text='Спортивная гимнастика', callback_data='sport_gym')
inline_button_team_gym = InlineKeyboardButton(text='Командная гимнастика', callback_data='team_gym')
inline_button_acrobatics = InlineKeyboardButton(text='Акробатика', callback_data='acrobatics')
inline_button_cheerleading = InlineKeyboardButton(text='Чирлидинг', callback_data='cheerleading')
inline_button_personal = InlineKeyboardButton(text='Персональные тренировки', callback_data='personal')

inline_direction_menu = InlineKeyboardMarkup(row_width=1)
inline_direction_menu.add(inline_button_baby).add(inline_button_sport_gym).add(inline_button_team_gym).add(inline_button_acrobatics).add(inline_button_cheerleading).add(inline_button_personal)

# Группы по спорт гимнастике
inline_button_amateur = InlineKeyboardButton(text='Для любителей', callback_data='amateur')
inline_button_professional = InlineKeyboardButton(text='Для профессионалов', callback_data='professional')

inline_gym_menu = InlineKeyboardMarkup(row_width=1)
inline_gym_menu.add(inline_button_amateur).add(inline_button_professional)

# Группы по акробатике
inline_button_children = InlineKeyboardButton(text='Для детей', callback_data='children')
inline_button_adults = InlineKeyboardButton(text='Для взрослых', callback_data='adults')

inline_acr_menu = InlineKeyboardMarkup(row_width=1)
inline_acr_menu.add(inline_button_children).add(inline_button_adults)

# Финиш ветки
inline_back = InlineKeyboardButton(text='Вернуться в главное меню', callback_data='back_menu')

inline_finish_back = InlineKeyboardMarkup(row_width=1)
inline_finish_back.add(inline_back)

