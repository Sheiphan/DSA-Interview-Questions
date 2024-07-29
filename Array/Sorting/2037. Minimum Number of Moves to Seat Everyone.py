class Solution:
    def minMovesToSeat(self, seats, students) -> int:
        # Sort the seats and students
        seats = self.quickSort(seats)
        students = self.quickSort(students)

        # Initialize the total moves counter
        total_moves = 0

        # Calculate the total number of moves
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)

        return total_moves

    def quickSort(self, arr):
        if len(arr)<=1:
            return arr

        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.quickSort(left) + middle + self.quickSort(right)
        

seats = [3, 1, 5]
students = [2, 7, 4]
s = Solution()
print(s.minMovesToSeat(seats, students))
