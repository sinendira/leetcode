class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        first_max_height=[0]*(n)
        second_max_height=[-1]*(n)
        dp_up=[0]*(n)
        def dfs_down(node,parent):
            heights=[]
            for nxt_node in adj[node]:
                if nxt_node!=parent:
                    dfs_down(nxt_node,node)
                    heights.append(first_max_height[nxt_node]+1)
                    # if second_max_height[nxt_node]!=-1:
                    #     heights.append(second_max_height[nxt_node]+1)
            heights.sort(reverse=True)
            if len(heights)>0:
                first_max_height[node]=heights[0]
            if len(heights)>1:
                second_max_height[node]=heights[1]
        dfs_down(0,-1)
        print(first_max_height)
        print(second_max_height)
        def dfs_up(node,parent):
            if parent!=-1:
                dp_up[node]=max(dp_up[parent]+1,dp_up[node])
                dp_up[node]=max(dp_up[node],first_max_height[parent]+1 if first_max_height[parent]!=first_max_height[node]+1 else second_max_height[parent]+1)
            for nxt_node in adj[node]:
                if nxt_node!=parent:
                    dfs_up(nxt_node,node)
        dfs_up(0,-1)
        print(first_max_height)
        print(dp_up)
        ans=[0]*(n)
        for i in range(n):
            ans[i]=max(first_max_height[i],dp_up[i])
        min_val=min(ans)
        fans=[]
        for i in range(n):
            if ans[i]==min_val:
                fans.append(i)
        return fans