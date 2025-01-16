import json
from pymongo import MongoClient
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class UserPreferences:
    timezone: str


@dataclass
class User:
    username: str
    password: str
    roles: list
    preferences: UserPreferences
    active: bool
    created_ts: float


def parse_roles(data):
    roles = []
    if data.get("is_user_admin"):
        roles.append("admin")
    if data.get("is_user_manager"):
        roles.append("manager")
    if data.get("is_user_tester"):
        roles.append("tester")
    return roles


def parse_user(data):
    return User(
        username=data["user"],
        password=data["password"],
        roles=parse_roles(data),
        preferences=UserPreferences(timezone=data["user_timezone"]),
        active=data["is_user_active"],
        created_ts=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")).timestamp(),
    )


def main():
    # Connect MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["my_database"]
    users_collection = db["users"]

    # Read File
    with open("udata.json", "r") as file:
        data = json.load(file)["users"]

        # Parse data
        users = [parse_user(item) for item in data]
        
        # Convert user to dict
        users_dicts = [asdict(user) for user in users]
        
        users_collection.insert_many(users_dicts)

    print("Users successfully imported")


if __name__ == "__main__":
    main()
