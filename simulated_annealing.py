import random
import math


def random_solution(bounds):
    return [random.uniform(b[0], b[1]) for b in bounds]


def get_neighbor(solution, bounds, step_size=0.1):
    neighbor = solution[:]
    
    i = random.randint(0, len(solution) - 1)
    neighbor[i] += random.uniform(-step_size, step_size)
    
    # garantir limites
    neighbor[i] = max(bounds[i][0], min(neighbor[i], bounds[i][1]))
    
    return neighbor


def simulated_annealing(objective_function, bounds,
                        n_iterations=100,
                        step_size=0.1,
                        temp=10):
    
    # solução inicial
    current = random_solution(bounds)
    current_eval = objective_function(current)
    
    best = current[:]
    best_eval = current_eval

    for i in range(n_iterations):
        
        # temperatura decrescente (igual ao código original)
        t = temp / float(i + 1)
        
        # gerar vizinho
        candidate = get_neighbor(current, bounds, step_size)
        candidate_eval = objective_function(candidate)
        
        # diferença de custo
        delta = candidate_eval - current_eval
        
        # critério de aceitação
        if delta < 0 or random.random() < math.exp(-delta / t):
            current = candidate
            current_eval = candidate_eval
        
        # atualizar melhor global
        if current_eval < best_eval:
            best = current[:]
            best_eval = current_eval

    return best, best_eval