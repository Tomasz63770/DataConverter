import tkinter as tk
from tkinter import filedialog, messagebox
import json
import yaml
import xmltodict
from dicttoxml import dicttoxml
import threading


data = None


# ---------------- LOAD ----------------
def load_file():
    def task():
        global data
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        try:
            if file_path.endswith(".json"):
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

            elif file_path.endswith((".yaml", ".yml")):
                with open(file_path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)

            elif file_path.endswith(".xml"):
                with open(file_path, "r", encoding="utf-8") as f:
                    data = xmltodict.parse(f.read())

            else:
                messagebox.showerror("Error", "Unsupported format")
                return

            text.delete("1.0", tk.END)
            text.insert(tk.END, str(data))

        except Exception as e:
            messagebox.showerror("Error", str(e))

    threading.Thread(target=task).start()


# ---------------- SAVE ----------------
def save_file():
    def task():
        global data

        file_path = filedialog.asksaveasfilename(defaultextension=".json")
        if not file_path:
            return

        try:
            content = text.get("1.0", tk.END)

            if file_path.endswith(".json"):
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(eval(content), f, indent=4)

            elif file_path.endswith((".yaml", ".yml")):
                with open(file_path, "w", encoding="utf-8") as f:
                    yaml.dump(eval(content), f, allow_unicode=True)

            elif file_path.endswith(".xml"):
                xml = dicttoxml(eval(content), custom_root="root", attr_type=False)
                with open(file_path, "wb") as f:
                    f.write(xml)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    threading.Thread(target=task).start()


# ---------------- UI ----------------
root = tk.Tk()
root.title("DataConverter UI")

btn_load = tk.Button(root, text="Load file", command=load_file)
btn_load.pack()

btn_save = tk.Button(root, text="Save file", command=save_file)
btn_save.pack()

text = tk.Text(root, height=20, width=60)
text.pack()

root.mainloop()