import pyglet
from pyglet import shapes
from random import sample
window = pyglet.window.Window(width=720, height=480)
batch = pyglet.graphics.Batch()

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

array_to_sort = [5,4,1,2,3]
# array_to_sort.insert(0, 132)
animation_frames = bubble_sort_animation(array_to_sort.copy())

compared_color = (255, 0, 0)
normal_color = (255, 255, 255)

@window.event
def on_draw():
    window.clear() # เคลียร์หน้าต่างก่อนที่จะวาดภาพใหม่
    for i, value in enumerate(array_to_sort):
        color = compared_color  # กำหนดสีให้เริ่มต้นเป็นสีแดง (สีของสมาชิกที่เปรียบเทียบ)
        if animation_frames and animation_frames[0][i] == value:
            color = normal_color  # เปลี่ยนสีเป็นสีขาว (สีของสมาชิกที่ไม่ได้ถูกเปรียบเทียบ)
        base_y = 10  # ตำแหน่ง Y ของส่วนล่างของแท่งเริ่มต้นที่ 10
        if animation_frames:
            # ปรับตำแหน่ง Y ของแท่งให้มีการเลื่อนขึ้นหรือลงเมื่อมีการลบ frame ออกจาก animation_frames
            base_y = 10 + (len(array_to_sort) - len(animation_frames[0])) * 3
        # สร้างสี่เหลี่ยมเพื่อแสดงข้อมูล
        rect = shapes.Rectangle(i * 50 + 120 #แกน X
                                , base_y #แกน Y
                                , 40 #ความกว้าง
                                , value * 80 #ความสูง
                                , color=color
                                , batch=batch)
        rect.draw()  # วาดสี่เหลี่ยมลงบนหน้าต่าง
        label = pyglet.text.Label(str(value), font_size=12, x=rect.x + rect.width // 2, y=rect.y + rect.height // 2,
                                  anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
        label.draw()  # วาดข้อความลงบนหน้าต่าง


def update(dt):
    global array_to_sort, animation_frames
    if animation_frames:
        array_to_sort = animation_frames.pop(0)

pyglet.clock.schedule_interval(update, 1)  # ปรับความเร็วของ animation
pyglet.app.run()
