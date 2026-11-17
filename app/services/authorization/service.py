# from app.telegram.client import client
# # from app.services.users.service import UsersService as users_service
# from app.dependencies import users_service
#
#
# class AuthorizationService:
#
#     def initialize_current_user(self):
#         telegram_user = client.get_me()
#
#         user = users_service.register_or_get(
#             telegram_id=telegram_user.id,
#             username=telegram_user.username
#         )
#
#         return user
#
#     # получаем данные из client.get_me()
#     # проверяем есть ли такой пользователь в БД (отправляем в репо слой)
#     # далее вызываем register_or_get
