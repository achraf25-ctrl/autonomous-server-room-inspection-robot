#!/usr/bin/env python3
"""
Planification de la tournée d'inspection = variante du Traveling Salesman
Problem (TSP) : trouver l'ordre de visite des racks qui minimise la distance
totale parcourue par le robot, en partant de sa position de départ.

Implémentation pure Python (aucune dépendance lourde) :
  1. Heuristique du plus proche voisin (nearest neighbor) pour une première
     solution rapide.
  2. Amélioration locale par 2-opt jusqu'à convergence.

Ce module est utilisable :
  - en standalone : `python3 tsp_planner.py` (affiche l'ordre optimisé)
  - importé depuis inspection_commander.py côté ROS2

Lien avec le cours de Recherche Opérationnelle : le TSP est NP-difficile ;
sur une douzaine de points, une heuristique 2-opt donne une solution à
quelques % de l'optimal en temps quasi instantané, ce qui est largement
suffisant ici (le point n'est pas l'optimalité absolue mais d'éviter les
allers-retours inutiles dans les couloirs étroits entre racks).
"""

import math
import os
from typing import List, Tuple, Dict

try:
    import yaml
except ImportError:
    yaml = None


Point = Dict[str, float]


def euclidean(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def load_inspection_points(yaml_path: str) -> Tuple[Tuple[float, float], List[Point]]:
    """Charge inspection_points.yaml. Retourne (start_xy, liste_de_points)."""
    if yaml is None:
        raise RuntimeError("PyYAML n'est pas installé (pip install pyyaml).")

    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    points = data["inspection_points"]
    start = data["start_pose"]
    start_xy = (start["x"], start["y"])
    return start_xy, points


def nearest_neighbor_order(start_xy: Tuple[float, float], points: List[Point]) -> List[int]:
    """Retourne les indices des points dans l'ordre du plus proche voisin."""
    remaining = list(range(len(points)))
    order = []
    current = start_xy

    while remaining:
        next_idx = min(
            remaining,
            key=lambda i: euclidean(current, (points[i]["x"], points[i]["y"])),
        )
        order.append(next_idx)
        current = (points[next_idx]["x"], points[next_idx]["y"])
        remaining.remove(next_idx)

    return order


def tour_length(start_xy: Tuple[float, float], points: List[Point], order: List[int]) -> float:
    total = 0.0
    current = start_xy
    for idx in order:
        nxt = (points[idx]["x"], points[idx]["y"])
        total += euclidean(current, nxt)
        current = nxt
    return total


def two_opt(start_xy: Tuple[float, float], points: List[Point], order: List[int]) -> List[int]:
    """Amélioration locale 2-opt : inverse des segments tant que ça raccourcit le tour."""
    best = order[:]
    best_len = tour_length(start_xy, points, best)
    improved = True

    while improved:
        improved = False
        for i in range(len(best) - 1):
            for j in range(i + 1, len(best)):
                candidate = best[:i] + best[i:j + 1][::-1] + best[j + 1:]
                candidate_len = tour_length(start_xy, points, candidate)
                if candidate_len < best_len - 1e-9:
                    best, best_len = candidate, candidate_len
                    improved = True
    return best


def solve_tsp(start_xy: Tuple[float, float], points: List[Point]) -> Tuple[List[Point], float]:
    """API principale : retourne (points_dans_l_ordre_optimise, distance_totale)."""
    order = nearest_neighbor_order(start_xy, points)
    order = two_opt(start_xy, points, order)
    ordered_points = [points[i] for i in order]
    return ordered_points, tour_length(start_xy, points, order)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    yaml_path = os.path.join(here, "..", "config", "inspection_points.yaml")
    yaml_path = os.path.normpath(yaml_path)

    start_xy, points = load_inspection_points(yaml_path)
    ordered_points, total_distance = solve_tsp(start_xy, points)

    print(f"Point de départ : {start_xy}")
    print(f"{len(ordered_points)} racks à inspecter — distance totale optimisée : "
          f"{total_distance:.2f} m\n")
    print("Ordre de la tournée d'inspection :")
    for rank, p in enumerate(ordered_points, start=1):
        print(f"  {rank:2d}. {p['id']:10s} (x={p['x']:.1f}, y={p['y']:.1f})")


if __name__ == "__main__":
    main()
