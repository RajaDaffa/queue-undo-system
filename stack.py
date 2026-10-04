class Stack:
    def __init__(self):
        self.data = []

    # Menambahkan aktivitas
    def push(self, aktivitas):
        self.data.append(aktivitas)

    # Mengambil aktivitas terakhir untuk Undo
    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    # Melihat aktivitas terakhir
    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    # Mengecek apakah stack kosong
    def is_empty(self):
        return len(self.data) == 0

    # Menampilkan seluruh aktivitas
    def display(self):
        return self.data


# Simulasi program (sesuai tabel simulasi nomor 9)
if __name__ == "__main__":
    stack = Stack()

    print("=== SIMULASI FITUR UNDO ===")

    # Langkah 1-5: Push
    for aktivitas in [
        "Menambahkan mahasiswa Radish",
        "Menambahkan mahasiswa Tio",
        "Mengubah data Dimas",
        "Menghapus data Falah",
        "Menambahkan mahasiswa Raja",
    ]:
        stack.push(aktivitas)
        print("Push", aktivitas, "->", stack.display())

    # Langkah 6-7: Pop / Undo
    print("Undo", stack.pop(), "->", stack.display())
    print("Undo", stack.pop(), "->", stack.display())

    # Langkah 8: Peek
    print("Peek", stack.peek(), "->", stack.display())

    # Langkah 9: Is empty
    print("Is empty:", stack.is_empty(), "->", stack.display())