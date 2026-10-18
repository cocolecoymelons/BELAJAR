from enum import Enum

class Status(Enum):
    
    ONLINE = 1
    OFFLINE = 0
    LOCKED = 2
    BANNED = 4
    
player_1 = Status.ONLINE
player_2 = Status.BANNED

print(player_1)
print(player_1.name)
print(player_1.value)
