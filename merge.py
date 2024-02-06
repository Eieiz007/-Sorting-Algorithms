import pyglet
from pyglet import shapes
from random import sample
window = pyglet.window.Window(width=720, height=480)
batch = pyglet.graphics.Batch()

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

array_to_sort = [5,4,1,2,3]
# array_to_sort.insert(0, 132)

animation_frames = merge_sort_animation(array_to_sort.copy())

compared_color = (255, 0, 0)
normal_color = (255, 255, 255)

@window.event
def on_draw():
    window.clear()
    for i, value in enumerate(array_to_sort):
        color = compared_color
        if animation_frames and animation_frames[0][i] == value:
            color = normal_color
        # สร้างกล่องเล็ก
        box = shapes.Rectangle(i * 50 + 120, 10, 40, value * 80, color=color, batch=batch)
        box.draw()
        # เพิ่มข้อความ
        label = pyglet.text.Label(str(value), font_size=12, x=box.x + box.width // 2, y=box.y + box.height // 2,
                                  anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
        label.draw()

def update(dt):
    global array_to_sort, animation_frames
    if animation_frames:
        array_to_sort = animation_frames.pop(0)

pyglet.clock.schedule_interval(update, 2)
pyglet.app.run()
