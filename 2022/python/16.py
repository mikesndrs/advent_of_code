"""https://adventofcode.com/2022/day/16"""
import re


class volcano_room:
    def __init__(self, valve_name, flow_rate, connected_tunnels):
        self.valve_name = valve_name
        self.flow_rate = flow_rate
        self.connected_tunnels = connected_tunnels
        self.on = False

    def turn_on(self, idx):
        self.on = idx


def main():
    input_filename = "2022/inputs/16.txt"
    match_line = "Valve (.*) has flow rate=(.*); tunnels lead to valves (.*)"
    rooms = []
    with open(input_filename) as f:
        for line in f:
            match = re.search(match_line, line.strip())
            valve_name = match.group(1)
            flow_rate = int(match.group(2))
            connected_tunnels = match.group(3).split(", ")
            rooms.append(volcano_room(valve_name, flow_rate, connected_tunnels))


if __name__ == "__main__":
    main()
