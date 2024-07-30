class Solution:
    def mergeSimilarItems(self, items1, items2):
        self.sort2DArray(items1)
        self.sort2DArray(items2)

        ret = []
        i = j = 0
        while i < len(items1) and j < len(items2):
            if items1[i][0] == items2[j][0]:
                ret.append([items1[i][0], items1[i][1] + items2[j][1]])
                i += 1
                j += 1
            elif items1[i][0] < items2[j][0]:
                ret.append(items1[i])
                i += 1
            else:
                ret.append(items2[j])
                j += 1
        while i < len(items1):
            ret.append(items1[i])
            i+=1
        while j < len(items2):
            ret.append(items2[j])
            j+=1

        return ret

    def sort2DArray(self, arr):
        n = len(arr)
        for k in range(n):
            i = 0
            j = 1
            while i < (n - k - 1) and j < (n - k):
                if arr[i][0] > arr[j][0]:
                    arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1

    def merge_and_sort_items(items1, items2):
        # Step 1: Merge items2 into items1
        for item in items2:
            items1.append(item)

        # Step 2: Create a dictionary to aggregate values based on keys
        aggregated_items = {}
        for item in items1:
            key = item[0]
            value = item[1]
            if key in aggregated_items:
                aggregated_items[key] += value
            else:
                aggregated_items[key] = value

        # Step 3: Convert the dictionary back into a list of lists
        aggregated_list = []
        for key, value in aggregated_items.items():
            aggregated_list.append([key, value])

        # Step 4: Sort the aggregated list by keys
        sorted_aggregated_list = sorted(aggregated_list)

        return sorted_aggregated_list


items1 = [[1, 1], [4, 5], [3, 8]]
items2 = [[3, 1], [1, 5]]

items1 = [[5,1],[4,2],[3,3],[2,4],[1,5]]
items2 = [[7,1],[6,2],[5,3],[4,4]]



s = Solution()
print(s.mergeSimilarItems(items1, items2))
