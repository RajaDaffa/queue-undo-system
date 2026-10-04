import unittest
from antrean import Queue


class TestQueue(unittest.TestCase):

    # Pengujian penambahan mahasiswa
    def test_enqueue(self):
        queue = Queue()

        queue.enqueue("Radish")
        queue.enqueue("Tio")
        queue.enqueue("Dimas")

        self.assertEqual(
            queue.display(),
            ["Radish", "Tio", "Dimas"]
        )

    # Pengujian pengambilan mahasiswa
    def test_dequeue(self):
        queue = Queue()

        queue.enqueue("Radish")
        queue.enqueue("Tio")
        queue.enqueue("Dimas")

        hasil = queue.dequeue()

        self.assertEqual(hasil, "Radish")
        self.assertEqual(
            queue.display(),
            ["Tio", "Dimas"]
        )

    # Pengujian melihat mahasiswa paling depan
    def test_peek(self):
        queue = Queue()

        queue.enqueue("Radish")
        queue.enqueue("Tio")

        self.assertEqual(queue.peek(), "Radish")

    # Pengujian kondisi kosong
    def test_is_empty(self):
        queue = Queue()

        self.assertTrue(queue.is_empty())

        queue.enqueue("Radish")

        self.assertFalse(queue.is_empty())

        # Pengujian tambahan: input berbeda
    def test_enqueue_satu_data(self):
        queue = Queue()
        queue.enqueue("Lika")
        self.assertEqual(queue.display(), ["Lika"])

    def test_dequeue_antrean_kosong(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())

    def test_peek_antrean_kosong(self):
        queue = Queue()
        self.assertIsNone(queue.peek())

    def test_is_empty_setelah_dequeue(self):
        queue = Queue()
        queue.enqueue("Fitri")
        queue.dequeue()
        self.assertTrue(queue.is_empty())
        
if __name__ == "__main__":
    unittest.main()