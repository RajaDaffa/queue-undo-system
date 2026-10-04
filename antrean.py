class Queue:
    def __init__(self):
        self.data = []

    # Menambahkan mahasiswa ke belakang antrean
    def enqueue(self, mahasiswa):
        self.data.append(mahasiswa)

    # Mengambil mahasiswa paling depan
    def dequeue(self):
        if self.is_empty():
            return None
        return self.data.pop(0)

    # Melihat mahasiswa paling depan
    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]

    # Mengecek apakah antrean kosong
    def is_empty(self):
        return len(self.data) == 0

    # Menampilkan seluruh antrean
    def display(self):
        return self.data


# Simulasi program (sesuai tabel simulasi nomor 7)
if __name__ == "__main__":
    queue = Queue()

    print("=== SIMULASI ANTREAN MAHASISWA ===")

    # Langkah 1-5: Enqueue
    for nama in ["Radish", "Tio", "Dimas", "Falah", "Raja"]:
        queue.enqueue(nama)
        print("Enqueue", nama, "->", queue.display())

    # Langkah 6: Dequeue
    print("Dequeue", queue.dequeue(), "->", queue.display())

    # Langkah 7: Peek
    print("Peek", queue.peek(), "->", queue.display())

    # Langkah 8: Is empty
    print("Is empty:", queue.is_empty(), "->", queue.display())