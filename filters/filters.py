import re
from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


class AddUserTheory(BaseFilter):
    async def __call__(self, message: Message) -> None | int:
        mess = message.text
        add_id = re.match(r'^\d+$', mess)
        return add_id


class AddUserPractice(BaseFilter):
    async def __call__(self, message: Message) -> None | int:
        mess = message.text
        add_id = re.match(r'^\d+_practice$', mess)
        return add_id


class AddUserPolirovka(BaseFilter):
    async def __call__(self, message: Message) -> None | int:
        mess = message.text
        add_id = re.match(r'^\d+_polirovka$', mess)
        return add_id
