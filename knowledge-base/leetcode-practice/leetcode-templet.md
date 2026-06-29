# [题目名称] - [难度] (例如：环形链表 - 简单)

## 1. 我遇到的困惑（动手写笔记的第一步）
我当时的真实想法是什么？
（示例：我完全看不懂链表里的环是什么东西，不知道为什么快慢指针能判断环。）

## 2. 参考的题解/教程来源
（示例：我是看了 B站 [某某] 的视频，或者力扣官方题解里 [某某] 的 Python 解法才懂的。）

## 3. 这道题到底在考什么？（核心知识点提炼）
（示例：考的是链表指针的移动速度和“追及问题”。如果有环，快指针一定会和慢指针相遇。）

## 4. 手抄官方解法（比看十遍都管用）
我在本地跑通的完整代码：

```python
# 把你的代码完整粘贴在这里
def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```