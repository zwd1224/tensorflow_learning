# """
# 题目描述：合并区间
# 给出一个区间的列表集合，请合并所有重叠的区间。

# 示例：
# 输入: 
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

# 要求：实现一个函数，输入为一个区间集合，输出为合并后的区间集合。
# def merge_intervals(intervals):
#     """合并所有重叠的区间，并返回一个不重叠的区间列表。"""
#     pass
#     return merged
# """

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key = lambda x : x[0])
ans = [intervals[0]]
for i in intervals:
    start = i[0]
    end = i[1]
    if start > ans[-1][1]:
        ans.append([start,end])
    if end > ans[-1][1]:
        ans[-1][1] = end
print(ans)