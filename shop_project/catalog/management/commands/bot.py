import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import Router, F
from django.core.management import BaseCommand
from django.conf import settings
import asyncio
from asgiref.sync import sync_to_async
from catalog.models import Category, Seller
from aiohttp import ClientSession
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class SomeState(StatesGroup):/
    waiting_for_login = State()
    waiting_for_password = State()
    waiting_for_name_product = State()
    waiting_for_count_product = State()

bot = Bot(token=settings.TELEGRAM_API)
storage = MemoryStorage
router = Router()
dp = Dispatcher(stage= storage)

button_categories = KeyboardButton(text='Show categories')
button_sellers = KeyboardButton(text='Show sellers')
button_show_cart = KeyboardButton(text='Show cart')
button_add_to_cart = KeyboardButton(text='Add to cart')
keyword = ReplyKeyboardMarkup(
    keyboard=[[button_categories], [button_sellers], [button_show_cart], [button_add_to_cart], ],
    resize_keyboard=True,
    one_time_keyboard=False
)



@sync_to_async()
def get_categories():
    return list(Category.objects.all())


async def fetch_user_cart(login, password):
    cart_url =settings.CART_URL
    auth_url = settings.USERS_AUTH

    async with aiohttp.ClientSession() as session:
        auth_data = {"email": login, "password": password}
        async with session.post(auth_url, json=auth_data) as auth_response:
            if auth_response.status == 200:
                auth_content = await auth_response.json()
                token = auth_content.get('access')

                headers = {"Authorization": f"Bearer {token}"}
                async with session.get(cart_url, headers=headers) as cart_response:
                    cart_content = await cart_response.json()
                    return cart_content
            else:
                return None


async def fetch_user_add_product(login, password):
    product_url =settings.PRODUCT_URL
    auth_url = settings.USERS_AUTH

    async with aiohttp.ClientSession() as session:
        auth_data = {"email": login, "password": password}
        async with session.post(auth_url, json=auth_data) as auth_response:
            if auth_response.status == 200:
                auth_content = await auth_response.json()
                token = auth_content.get('access')

                headers = {"Authorization": f"Bearer {token}"}
                async with session.get(product_url, headers=headers) as cart_response:
                    cart_content = await cart_response.json()
                    return cart_content
            else:
                return None


@router.message(F.text == "/start")
async def command_start(message: types.Message):
    await message.answer('Hello', reply_markup=keyword)


@router.message(F.text == "Show categories")
async def show_categories(message: types.Message):
    categories = await get_categories()
    msg_to_answer = ''
    for category in categories:
        msg_to_answer += (f"Category: {category.name}\n"
                         f"Description: {category.description}\n"
                         f"___________________________________\n")
    await bot.send_message(message.chat.id, msg_to_answer)


@router.message(F.text == "Show sellers")
async def get_sellers(message: types.Message):
    async with ClientSession() as session:
        async with session.get(settings.SELLERS_URL) as response:
            sellers = await response.json()
    msg_to_answer = ''
    for seller in sellers:
        msg_to_answer += (f"Seller: {seller['name']}\n"
                         f"Description: {seller['description']}\n"
                         f"___________________________________\n")
    await bot.send_message(message.chat.id, msg_to_answer)


@router.message(F.text == "Show cart" or "Add to cart")
async def ask_for_login(message: types.Message, state: FSMContext):
    await message.reply('Enter your login:')
    await state.set_state(SomeState.waiting_for_login)


@router.message(SomeState.waiting_for_login)
async def capture_login(message: types.Message, state: FSMContext):
    await state.update_data(login=message.text)
    await message.reply('Enter your password')
    await state.set_state(SomeState.waiting_for_password)


@router.message(SomeState.waiting_for_password)
async def capture_password(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    login = user_data['login']
    password = message.text

    user_cart_data = await fetch_user_cart(login, password)

    if user_cart_data:
        msg_to_answer = ''
        products = user_cart_data['products']
        for product in products:
            msg_to_answer += f"Product: {product['name']}, count:{product['count']}\n"
        msg_to_answer += f"Result price:{user_cart_data['result_price']}"
        await bot.send_message(message.chat.id, msg_to_answer)
    else:
        await bot.send_message(message.chat.id, f"Invalid data")


@router.message(SomeState.waiting_for_password)
async def capture_password_for_product(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    login = user_data['login']
    password = message.text

    user_add_product_data = await fetch_user_add_product(login, password)

    if user_add_product_data:
        products = user_add_product_data['products']
        cart = []

        msg_to_answer = "Available products:\n"
        for product in products:
            msg_to_answer += f"- {product['name']}, price: {product['price']}\n"
            cart.append(product)
        await bot.send_message(message.chat.id, msg_to_answer)

        msg_to_answer = "Your cart:\n"
        for product in cart:
            msg_to_answer += f"- {product['name']}, price: {product['price']}\n"
        await bot.send_message(message.chat.id, msg_to_answer)
    else:
        await bot.send_message(message.chat.id, "Invalid data")






async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


class Command(BaseCommand):
    help = 'TG Bot for online shop'

    def handle(self, *args, **options):
        asyncio.run(main())