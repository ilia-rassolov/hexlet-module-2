'''
В этом упражнении вам предстоит написать тесты для функций управления пользователями. Функции что вам нужно
будет протестировать:

create_user() - принимает словарь пользователей users.json, имя пользователя и его почту. Добавляет пользователя в словарь
и возвращает пользователя, либо возвращает None, если такой уже существует.
get_user() - принимает словарь пользователей users.json и имя пользователя. Возвращает пользователя либо None, если
такого нет.
update_user() - принимает словарь пользователей users.json, имя пользователя и новую почту. Обновляет данные пользователя
 и возвращает нового пользователя, либо None если такого нет.
delete_user() - принимает словарь пользователей users.json и имя пользователя. Удаляет его из словаря. При повторной
попытке удаления ничего не происходит.
list_users() - принимает словарь пользователей users.json и возвращает подробный список в виде [{"username": username,
 "email": email}, {..}]

users.json = {"alice": {"email": "alice@mail.com"}}

create_user(users.json, "phil", "phil@mail.com")
users.json # {"alice": {"email": "alice@mail.com"}, "phil": {"email": "phil@mail.com"}}
create_user(users.json, "phil", "phil@mail.com") # None
update_user(users.json, "john", "john@mail.com") # None
update_user(users.json, "phil", "new_mail@mail.com")
users = get_user(users.json, "phil")
users["email"] # "new_mail@mail.com"
get_user(users.json, "wrong_user") # None
delete_user(users.json, "phil")
delete_user(users.json, "phil")
list_users(users.json) # [{"username": "alice", "email": "alice@mail.com"}]

Подсказки
Один из тестов уже написан в упражнении. Используйте его как образец при написании своих тестов.
Используйте фикстуру users.json в ваших тестах
'''

import pytest


@pytest.fixture
def users():
    return {
        "alice": {"email": "alice@example.com"},
        "bob": {"email": "bob@example.com"},
    }


def test_get_user(users, get_user):
    user = get_user(users, "alice")
    assert user["email"] == "alice@example.com"

    assert get_user(users, "wrong_user") is None


# BEGIN (write your solution here)
def test_create_user(users, create_user):
    user = create_user(users, 'ilia', 'il@il.ru')
    assert user["email"] == 'il@il.ru'

    assert create_user(users, "alice", "alice@example.com") is None


def test_update_user(users, update_user):
    user = update_user(users, "alice", "alice_update@example.com")
    assert user["email"] == "alice_update@example.com"

    assert update_user(users, 'ilia', 'il@il.ru') is None


def test_delete_user(users, delete_user):
    delete_user(users, "alice")
    assert users.get("alice") is None


def test_list_users(users, list_users):
    all = list_users(users)
    assert all[0]["username"] == "alice"




