# List of all cities (fixed order)
cities = [
    "Arad", "Zerind", "Oradea", "Sibiu", "Timisoara", "Lugoj", "Mehadia",
    "Dobreta", "Craiova", "Rimnicu Vilcea", "Fagaras", "Pitesti",
    "Bucharest", "Giurgiu", "Urziceni", "Vaslui", "Hirsova",
    "Eforie", "Iasi", "Neamt"
]

# Map each city to its index for easy lookup
city_index = {city: i for i, city in enumerate(cities)}

# Initialize matrix with None (no edge)
n = len(cities)
matrix = [[None for _ in range(n)] for _ in range(n)]

# Set diagonal to 0
for i in range(n):
    matrix[i][i] = 0

# List of undirected edges
edges = [
    ("Arad", "Zerind", 75),
    ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118),
    ("Zerind", "Oradea", 71),
    ("Oradea", "Sibiu", 151),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Dobreta", 75),
    ("Dobreta", "Craiova", 120),
    ("Craiova", "Pitesti", 138),
    ("Craiova", "Rimnicu Vilcea", 146),
    ("Sibiu", "Fagaras", 99),
    ("Sibiu", "Rimnicu Vilcea", 80),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Fagaras", "Bucharest", 211),
    ("Pitesti", "Bucharest",101),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Vaslui", 142),
    ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Eforie", 86),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87),
]

# Fill adjacency matrix
for a, b, w in edges:
    i, j = city_index[a], city_index[b]
    matrix[i][j] = w
    matrix[j][i] = w

# Optional: print matrix nicely
for row in matrix:
    print(row)