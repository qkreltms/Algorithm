'''
'''


def solution(tickets):
    dic = {}
    for key, value in tickets:
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]
    for key in dic.keys():
        dic[key].sort()
    route = ['ICN']
    ans = []
    while route:
        s = route[-1]
        if s not in dic or not dic[s]:
            ans.append(route.pop())
        else:
            route.append(dic[s].pop(0))
    return list(reversed(ans))


print(solution([["ICN", "JFK"], ['HND', 'IAD'], ['JFK', 'HND']]),
      "\n", ['ICN', 'JFK', 'HND', 'IAD'])
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], [
      'ATL', 'SFO']]), "\n", ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'])
print(solution([['ICN', 'B'], ['B', 'ICN'], ['ICN', 'A'], [
      'A', 'D'], ['D', 'A']]), "\n", ['ICN', 'B', 'ICN', 'A', 'D', 'A'])
print(solution([['ICN', 'SFO'], ['SFO', 'ICN'], ['ICN', 'SFO'],
                ['SFO', 'JFK']]), "\n", ['ICN', 'SFO', 'ICN', 'SFO', 'JFK'])
print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'],
                ['A', 'C']]), "\n", ['ICN', 'A', 'ICN', 'A', 'C'])
print(solution([['ICN', 'A'], ['A', 'ICN'], ['A', 'B'],
                ['ICN', 'A']]), "\n", ['ICN', 'A', 'ICN', 'A', 'B'])
print(solution([['ICN', 'BBB'], ['AAA', 'ICN'], ['ICN', 'AAA']]),
      "\n", ['ICN', 'AAA', 'ICN', 'BBB'])
print(solution([['ICN', 'ABB'], ['AAA', 'ICN'], ['ICN', 'AAA'], ['ICN', 'ADD'], [
      'ABB', 'ICN']]), "\n", ['ICN', 'AAA', 'ICN', 'ABB', 'ICN', 'ADD'])
print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['AAA', 'ICN'],
                ['AAA', 'CCC']]), "\n", ['ICN', 'AAA', 'ICN', 'AAA', 'CCC'])
print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['ICN', 'AAA'],
                ['AAA', 'ICN'], ['AAA', 'ICN']]), "\n", ['ICN', 'AAA', 'ICN', 'AAA', 'ICN', 'AAA'])
# 출발지가 항상 첫번째 인덱스는 아니다.
print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]),
      "\n", ['ICN', 'B', 'ICN', 'A'])
print(solution([['ICN', 'A'], ['A', 'C'], ['ICN', 'B'], ['B', 'ICN']]),
      "\n", ['ICN', 'B', 'ICN', 'A', 'C'])
# 백트래킹으로 구현되어있는가?
print(solution([['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], [
      'BOO', 'DOO'], ['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO']]), "\n", ['ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO', 'DOO', 'COO', 'BOO'])
