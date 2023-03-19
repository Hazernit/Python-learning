# class Team
#     def __init__(*members):
#         self.members = members
#         self.index = None
#
#     def __iter__(self):
#         return self,
#
#     def __next__(self):
#         try:
#             return "{} is {}".format(self.members[self.index], self.index)
#         except ValueError:
#             raise StopIteration
#         finally:
#             self.index += 1
#
# a = Team("root", "neo")