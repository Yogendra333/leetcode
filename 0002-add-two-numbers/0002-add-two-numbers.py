class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) :
        curr = head = ListNode(0)
        nums1 = []
        nums2 = []
        number1 = 0
        number2 = 0
        while l1:
            nums1.append(l1.val)
            l1 = l1.next
        while l2:
            nums2.append(l2.val)
            l2 = l2.next
        nums1.reverse()
        nums2.reverse()
        for i in range(len(nums1)):
            if i == 0: number1 = nums1[i]
            else: number1 = number1 * 10 + nums1[i]
        for i in range(len(nums2)):
            if i == 0: number2 = nums2[i]
            else: number2 = number2 * 10 + nums2[i]
        sum_nums = [int(char) for char in str(number1 + number2)]
        sum_nums.reverse()
        for element in sum_nums:
            curr.next = ListNode(element)
            curr = curr.next
        curr.next = None
        return head.next