import pytest

from app.user_manager import UserManager
from app.user_manager import count_total_users


def test_add_user():

    manager = UserManager()

    manager.add_user("Ali")

    assert manager.count_users() == 1


def test_add_duplicate_user():

    manager = UserManager()

    manager.add_user("Ali")

    with pytest.raises(ValueError):
        manager.add_user("Ali")


def test_add_empty_user():

    manager = UserManager()

    with pytest.raises(ValueError):
        manager.add_user("")


def test_remove_user():

    manager = UserManager()

    manager.add_user("Ali")
    manager.remove_user("Ali")

    assert manager.count_users() == 0


def test_remove_unknown_user():

    manager = UserManager()

    with pytest.raises(ValueError):
        manager.remove_user("Ali")


def test_count_total_users():

    users = ["Ali", "Sara", "Amine"]

    assert count_total_users(users) == 3