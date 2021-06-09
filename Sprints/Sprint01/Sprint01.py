# #S01-00
# import os.path
# def print_filename():
#     if __name__ == "__main__":
#         print(os.path.basename(__file__))
# print_filename()

# #S01-01
# def crystal_ball(courage, intelligence):
#     if courage > 50 and intelligence > 50:
#         print("I see great success in your future.")
#     elif courage >= 100 or intelligence <= 10:
#         print("Your life is in danger!")
#     else:
#         print("Your future is a mystery")
# def print_result(coureage, intelligence):
#     print(f'Reading the future for an adventurer with {coureage} courage '
#           f'and {intelligence} intelligence...')
#     crystal_ball(coureage, intelligence)
#     print('***')
# if __name__ == "__main__":
#     print_result(19, 0)
#     print_result(57, 60)
#     print_result(200, 79)
#     print_result(150, 15)
#     print_result(30, 100)
#     print_result(100, 25)
#     print_result(50, 55)
#     print_result(50, 9)

# #S01-02
# def buy_milk(money=0):
#     product = "[milk]"
#     price = 25
#     if money >= price:
#         product = product * (money // price)
#     else:
#         product = None
#     return product
# def buy_bread(money=0):
#     product = '[bread]'
#     price = 19
#     if money >= price and money // price >= 3:
#         product = product * 3
#     elif money >= price:
#         product = product * (money // price)
#     else:
#         product = None
#     return product
#
# print(f"Buy milk with 25$, result: {buy_milk(25)}")
# print(f"Buy bread with 19$, result: {buy_bread(19)}")
# print(f"Buy milk with nothing, result: {buy_milk()}")
# print(f"Buy bread with nothing, result: {buy_bread(00)}")
# print(f"Buy milk with 200$, result: {buy_milk(200)}")
# print(f"Buy bread with 200$, result: {buy_bread(200)}")
# print(f"Buy milk with 10$, result: {buy_milk(10)}")
# print(f"Buy bread with 10$, result: {buy_bread(10)}")
# print(f"Buy milk with 53$, result: {buy_milk(53)}")
# print(f"Buy bread with 53$, result: {buy_bread(53)}")
# print(f"Buy milk with 100$, result: {buy_milk(100)}")
# print(f"Buy bread with 100$, result: {buy_bread(100)}")
# a = 100
# b = 5
# c = min(7, a//b)
# print(c) // ответ 7
