# reflex agent
def VacuumAgent(percept_sequence):
    recent_action = None
    for pair in percept_sequence:
        if pair[1] == "Dirty":
            recent_action = "Suck"
        else:
            if pair[0] == "A":
                recent_action = "Right"
            else:
                recent_action = "Left"

    return recent_action

def main():
    percept_sequence = [["A","Clean"], [["A","Clean"], ["B","Clean"]]]

    print(VacuumAgent(percept_sequence))