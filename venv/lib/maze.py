from enum import Enum

class MapSite():
    def Enter(self):
        raise NotImplementedError('Abstract Base Class Method')

class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3

class Room(MapSite):
    def __init__(self, roomNo):
        self._sides = [MapSite] * 4
        self._roomNumber = int(roomNo)

    def GetSide(self, Direction):
        return self._sides[Direction]

    def SetSide(self, Direction, MapSite):
        self._sides[Direction] = MapSite

    def Enter(self):
        print('        You have entered room: ' + str(self._roomNumber))

class Wall(MapSite):
    def Enter(self):
        print('        You just ran into a wall. . .')

class Door(MapSite):
    def __init__(self, Room1=None, Room2=None):
        self._room1 = Room1
        self._room2 = Room2
        self._isOpen = False

    def OtherSideFrom(self, Room):
        print('\tDoor obj: This door is a side of Room: {}'.format(Room._roomNumber))
        if 1 == Room.roomNumber:
            other_room = self._room2
        else:
            other_room = self._room1
        return other_room

    def Enter(self):
        if self._isOpen: print('         ***** You have passed through this door...')
        else: print('     **This door needs to be opened before you can pass through it')


class Maze():
    def __init__(self):
        self._rooms = {}

    def AddRoom(self, room):
        self._rooms[room._roomNumber] = room

    def RoomNo(self, room_number):
        return self._rooms[room_number]


class MazeFactory():
    @classmethod
    def MakeMaze(cls):
        return Maze()

    @classmethod
    def MakeWall(cls):
        return Wall()

    @classmethod
    def MakeRoom(cls, n):
        return Room(n)

    def MakeDoor(cls, r1, r2):
        return Door(r1, r2)


class MazeGame():

    def CreateMaze(self, factory=MazeFactory):
        aMaze = factory.MakeMaze()
        r1 = factory.MakeRoom(1)
        r2 = factory.MakeRoom(2)
        aDoor = factory.MakeDoor(r1, r2)

        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)

        r1.SetSide(Direction.North.Value, MakeWall())
        r1.SetSide(Direction.East.Value, aDoor)
        r1.SetSide(Direction.South.Value, MakeWall())
        r1.SetSide(Direction.West.Value, MakeWall())

        r2.SetSide(Direction(0).value, MakeWall())
        r2.SetSide(Direction(1).value, MakeWall())
        r2.SetSide(Direction(2).value, MakeWall())
        r2.SetSide(Direction(3).value, aDoor)

        return aMaze


if __name__ == '__main__':
    def find_maze_rooms(maze_obj):
        maze_rooms = []
        for room_number in range(5):
            try:
                room=maze_obj.RoomNo(room_number)
                print('\n^^^ Maze has room: {}'.format(room_number, room))
                print('        Entering the room. . .')
                room.Enter()

                maze_rooms.append(room)
                for idx in range(4):
                    side = room.GetSide(idx)
                    side_str = str(side.__class__).replace("<class '__main__.", "").replace("'>", "")
                    print('      Room: {}, {:<15s}, Type: {}'.format(room_number, Direction(idx), side_str))
                    print('      Trying to enter: ', Direction(idx))
                    side.Enter()
                    if 'Door' in side_str:
                        door = side
                        if not door._isOpen:
                            print('     *** Opening the door')
                            door.isOpen = True
                            door.Enter()
                        print('\t', door)

                        other_room = door.OtherSideFrom(room)

            except KeyError:
                print('No room', room_number)
            num_of_rooms = len(maze_rooms)
            print('\n There are {} rooms in the Maze.'.format(num_of_rooms))

            print('Both doors are teh same object and they are on the East and West Side of the rooms.')
print('*' * 21)
print('*** The Maze Game ***')
print('*' * 21)

factory = MazeFactory
print(factory)

maze_obj = MazeGame().CreateMaze(factory)
find_maze_rooms(maze_obj)