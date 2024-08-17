colors=['red','blue','green','yellow','black']
states=['andhra','karnataka','tamilnadu','kerela']
neighbors={}
neighbors['andhra']=['karnataka','tamilnadu']
neighbors['karnataka']=['andhra','tamilnadu','kerela']
neighbors['tamilnadu']=['andhra','kerela','karnataka']
neighbors['kerela']=['karnataka','tamilnadu']
colors_of_states={}
def promising(state,color):
    for neighbor in neighbors.get(state):
        colors_of_neighbor=colors_of_states.get(neighbor)
        if colors_of_neighbor==color:
            return False
    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state,color):
            return color

def main():
    for state in states:
        colors_of_states[state]=get_color_for_state(state)
    print(colors_of_states)

main()
