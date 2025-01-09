class UndergroundSystem:

    def __init__(self):
        
        self.checkInMap = {} # maps Traveller ID to (Start Station, Start Time)
        self.totalMap = {} # maps route i.e (startStation, endStation) to [totalTime, Count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, time = self.checkInMap[id]
        route = (startStation, stationName)
        if route not in self.totalMap:
            self.totalMap[route] = [0,0]
        self.totalMap[route][1] +=1
        self.totalMap[route][0] += t - time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)