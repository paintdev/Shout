from RealtimeSTT import AudioToTextRecorder
import pyautogui
import customtkinter
import threading
import keyboard
import time
import webbrowser

def shout():
    recorder = AudioToTextRecorder()

    def process_text(text):
            if text:
                 keyboard.release('decimal')
                 keyboard.release('delete')

            pyautogui.typewrite(text + " ")
            print(f"Shout detected and typed: {text}")
    
    print("Loading Shout. Please wait until you see 'speak now'")

    while True:
        if check_var and check_var.get():
             if keyboard.is_pressed('decimal') or keyboard.is_pressed('delete'):
                  recorder.text(process_text)

                  while keyboard.is_pressed('decimal') or keyboard.is_pressed('delete'):
                       time.sleep(0.1)
             else:
                  time.sleep(0.05)
        else:
             time.sleep(0.5)

def shout_gh():
    webbrowser.open("https://github.com/paintdev/Shout")

check_var = None

if __name__ == "__main__":
    app = customtkinter.CTk()
    app.title("Shout")
    app.geometry("420x200")
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, pad=20)

    check_var = customtkinter.BooleanVar(value=True)

    namelabel = customtkinter.CTkLabel(app, text="Shout", font=("Arial", 24, "bold"))
    namelabel.grid(row=0, column=0, padx=20, pady=0, sticky="ew")

    checkbox = customtkinter.CTkCheckBox(app, text="Toggle Shout", variable=check_var)
    checkbox.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

    label = customtkinter.CTkLabel(app, text="Hold Numpad Period while speaking (NumLock is recommended to\nbe off, but works with it on)")
    label.grid(row=2, column=0, padx=20, pady=0, sticky="w")   

    button = customtkinter.CTkButton(app, text="Shout GitHub", command=shout_gh)
    button.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

    threading.Thread(target=shout, daemon=True).start()

    app.mainloop()

