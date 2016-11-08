from dateutil import tz

class Node(object):
    def __init__(self, timestamp, sign):
        self.timestamp = timestamp
        self.sign = sign
        self.next = None


class EvalResults:
    def __init__(self, timestamp, max_intersects):
        self.timestamp = timestamp
        self.max_intersects = max_intersects


def add_node(head, timestamp, sign):
    """
    Function for internal usage. Inserts not between two nodes in chronological sequence
    :param head: Linked list head
    :param timestamp: node timestamp
    :param sign: +1 or -1
    """
    tmp_node = Node(timestamp, sign)
    if head is None:
        return tmp_node
    if timestamp < head.timestamp:
        tmp_node.next = head
        return tmp_node
    else:
        curr = head
        while curr.next is not None:
            if curr.timestamp < timestamp < curr.next.timestamp:
                next = curr.next
                curr.next = tmp_node
                tmp_node.next = next
                break
            curr = curr.next
        else:
            curr.next = tmp_node
        return head


def intervals_intersecting(value, interval):
    if interval[0] > value[1] or interval[1] < value[0]:
        return False
    else:
        return True


def intersection(values, interval):
    head = None
    for value in values:
        if not intervals_intersecting(value, interval):
            continue
        head = add_node(head, value[0], +1)
        if interval[0] < value[1] < interval[1]:
            head = add_node(head, value[1], -1)
    curr = head
    max_intersections = 0
    max_timestamp = head.timestamp if head.timestamp < interval[0] else interval[0]
    curr_intersections = 0
    while curr is not None:
        curr_intersections += curr.sign
        if curr_intersections > max_intersections:
            max_timestamp = curr.timestamp
            max_intersections = curr_intersections
        curr = curr.next
    return EvalResults(max_timestamp, max_intersections)
