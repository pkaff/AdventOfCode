import re
import functools

class Blueprint:
    def __init__(self, input_line):
        self.id = input_line[0]
        self.ore_robot_cost = input_line[1]
        self.clay_robot_cost = input_line[2]
        self.obs_robot_cost = tuple(input_line[3:5])
        self.geo_robot_cost = tuple(input_line[5:7])
        self.max_ore_consumption = max([self.ore_robot_cost, self.clay_robot_cost, self.obs_robot_cost[0], self.geo_robot_cost[0]])
        self.max_clay_consumption = self.obs_robot_cost[1]
    def __eq__(self, other):
        return self.id == other.id and self.ore_robot_cost == other.ore_robot_cost and self.clay_robot_cost == other.clay_robot_cost and self.obs_robot_cost == other.obs_robot_cost and self.geo_robot_cost == other.geo_robot_cost
    def __hash__(self):
        return hash((self.id, self.ore_robot_cost, self.clay_robot_cost, self.obs_robot_cost, self.geo_robot_cost))

@functools.lru_cache(maxsize=None)
def run_blueprint(blueprint, ore_robots, clay_robots, obs_robots, n_ore, n_clay, n_obs, time_left):
    geo_robot_ore_cost, geo_robot_obs_cost = blueprint.geo_robot_cost
    obs_robot_ore_cost, obs_robot_clay_cost = blueprint.obs_robot_cost
    clay_robot_cost = blueprint.clay_robot_cost
    ore_robot_cost = blueprint.ore_robot_cost
    max_ore_consumption = blueprint.max_ore_consumption
    max_clay_consumption = blueprint.max_clay_consumption

    if time_left == 1:
        return 0

    new_n_ore = n_ore + ore_robots
    new_n_clay = n_clay + clay_robots
    new_n_obs = n_obs + obs_robots

    max_geodes = 0
    if n_ore >= geo_robot_ore_cost and n_obs >= geo_robot_obs_cost:
        max_geodes = run_blueprint(blueprint, ore_robots, clay_robots, obs_robots, new_n_ore - geo_robot_ore_cost, new_n_clay, new_n_obs - geo_robot_obs_cost, time_left - 1)
        return max_geodes + time_left - 1
    if n_ore >= obs_robot_ore_cost and n_clay >= obs_robot_clay_cost:
        max_geodes = max(max_geodes, run_blueprint(blueprint, ore_robots, clay_robots, obs_robots + 1, new_n_ore - obs_robot_ore_cost, new_n_clay - obs_robot_clay_cost, new_n_obs, time_left - 1))
    if n_ore >= clay_robot_cost and clay_robots < max_clay_consumption:
        max_geodes = max(max_geodes, run_blueprint(blueprint, ore_robots, clay_robots + 1, obs_robots, new_n_ore - clay_robot_cost, new_n_clay, new_n_obs, time_left - 1))
    if n_ore >= ore_robot_cost and ore_robots < max_ore_consumption:
        max_geodes = max(max_geodes, run_blueprint(blueprint, ore_robots + 1, clay_robots, obs_robots, new_n_ore - ore_robot_cost, new_n_clay, new_n_obs, time_left - 1))
    # Don't create a robot and save resources
    max_geodes = max(max_geodes, run_blueprint(blueprint, ore_robots, clay_robots, obs_robots, new_n_ore, new_n_clay, new_n_obs, time_left - 1))

    return max_geodes

input = list(map(Blueprint, [list(map(int, re.findall(r'\d+', line.strip('\n')))) for line in open("input.txt", "r").readlines()]))[:3]

res = 1
for blueprint in input:
    res *= run_blueprint(blueprint, 1, 0, 0, 0, 0, 0, 32)
print(res)
