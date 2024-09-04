# def find_steps_to_return(n, k):
#     position = 0  # Start from Hasani's position which is index 0
#     steps = 0
#     while True:
#         position = (position + k) % n
#         steps += 1
#         if position == 0:
#             break
#     return steps

# # Example usage
# n, k = map(int, input().split())
# print(find_steps_to_return(n, k))
