class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.itinerary = []
        
        tickets.sort()
        visit_map = defaultdict(list)
        city_map = defaultdict(list)
        for ticket in tickets:
            city_map[ticket[0]].append(ticket[1]) 
            visit_map[ticket[0]].append(0)        
        print(city_map)

        def dfs(city):
            #curr_itinerary.append(city)
            self.itinerary.append(city)
            if len(self.itinerary)==len(tickets)+1:
                return True
            
            for i, next_city in enumerate(city_map[city]):
                
                if visit_map[city][i]==0:
                    visit_map[city][i]=1
                    ret = dfs(next_city)
                    visit_map[city][i]=0
                    if ret:
                        return True
            self.itinerary.pop()
        
        curr_city = "JFK"
        dfs(curr_city)
        return self.itinerary