#!/usr/bin/python

import os
import sys
import re


class link(object):
    def __init__(self):
        self.prev = self
        self.next = self

    def add_node(self, node):
        node.next = self
        node.prev = self.prev
        self.prev.next = node
        self.prev = node

    def del_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def is_node_empty(self):
        if self == self.next:
            return 1
        else:
            return 0

    def get_node_number(self):
        node = self.next
        cnt = 0
        while node != self:
            cnt += 1
            node = node.next
        return cnt


def main():
    head = link()
    node = link()
    print(head.get_node_number())
    print(head.is_node_empty())
    print(head.add_node(node))
    print(head.get_node_number())
    print(head.is_node_empty())

    print(head.del_node(node))
    print(head.get_node_number())
    print(head.is_node_empty())


if __name__ == '__main__':
    main()