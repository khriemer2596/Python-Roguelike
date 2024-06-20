from typing import Tuple

class Entity:
    """
    Generic class to represent an object in the game
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        
    def move(self, dx: int, dy: int) -> None:
        """Moves the entity

        Args:
            dx (int): horizontal moves
            dy (int): vertical moves
        """
        self.x += dx
        self.y += dy
