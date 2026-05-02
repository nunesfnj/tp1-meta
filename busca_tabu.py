import random


def random_solution(bounds):
    return [random.uniform(b[0], b[1]) for b in bounds]


def get_neighbors(solution, bounds, step=0.1):
    neighbors = []
    
    for i in range(len(solution)):
        for delta in [-step, step]:
            neighbor = solution[:]
            neighbor[i] += delta
            
            neighbor[i] = max(bounds[i][0], min(neighbor[i], bounds[i][1]))
            neighbors.append(neighbor)
    
    return neighbors


def tabu_search(objective_function, bounds, max_iter=200, tabu_size=15):
    
    current = random_solution(bounds)
    best = current[:]
    tabu_list = []

    for _ in range(max_iter):
        neighbors = get_neighbors(current, bounds)
        
        best_neighbor = None
        best_value = float('inf')
        
        for n in neighbors:
            if n not in tabu_list:
                val = objective_function(n)
                
                if val < best_value:
                    best_neighbor = n
                    best_value = val
        
        if best_neighbor is None:
            break
        
        current = best_neighbor
        tabu_list.append(best_neighbor)
        
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        
        if objective_function(current) < objective_function(best):
            best = current[:]

    return best, objective_function(best)