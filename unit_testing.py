import unittest
from linked_list import SLL

class TestSLL(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.list1 = SLL("node1")

    def test_init_list(self):
        print('test_init_list')
        self.assertEqual(self.list1.head_node.value, "node1")

    def test_insert_at_beginning(self):
        print('test_insert_at_beginning')
        self.list1.insert_beginning("node2")
        self.assertEqual(self.list1.head_node.value, "node2")

    def test_remove_at_beginning(self):
        print('test_remove_at_beginning')
        self.list1.insert_beginning("node2")
        self.list1.remove_node("node2")
        self.assertEqual(self.list1.head_node.value, "node1")

    def test_remove_in_middle(self):
        print('test_remove_in_middle')
        self.list1.insert_beginning("node2")
        self.list1.insert_beginning("node3")
        self.list1.remove_node("node2")
        self.assertFalse(self.list1.head_node.next_node.value == "node2")

    def test_remove_last(self):
        print('test_remove_last')
        self.list1.insert_beginning("node2")
        self.list1.insert_beginning("node3")
        self.list1.remove_node("node1")
        self.assertTrue(self.list1.head_node.next_node.value == "node2")    

if __name__ == '__main__':
    unittest.main()