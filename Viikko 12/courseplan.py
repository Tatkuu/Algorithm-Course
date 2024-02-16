from collections import deque

class CoursePlan:
    def __init__(self):
        self.graph = {}  # dictionary esitietovaatimusten tallentamiseen
        self.courses = set()  # joukko kaikista kursseista

    def add_course(self, course):
        self.courses.add(course)
        if course not in self.graph:
            self.graph[course] = set()

    def add_requisite(self, course1, course2):
        # lisätään kaaret esitietovaatimuksista
        self.add_course(course1)
        self.add_course(course2)
        self.graph[course1].add(course2)

    def find(self):
        # lasketaan jokaisen solmun saapuvien kaarien määrä (in-degree)
        indegree = {course: 0 for course in self.courses}
        for course in self.graph:
            for requisite in self.graph[course]:
                indegree[requisite] += 1

        # lisätään solmut, joilla on in-degree 0 jonoon
        queue = deque(course for course in indegree if indegree[course] == 0)
        order = []  # lista kursseista järjestyksessä
        while queue:
            # poistetaan solmu jonosta
            course = queue.popleft()
            order.append(course)
            # vähennetään esitietovaatimuksia solmun naapureilta
            for requisite in self.graph[course]:
                indegree[requisite] -= 1
                # jos naapurilla ei ole jäljellä saapuvia kaaria, lisätään se jonoon
                if indegree[requisite] == 0:
                    queue.append(requisite)

        # jos jokainen kurssi lisättiin järjestyksessä listaan, palautetaan lista
        if len(order) == len(self.courses):
            return order
        else:
            return None

if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe","Ohja")
    c.add_requisite("Ohja","Tira")
    c.add_requisite("Jym","Tira")
    print(c.find()) # [Ohpe,Jym,Ohja,Tira]
    c.add_requisite("Tira","Tira")
    print(c.find()) # None
