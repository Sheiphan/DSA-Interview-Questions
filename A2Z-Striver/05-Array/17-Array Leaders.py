class BruteForce:

    def leaders(self, n, arr):
        ans = []
        for i in range(n):
            flag = True
            for j in range(i + 1, n):
                if arr[j] > arr[i]:
                    flag = False
                    break
            if flag == True:
                ans.append(arr[i])
        return ans


class Optimal:
    #Back-end complete function Template for Python 3

    #Function to find the leaders in the array.
    def leaders(self, n, arr):
        ans = []
        maxx = arr[n - 1]

        #We start traversing the array from last element.
        for i in range(n - 1, -1, -1):
            #Comparing the current element with the maximum element stored.
            #If current element is greater than max, we add the element.
            if arr[i] >= maxx:
                #Updating the maximum element.
                maxx = arr[i]
                #Appending the current element.
                ans.append(maxx)

        #Reversing the array.
        ans.reverse()
        #returning the answer.
        return ans



n = 6
arr = [16, 17, 4, 3, 5, 2]

print(Optimal().leaders(n, arr))
