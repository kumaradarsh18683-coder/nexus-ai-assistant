import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("NEXUS AI")
app.geometry("900x600")
app.configure(fg_color="#050816")

title = ctk.CTkLabel(
    app,
    text="NEXUS AI",
    font=("Segoe UI", 52, "bold"),
    text_color="#00E5FF"
)

title.pack(pady=(80,10))

subtitle = ctk.CTkLabel(
    app,
    text="Initializing System...",
    font=("Segoe UI",20),
    text_color="#8BE9FD"
)

subtitle.pack(pady=10)

progress = ctk.CTkProgressBar(
    app,
    width=500,
    height=16
)

progress.pack(pady=30)
progress.set(0)

status = ctk.CTkLabel(
    app,
    text="Starting...",
    font=("Consolas",18),
    text_color="white"
)

status.pack()
import subprocess

steps = [
    "Booting Nexus Core...",
    "Initializing Voice Engine...",
    "Connecting Gemini AI...",
    "Loading Command Engine...",
    "Loading Memory...",
    "Checking System...",
    "Optimizing Performance...",
    "System Ready..."
]


current = 0

def start_loading():
    global current

    if current < len(steps):
        progress.set((current + 1) / len(steps))
        status.configure(text=steps[current])
        current += 1
        app.after(1200, start_loading)
    else:
     status.configure(text="🚀 Launching Nexus AI...")
    app.after(1000, launch_gui)

glow_colors = [
    "#00BFFF",
    "#00E5FF",
    "#66FFFF",
    "#00E5FF"
]

glow_index = 0

def animate_title():
    global glow_index

    title.configure(text_color=glow_colors[glow_index])

    glow_index = (glow_index + 1) % len(glow_colors)

    app.after(300, animate_title)

def launch_gui():
    app.destroy()
    subprocess.Popen(["python", "gui.py"])

animate_title()
start_loading()

app.mainloop()