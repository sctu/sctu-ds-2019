# 10�����ĵ�����ֵΪ1,2,...��10
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(-1)
tail = head

# β�巨����������
for i in range(1, 11):
    # (1) ����һ���µĽ��
    new_node = Node(i)

    # (2) ����ǰ��������һ�����(β���)
    # ��next����Ϊ�½ڵ�
    tail.next = new_node

    # (3) ����β����ֵ
    tail = new_node











