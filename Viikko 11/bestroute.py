import heapq

class BestRoute:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_road(self,a,b,x):
        # lisää tie solmujen a ja b välillä, jonka pituus on x
        self.graph[a-1].append((b-1,x))
        self.graph[b-1].append((a-1,x))

    def find_route(self,a,b):
        # etsi lyhin reitti solmujen a ja b välillä
        dist = [float('inf')] * self.n
        dist[a-1] = 0
        pq = [(0,a-1)]

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, weight in self.graph[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
                    heapq.heappush(pq, (dist[neighbor], neighbor))

        return dist[b-1] if dist[b-1] < float('inf') else -1

if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1,2,2)
    print(b.find_route(1,3)) # -1
    b.add_road(1,3,5)
    print(b.find_route(1,3)) # 5
    b.add_road(2,3,1)
    print(b.find_route(1,3)) # 3
