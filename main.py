import tkinter as tk

class TamagusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tamagus AZ")
        self.hunger = 5

        self.label = tk.Label(root, text="Seu Tamagus está com fome!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.feed_button = tk.Button(root, text="Alimentar", command=self.feed)
        self.feed_button.pack()

        self.status_label = tk.Label(root, text="Fome: 5", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.root.after(5000, self.increase_hunger)

    def feed(self):
        self.hunger = max(0, self.hunger - 1)
        self.update_status()

    def increase_hunger(self):
        self.hunger += 1
        self.update_status()
        self.root.after(5000, self.increase_hunger)

    def update_status(self):
        if self.hunger > 10:
            self.label.config(text="Seu Tamagus está triste!")
        elif self.hunger > 5:
            self.label.config(text="Seu Tamagus está faminto!")
        else:
            self.label.config(text="Seu Tamagus está feliz!")
        self.status_label.config(text=f"Fome: {self.hunger}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TamagusApp(root)
    root.mainloop()
