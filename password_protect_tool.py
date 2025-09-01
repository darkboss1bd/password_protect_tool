import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Hacker-style animation text (simulated)
ANIMATION_TEXT = """
██████╗  █████╗ ████████╗████████╗██╗     ███████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
██████╔╝███████║   ██║      ██║   ██║     █████╗  
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
                                                
███████╗███╗   ██╗██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝████╗  ██║██╔══██╗██║   ██║██╔════╝██╔══██╗
█████╗  ██╔██╗ ██║██║  ██║██║   ██║█████╗  ██████╔╝
██╔══╝  ██║╚██╗██║██║  ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
███████╗██║ ╚████║██████╔╝ ╚████╔╝ ███████╗██║  ██║
╚══════╝╚═╝  ╚═══╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
"""

BANNER = r"""
╔════════════════════════════════════════╗
║        🔐 DARKBOSS1BD TOOLKIT 🔐       ║
║    Secure Your Python Scripts Now!     ║
╚════════════════════════════════════════╝
"""

def add_password_protection(script_path, password, output_path):
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            original_code = f.read()

        # Generate protected script
        protected_code = f'''# DARKBOSS1BD - PASSWORD PROTECTED SCRIPT
# 🔐 Script secured with password protection

import sys
import time

# Hacker Animation (Simulated)
def show_hacker_animation():
    animation = """{ANIMATION_TEXT.strip()}"""
    for line in animation.splitlines():
        print(line)
        time.sleep(0.05)
    print("\\n[+] Initializing secure script...\\n")

show_hacker_animation()

# Password Prompt
def authenticate():
    correct_password = "{password}"
    attempts = 3
    while attempts > 0:
        pwd = input("🔐 Enter Password to run this script: ")
        if pwd == correct_password:
            print("\\n✅ Access Granted! Running script...\\n")
            return True
        else:
            attempts -= 1
            print(f"❌ Wrong Password! {attempts} attempts left.\\n")
    print("\\n⛔ Too many failed attempts. Exiting...")
    sys.exit(1)

if __name__ == "__main__":
    authenticate()

# --- Original Script Starts Here ---
{original_code}
'''

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(protected_code)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# GUI Application
class PasswordProtectTool:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 darkboss1bd - Script Protector")
        self.root.geometry("700x500")
        self.root.config(bg="#0e0e0e")
        self.root.resizable(False, False)

        # Title Label
        title = tk.Label(
            root,
            text="🔐 DARKBOSS1BD PASSWORD PROTECTOR",
            font=("Courier", 16, "bold"),
            fg="#00ff00",
            bg="#0e0e0e"
        )
        title.pack(pady=20)

        # Banner
        banner_label = tk.Label(
            root,
            text=BANNER,
            font=("Courier", 10),
            fg="#00ccff",
            bg="#0e0e0e",
            justify="left"
        )
        banner_label.pack(pady=10)

        # File Selection
        self.file_label = tk.Label(
            root,
            text="No file selected",
            font=("Courier", 10),
            fg="white",
            bg="#0e0e0e",
            wraplength=600
        )
        self.file_label.pack(pady=10)

        select_btn = tk.Button(
            root,
            text="📁 Select Python Script",
            font=("Courier", 12),
            bg="#0066cc",
            fg="white",
            command=self.select_file
        )
        select_btn.pack(pady=10)

        # Password Entry
        tk.Label(
            root,
            text="Enter Password:",
            font=("Courier", 12),
            fg="white",
            bg="#0e0e0e"
        ).pack(pady=5)

        self.password_entry = tk.Entry(
            root,
            font=("Courier", 12),
            width=30,
            show="*"
        )
        self.password_entry.pack(pady=5)

        # Protect Button
        protect_btn = tk.Button(
            root,
            text="🔒 Add Password Protection",
            font=("Courier", 14, "bold"),
            bg="#00cc00",
            fg="black",
            command=self.protect_script
        )
        protect_btn.pack(pady=20)

        # Status Label
        self.status_label = tk.Label(
            root,
            text="",
            font=("Courier", 10),
            fg="#00ff00",
            bg="#0e0e0e"
        )
        self.status_label.pack(pady=10)

        self.script_path = ""

    def select_file(self):
        self.script_path = filedialog.askopenfilename(
            title="Select a Python Script",
            filetypes=[("Python Files", "*.py")]
        )
        if self.script_path:
            self.file_label.config(text=f"Selected: {os.path.basename(self.script_path)}")
        else:
            self.file_label.config(text="No file selected")

    def protect_script(self):
        if not self.script_path:
            messagebox.showwarning("Warning", "Please select a Python script first!")
            return

        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Warning", "Please enter a password!")
            return

        output_path = filedialog.asksaveasfilename(
            title="Save Protected Script As",
            defaultextension=".py",
            filetypes=[("Python Files", "*.py")]
        )

        if not output_path:
            return

        if add_password_protection(self.script_path, password, output_path):
            self.status_label.config(text="✅ Script protected successfully!", fg="#00ff00")
            messagebox.showinfo("Success", f"Protected script saved as:\n{output_path}")
        else:
            self.status_label.config(text="❌ Failed to protect script!", fg="#ff0000")
            messagebox.showerror("Error", "Failed to protect the script!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordProtectTool(root)
    root.mainloop()