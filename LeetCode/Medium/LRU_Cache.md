今天要解决的是之前面试特斯拉数据工程师的实习岗位的时候的一道面试题，当时其实根本不懂，但是看了网上的一些资料在AI的帮助下完成了（不是现场，现场的题更多的是让我写SQL）

今天要从头把它给搞懂

其实就想像成浏览器缓存，比如我今天登陆了谷歌的官网，我的RAM就会把谷歌的logo给存下来，第一次进入时会有点慢，但当我下一次再登录的时候就会很快，因为已经存在RAM里面了。后来我又登录了Youtube和别的一些网站，这个时候RAM已经满了，在满了之后我再登录一个新的网站，就面临一个需要删除一些缓存的问题，那应该删除哪个呢？最聪明的方法就是删掉那个**最不常使用的**。所以这个缓存机制就需要知道哪个是最常使用和最不常使用的，需要排序。

首先需要定义Node类

```python
class LRUCache:
  
    # 内部类：链表的节点
    class Node:
        def __init__(self, key, val):
            self.key = key # 我们需要存 key，这样淘汰时才能从字典里删掉它
            self.val = val
            self.prev = None
            self.next = None

    # 缓存的主体
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 字典：key -> Node
  
        # 哨兵节点：简化边界情况
        self.head = self.Node(0, 0) # "最近使用"的哨兵
        self.tail = self.Node(0, 0) # "最久没用"的哨兵
  
        self.head.next = self.tail
        self.tail.prev = self.head
```

然后我们需要get()和put()两个函数，为了不让这两个函数内出现复杂的prev.next逻辑，我们就需要两个辅助函数：_remove(node) and _add_to_front(node)

首先理解一下get和put操作：get就是通过key去找到value， put就是把一个key和value放进缓存内部。用我的理解来说的话，get就是在双向链表里面进行查找并输出val，但还需要加上一步，把这个键值对从链表中删除并且加到最前面**（最常使用）** put就是如果要放进来的值 的key不在原本的表中，就把这个键值对放进链表里。如果在的话，就用现有的值去替换掉原来的value，当然也要把这个值删掉，并且放在链表的最前面。所说链表的最前面其实就是head.next，最后一个就是tail.prev。

所以先来写两个辅助函数：

```python
def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

  
    def _add_to_front(self, node):
        first_node = self.head.next
        node.prev = self.head
        node.next = first_node
        first_node.prev = node
        self.head.next = node
```

然后补全get和put的逻辑：

```python
    def get(self, key:int):
        node = self.cache.get(key)

        if not node:
            return -1
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key:int, value):
        node = self.cache.get(key)

        if node:
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
```

我觉得这个系统我已经完全理解了，机制和用途我也明白，但就是在具体的代码实现上，有些模糊，还是代码写太少了，现在还是只能在AI辅助下才可以完成这种题。慢慢来，加油～
