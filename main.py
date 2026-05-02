import math
import numpy as np
import matplotlib.pyplot as plt

from busca_tabu import tabu_search
from simulated_annealing import simulated_annealing


# =========================
# FUNÇÕES OBJETIVO
# =========================

def objective_function_1(solution):
    x1, x2 = solution
    return 100 * math.sqrt(abs(x2 - 0.01 * x1**2)) + 0.01 * abs(x1 + 10)


def objective_function_2(solution, m=10):
    x1, x2 = solution
    total = 0
    
    for i, x in enumerate([x1, x2], start=1):
        total += math.sin(x) * (math.sin((i * x**2) / math.pi))**(2 * m)
    
    return -total


# =========================
# EXPERIMENTOS
# =========================

def run_experiments(algorithm, objective_function, bounds):
    results = []
    
    best_global_sol = None
    best_global_val = float('inf')
    
    for _ in range(30):
        sol, val = algorithm(objective_function, bounds)
        results.append(val)
        
        if val < best_global_val:
            best_global_val = val
            best_global_sol = sol
    
    return results, best_global_sol, best_global_val


def print_stats(results):
    print("Min:", np.min(results))
    print("Max:", np.max(results))
    print("Mean:", np.mean(results))
    print("Std:", np.std(results))


def plot_boxplot(results, title):
    plt.boxplot(results)
    plt.title(title)
    plt.show()


# =========================
# EXECUÇÃO
# =========================

problems = {
    "1a": (objective_function_1, [(-15, -5), (-3, 3)]),
    "1b": (objective_function_1, [(-11, -9), (0, 2)]),
    "2c": (objective_function_2, [(0, math.pi), (0, math.pi)]),
    "2d": (objective_function_2, [(1, 2.5), (1, 2.5)])
}


for name, (func, bounds) in problems.items():
    
    print(f"\n===== Problema {name} =====")
    
    # TABU
    r_tabu, sol_tabu, val_tabu = run_experiments(tabu_search, func, bounds)
    
    print("\n--- Tabu Search ---")
    print_stats(r_tabu)
    print("Melhor solução:", sol_tabu)
    print("Melhor valor:", val_tabu)
    plot_boxplot(r_tabu, f"Tabu - {name}")
    
    # SA
    r_sa, sol_sa, val_sa = run_experiments(simulated_annealing, func, bounds)
    
    print("\n--- Simulated Annealing ---")
    print_stats(r_sa)
    print("Melhor solução:", sol_sa)
    print("Melhor valor:", val_sa)
    plot_boxplot(r_sa, f"SA - {name}")