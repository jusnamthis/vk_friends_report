import vk_api


class VKConnector:
    def __init__(self, token):
        self.vk = vk_api.VkApi(token=token)  # паттерн dip, теперь reader не будет зависеть от коннектора,
        # будет лишь получать соединение

