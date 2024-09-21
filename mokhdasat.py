def find_coordinates(n):
    if n == 1:
        return (0, 0)
    
    # Determine the layer
    layer = 0
    max_number_in_layer = 1
    while max_number_in_layer < n:#1 14
        layer += 1#1
        max_number_in_layer += 8 * layer#1
    
    start_number_in_layer = max_number_in_layer - 8 * layer + 1#-7
    position_in_layer = n - start_number_in_layer#21
    
    # Determine the segment within the layer
    side_length = layer * 2#0
    # Each side of a layer has side_length numbers
    side = position_in_layer // side_length#21 // 0
    
    position_on_side = position_in_layer % side_length#21 0
    x, y = layer, -layer#-1 1
    
    # Adjust starting position based on the side
    if side == 0:
         x -= position_on_side
    elif side == 1:
        x -= side_length
        y += position_on_side + 1
    elif side == 2:
        y += side_length
        x -= side_length - (position_on_side + 1)
    elif side == 3:
        x += position_on_side + 1

    return (x, y)

n = int(input())
result = find_coordinates(n)
print(result[0], result[1])