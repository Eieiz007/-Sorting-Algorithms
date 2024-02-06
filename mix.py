import pyglet
from pyglet import shapes
from random import sample

# Bubble Sort
def bubble_sort_animation(arr):
    animations = []

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    animations.append(arr.copy())

    bubble_sort(arr)
    return animations

# Merge Sort
def merge_sort_animation(arr):
    animations = []

    def merge_sort(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        left_copy = arr[left:mid + 1]
        right_copy = arr[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_copy) and j < len(right_copy):
            if left_copy[i] <= right_copy[j]:
                arr[k] = left_copy[i]
                i += 1
            else:
                arr[k] = right_copy[j]
                j += 1
            k += 1

        while i < len(left_copy):
            arr[k] = left_copy[i]
            i += 1
            k += 1

        while j < len(right_copy):
            arr[k] = right_copy[j]
            j += 1
            k += 1

        animations.append(arr.copy())

    merge_sort(arr, 0, len(arr) - 1)
    return animations

# Common visualization setup
window = pyglet.window.Window(width=1200, height=600)
batch = pyglet.graphics.Batch()
compared_color = (255, 0, 0)
normal_color = (255, 255, 255)

# Bubble Sort Animation
array_bubble = sample(range(30, 91), 20)
# array_bubble.insert(0, 92)
animation_frames_bubble = bubble_sort_animation(array_bubble.copy())

# Merge Sort Animation
array_merge = array_bubble.copy()
# array_merge.insert(0, 92)
animation_frames_merge = merge_sort_animation(array_merge.copy())


@window.event
def on_draw():
    window.clear()
    
    # Draw Bubble Sort
    for i, value in enumerate(array_bubble):
        color = compared_color
        if animation_frames_bubble and animation_frames_bubble[0][i] == value:
            color = normal_color
        rect = shapes.Rectangle(i * 50 + 120, 300, 40, value * 3, color=color, batch=batch)
        rect.draw()
        label = pyglet.text.Label(str(value), font_size=12, x=rect.x + rect.width // 2, y=rect.y + rect.height // 2,
                                  anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
        label.draw()

    # Draw Merge Sort
    for i, value in enumerate(array_merge):
        color = compared_color
        if animation_frames_merge and animation_frames_merge[0][i] == value:
            color = normal_color
        rect = shapes.Rectangle(i * 50 + 120, 10, 40, value * 3, color=color, batch=batch)
        rect.draw()
        label = pyglet.text.Label(str(value), font_size=12, x=rect.x + rect.width // 2, y=rect.y + rect.height // 2,
                                  anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
        label.draw()



def update(dt):
    global array_bubble, animation_frames_bubble, array_merge, animation_frames_merge

    # Update Bubble Sort
    if animation_frames_bubble:
        array_bubble = animation_frames_bubble.pop(0)

    # Update Merge Sort
    if animation_frames_merge:
        array_merge = animation_frames_merge.pop(0)


pyglet.clock.schedule_interval(update, 0.05)
pyglet.app.run()
