import tkinter as tk


def get_root(geo_ver, geo_hor, title):
    root = tk.Tk()
    root.geometry(f"{geo_ver}x{geo_hor}")
    root.title(title)
    return root


def init_play_button(control_frame, func):
    play_button = tk.Button(control_frame, text="Play/Pause", command=func)
    play_button.pack(side="left")


def init_timing_button(control_frame, func):
    timing_button = tk.Button(control_frame, text="Timing", command=func)
    timing_button.pack(side="left")


def init_speed_toggle(root, control_frame, func):
    speed_var = tk.StringVar(root)
    speed_var.set("1.0")  # default
    speeds = ["0.5", "1.0", "1.5", "2.0", "2.5", "3.0"]
    speed_option = tk.OptionMenu(control_frame, speed_var, *speeds, command=func)
    speed_option.pack(side="left")


def init_menu_bar(root, func):
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=func)


def init_video_frame(root, title, ver, hor):
    video_window = tk.Toplevel(root)
    video_window.title(title)
    video_window.geometry(f"{hor}x{ver}")

    # Open window right next to the main window
    x = root.winfo_x()
    y = root.winfo_y()
    video_window.geometry(f"+{x + root.winfo_width()}+{y}")

    video_frame = tk.Frame(video_window, width=hor, height=ver, bg="black")
    video_frame.pack()

    return video_frame


def init_label(root, ver, hor):
    frame = tk.Frame(root, width=hor, height=ver, bg="black")
    frame.pack()
    label = tk.Label(frame, text="Open your video", bg="black", fg="white", wraplength=hor - 20)
    label.pack()

    return label
