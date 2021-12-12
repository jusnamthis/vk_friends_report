import vk_api


class VKFriendsError(Exception):
    pass


class VKAuthError(Exception):
    pass


class VKReader:
    def __init__(self, vk, user_id):
        try:
            self.friends = vk.method("friends.get",
                                     {"user_id": user_id,
                                      "order": "name",
                                      "fields": "nickname,country,city,bdate,sex"})
        except vk_api.exceptions.ApiError as api_err:
            # не знаю насколько это адекватно: внедрять такую логику в этом блоке
            if api_err.code == 5:
                raise VKAuthError("Неверный токен, обратитесь к инструкции.")
            elif api_err.code == 100:
                raise VKFriendsError("Ошибка ввода, обратитесь к инструкции.")
            elif api_err.code == 30:
                raise VKFriendsError("Пользователь скрыл свои данные.")

    def browse_friends(self):
        for friend in self.friends['items']:
            yield friend
