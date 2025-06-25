class Solution:
     def __init__(self, id=int, generation=int):
         self.id = id
         self.generation = generation
         self.field = [[0 for _ in range(9)] for _ in range(9)]