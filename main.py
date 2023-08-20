import tkinter as tk
import vlc
from tkinter import filedialog
from interfaces import get_root, init_menu_bar, init_play_button, init_timing_button, init_speed_toggle, \
    init_video_frame, init_label

# setting
MAIN_VERTICAL_SIZE = 500
MAIN_HORIZONTAL_SIZE = 300
VIDEO_VERTICAL_SIZE = 500
VIDEO_HORIZONTAL_SIZE = 700

# init
instance = vlc.Instance()
player = instance.media_player_new()
root = get_root(MAIN_HORIZONTAL_SIZE, MAIN_VERTICAL_SIZE, "Video Timing Counter")


def open_file():
    file_path = filedialog.askopenfilename()
    label.config(text=file_path)
    media = instance.media_new(file_path)
    player.set_media(media)
    video_frame = init_video_frame(root, file_path,
                                   VIDEO_VERTICAL_SIZE, VIDEO_HORIZONTAL_SIZE)
    player.set_hwnd(video_frame.winfo_id())


def toggle_play_pause():
    if player.get_state() == vlc.State.Playing:
        player.pause()
    else:
        player.play()


def get_current_time():
    time = player.get_time()  # ms
    text_box.insert("end", str(time) + "\n")


def change_speed(value):
    player.set_rate(float(value))


# interface setting
label = init_label(root, MAIN_VERTICAL_SIZE, MAIN_HORIZONTAL_SIZE)
control_frame = tk.Frame(root)
control_frame.pack()
init_play_button(control_frame, toggle_play_pause)
init_timing_button(control_frame, get_current_time)
init_speed_toggle(root, control_frame, change_speed)
init_menu_bar(root, open_file)

text_box = tk.Text(root)
text_box.pack()

root.mainloop()
