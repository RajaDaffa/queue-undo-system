import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    # Pengujian penambahan aktivitas
    def test_push(self):
        stack = Stack()

        stack.push("Menambahkan mahasiswa Radish")
        stack.push("Menambahkan mahasiswa Tio")

        self.assertEqual(
            stack.display(),
            [
                "Menambahkan mahasiswa Radish",
                "Menambahkan mahasiswa Tio"
            ]
        )

    # Pengujian Undo
    def test_pop(self):
        stack = Stack()

        stack.push("Menambahkan mahasiswa Radish")
        stack.push("Menambahkan mahasiswa Tio")

        hasil = stack.pop()

        self.assertEqual(
            hasil,
            "Menambahkan mahasiswa Tio"
        )

        self.assertEqual(
            stack.display(),
            ["Menambahkan mahasiswa Radish"]
        )

    # Pengujian melihat aktivitas terakhir
    def test_peek(self):
        stack = Stack()

        stack.push("Menambahkan mahasiswa Radish")
        stack.push("Menambahkan mahasiswa Tio")

        self.assertEqual(
            stack.peek(),
            "Menambahkan mahasiswa Tio"
        )

    # Pengujian kondisi kosong
    def test_is_empty(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())

        stack.push("Menambahkan mahasiswa Radish")

        self.assertFalse(stack.is_empty())


        # Pengujian tambahan: input berbeda
    def test_push_satu_aktivitas(self):
        stack = Stack()
        stack.push("Mengubah data Lika")
        self.assertEqual(stack.display(), ["Mengubah data Lika"])

    def test_pop_stack_kosong(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_peek_stack_kosong(self):
        stack = Stack()
        self.assertIsNone(stack.peek())

    def test_is_empty_setelah_pop(self):
        stack = Stack()
        stack.push("Menghapus data Fitri")
        stack.pop()
        self.assertTrue(stack.is_empty())

if __name__ == "__main__":
    unittest.main()