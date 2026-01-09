import tkinter as tk
from tkinter import messagebox

# =========================
# DATA QUIZ
# =========================
questions = [
    {
        "question": "Kapan hari kemerdekaan indonesia?",
        "options": ["17 agustus", "18 februari", "13 september", "21 agustus"],
        "answer": "17 agustus"
    },
    {
        "question": "Bahasa pemrograman untuk AI?",
        "options": ["HTML", "CSS", "Python", "PHP"],
        "answer": "Python"
    },
    {
        "question": "Sebutkan salah satu sistem operasi komputer?",
        "options": ["Ubuntu", "kubernetes", "photosop", "BMW"],
        "answer": "Ubuntu"
    }
]

# =========================
# APLIKASI QUIZ
# =========================
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x400")
        self.root.config(bg="#1e1e2f")

        self.q_index = 0
        self.score = 0

        self.title = tk.Label(
            root,
            text="QUIZ CERDAS",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#1e1e2f"
        )
        self.title.pack(pady=10)

        self.question_label = tk.Label(
            root,
            text="",
            font=("Arial", 14),
            fg="white",
            bg="#1e1e2f",
            wraplength=400
        )
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                root,
                text="",
                variable=self.var,
                value="",
                font=("Arial", 12),
                bg="#2b2b3c",
                fg="white",
                selectcolor="#4CAF50",
                width=30,
                anchor="w"
            )
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.next_btn = tk.Button(
            root,
            text="Next",
            command=self.next_question,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15
        )
        self.next_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        self.var.set(None)
        q = questions[self.q_index]
        self.question_label.config(text=q["question"])

        for i, option in enumerate(q["options"]):
            self.buttons[i].config(text=option, value=option)

    def next_question(self):
        if self.var.get() == "":
            messagebox.showwarning("Peringatan", "Pilih jawaban dulu!")
            return

        if self.var.get() == questions[self.q_index]["answer"]:
            self.score += 1

        self.q_index += 1

        if self.q_index < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo(
            "Hasil Quiz",
            f"Skor kamu: {self.score} dari {len(questions)}"
        )
        self.root.destroy()


# =========================
# JALANKAN PROGRAM
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()