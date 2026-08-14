class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ## RC ##
        ## APPROACH : GRAPH DFS ##
        ## EDGE CASE : [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##
        
        def dfs(city):
            while(len(graph[city]) > 0):
                dfs(graph[city].pop(0))
            res.insert(0, city)                  # last airport
            
        graph = collections.defaultdict(list)
        for u, v in (tickets):
            graph[u].append(v)
            graph[u].sort()
        res=[]                
        dfs("JFK")
        return res