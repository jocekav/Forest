import dance_step

# This file contains constants of dance steps arrays, and functions that create dance steps/patterns
# The function at the top of this file creates a list of dance_step objects that should be added to
# as dance step arrays are created

ISO_LEFT_S = [0, 0, 20, 0, 45, 0, 0]
ISO_LEFT_T = [2,2,2,2,2,2,2]
ISO_LEFT = dance_step.Dance_Step("ISO_LEFT", dance_step_arr=ISO_LEFT_S, dance_step_t_arr=ISO_LEFT_T)

ISO_RIGHT_S = [0, 0, -20, 0, -45, 0, 0]
ISO_RIGHT_T = [2,2,2,2,2,2,2]
ISO_RIGHT = dance_step.Dance_Step("ISO_RIGHT", dance_step_arr=ISO_RIGHT_S, dance_step_t_arr=ISO_RIGHT_T)

KNOCK_S = [[90, 0, -90],[0, 70, 0, -100, 20],0,[0, 60, 0, -45, 105, -60],0,-1*[0, -120, 70, -70, 70],0]
KNOCK_T = [[4, 24, 4],[4, 8, 8, 6, 6],32,[4, 4, 8, 4, 6, 6],32, [12, 4, 4, 6, 6],32]
KNOCK = dance_step.Dance_Step("KNOCK", dance_step_arr=KNOCK_S, dance_step_t_arr=KNOCK_T)

WAVE_BACK_S = [0,[0, 0, 0, -30, 0],0,[30, 0, 0, 40, -40, 0],0,[30, 0, 60, -60, 0],0]
WAVE_BACK_T = [4,[2, 0.5, 0.5, 0.9, 0.1],4,[2, 0.5, 0.25, 0.5, 0.5, 0.25],4,[2, 0.5, 0.5, 0.5, 0.5],4]
WAVE_BACK = dance_step.Dance_Step("WAVE_BACK", dance_step_arr=WAVE_BACK_S, dance_step_t_arr=WAVE_BACK_T)

WAVE_RIGHT_S = [[-90, 0],[0, 0, 0, -30, 0],0,[30, 0, 0, 40, -40, 0],0,[30, 0, 60, -60, 0],0]
WAVE_RIGHT_T = [[2, 2],[2, 0.5, 0.5, 0.9, 0.1],4,[2, 0.5, 0.25, 0.5, 0.5, 0.25],4,[2, 0.5, 0.5, 0.5, 0.5],4]
WAVE_RIGHT = dance_step.Dance_Step("WAVE_RIGHT", dance_step_arr=WAVE_RIGHT_S, dance_step_t_arr=WAVE_RIGHT_T)

WAVE_LEFT_S = [[90, 0],[0, 0, 0, -30, 0],0,[30, 0, 0, 40, -40, 0],0,[30, 0, 60, -60, 0],0]
WAVE_LEFT_T = [[2, 2],[2, 0.5, 0.5, 0.9, 0.1],4,[2, 0.5, 0.25, 0.5, 0.5, 0.25],4,[2, 0.5, 0.5, 0.5, 0.5],4]
WAVE_LEFT = dance_step.Dance_Step("WAVE_LEFT", dance_step_arr=WAVE_LEFT_S, dance_step_t_arr=WAVE_LEFT_T)

LEAN_BACK_S = [0,[0, 45],0,[30, 0],0,[30, 0],0]
LEAN_BACK_T = [6,[2, 4],6,[2, 4],6,[2, 4],6]
LEAN_BACK = dance_step.Dance_Step("LEAN_BACK", dance_step_arr=LEAN_BACK_S, dance_step_t_arr=LEAN_BACK_T)

DIP_S = [[90, -180],0,[0, 15, -30],[0, -40, 40],0,0,0]
DIP_T = [[2, 6],8,[2, 3, 3],[2, 3, 3],8,8,8]
DIP = dance_step.Dance_Step("DIP", dance_step_arr=DIP_S, dance_step_t_arr=DIP_T)

HEAD_DOWN_S = [0,0,0,0,0,-45,0]
HEAD_DOWN_T = [2,2,2,2,2,2,2]
HEAD_DOWN = dance_step.Dance_Step("HEAD_DOWN", dance_step_arr=HEAD_DOWN_S, dance_step_t_arr=HEAD_DOWN_T)

HEAD_UP_S = [0,0,0,0,0,-45,0]
HEAD_UP_T = [2,2,2,2,2,2,2]
HEAD_UP = dance_step.Dance_Step("HEAD_UP", dance_step_arr=HEAD_UP_S, dance_step_t_arr=HEAD_UP_T)

HEAD_TURN_RIGHT_S = [0,0,0,0,90,0,0]
HEAD_TURN_RIGHT_T = [2,2,2,2,2,2,2]
HEAD_TURN_RIGHT = dance_step.Dance_Step("HEAD_TURN_RIGHT", dance_step_arr=HEAD_TURN_RIGHT_S, dance_step_t_arr=HEAD_TURN_RIGHT_T)

HEAD_TURN_LEFT_S = [0,0,0,0,-90,0,0]
HEAD_TURN_LEFT_T = [2,2,2,2,2,2,2]
HEAD_TURN_LEFT = dance_step.Dance_Step("HEAD_TURN_LEFT", dance_step_arr=HEAD_TURN_LEFT_S, dance_step_t_arr=HEAD_TURN_LEFT_T)

TURN_BIG_RIGHT_S = [90,0,0,0,0,0,0]
TURN_BIG_RIGHT_T = [4,4,4,4,4,4,4]
TURN_BIG_RIGHT = dance_step.Dance_Step("TURN_BIG_RIGHT", dance_step_arr=TURN_BIG_RIGHT_S, dance_step_t_arr=TURN_BIG_RIGHT_T)

TURN_BIG_LEFT_S = [-90,0,0,0,0,0,0]
TURN_BIG_LEFT_T = [4,4,4,4,4,4,4]
TURN_BIG_LEFT = dance_step.Dance_Step("TURN_BIG_LEFT", dance_step_arr=TURN_BIG_LEFT_S, dance_step_t_arr=TURN_BIG_LEFT_T)

TURN_SMALL_RIGHT_S = [0,0,90,0,0,0,0]
TURN_SMALL_RIGHT_T = [4,4,4,4,4,4,4]
TURN_SMALL_RIGHT = dance_step.Dance_Step("TURN_SMALL_RIGHT", dance_step_arr=TURN_SMALL_RIGHT_S, dance_step_t_arr=TURN_SMALL_RIGHT_T)

TURN_SMALL_LEFT_S = [0,0,-90,0,0,0,0]
TURN_SMALL_LEFT_T = [4,4,4,4,4,4,4]
TURN_SMALL_LEFT = dance_step.Dance_Step("TURN_SMALL_LEFT", dance_step_arr=TURN_SMALL_LEFT_S, dance_step_t_arr=TURN_SMALL_LEFT_T)

WAVE_DIAGONAL_LEFT_S = [[-45, 0],[0, 0, 0, -30, 0],0,[30, 0, 0, 40, -40, 0],0,[30, 0, 60, -60, 0],0]
WAVE_DIAGONAL_LEFT_T = [[2, 2],[2, 0.5, 0.5, 0.9, 0.1],4,[2, 0.5, 0.25, 0.5, 0.5, 0.25],4,[2, 0.5, 0.5, 0.5, 0.5],4]
WAVE_DIAGONAL_LEFT = dance_step.Dance_Step("WAVE_DIAGONAL_LEFT", dance_step_arr=WAVE_DIAGONAL_LEFT_S, dance_step_t_arr=WAVE_DIAGONAL_LEFT_T)

WAVE_DIAGONAL_RIGHT_S = [[45, 0],[0, 0, 0, -30, 0],0,[30, 0, 0, 40, -40, 0],0,[30, 0, 60, -60, 0],0]
WAVE_DIAGONAL_RIGHT_T = [[2, 2],[2, 0.5, 0.5, 0.9, 0.1],4,[2, 0.5, 0.25, 0.5, 0.5, 0.25],4,[2, 0.5, 0.5, 0.5, 0.5],4]
WAVE_DIAGONAL_RIGHT = dance_step.Dance_Step("WAVE_DIAGONAL_RIGHT", dance_step_arr=WAVE_DIAGONAL_RIGHT_S, dance_step_t_arr=WAVE_DIAGONAL_RIGHT_T)

SEMI_CIRCLE_S = [[90, -180],0,[0, 15, -30],[0, 40, -40],0,0,0]
SEMI_CIRCLE_T = [[2, 6],8,[2, 3, 3],[2, 3, 3],8,8,8]
SEMI_CIRCLE = dance_step.Dance_Step("SEMI_CIRCLE", dance_step_arr=SEMI_CIRCLE_S, dance_step_t_arr=SEMI_CIRCLE_T)

LEAN_S = [[90, -180],[0, -45],0,[0, 30],0,[0, 75],0]
LEAN_T = [[2, 6],[2, 6],8,[2, 6],8,[2, 6],8]
LEAN = dance_step.Dance_Step("LEAN", dance_step_arr=LEAN_S, dance_step_t_arr=LEAN_T)

CIRCLE_S = [[90, -180, 180],0,[0, 15, -30, -15, 30],[0, 40, -40, -40, 40],0,0,0]
CIRCLE_T = [[2, 6, 6],14,[2, 3, 3, 3, 3],[2, 3, 3, 3, 3],14,14,14]
CIRCLE = dance_step.Dance_Step("CIRCLE", dance_step_arr=CIRCLE_S, dance_step_t_arr=CIRCLE_T)

BLOOM_S = [0,[0, -40],0,[0, 30],0,[-25, 8],0]
BLOOM_T = [11,[1, 10],11,[1, 10],11,[5.5, 5.5],11]
BLOOM = dance_step.Dance_Step("BLOOM", dance_step_arr=BLOOM_S, dance_step_t_arr=BLOOM_T)

ALIVE_S = [0, -30, 0, 30, 0, 0, 0]
ALIVE_T = [4, 4, 4, 4, 4, 4, 4]
ALIVE = dance_step.Dance_Step("ALIVE", dance_step_arr=ALIVE_S, dance_step_t_arr=ALIVE_T)

dance_step_database = [ISO_LEFT, ISO_RIGHT, KNOCK, WAVE_BACK, WAVE_RIGHT, WAVE_LEFT, LEAN_BACK, DIP, HEAD_DOWN, HEAD_UP,
                       HEAD_TURN_RIGHT, HEAD_TURN_LEFT, TURN_BIG_RIGHT, TURN_BIG_LEFT, TURN_SMALL_RIGHT,
                       TURN_SMALL_LEFT, WAVE_DIAGONAL_RIGHT, WAVE_DIAGONAL_LEFT, SEMI_CIRCLE, LEAN, CIRCLE, BLOOM,
                       ALIVE]

# returns a dictionary of dance step objects - keys are the step names
def get_database():
    dance_dict = {}
    for step in dance_step_database:
        step.set_trajectory()
        dance_dict[step.get_name()] = step
    return dance_dict

# dances = get_database()
# print(dances["ISO_LEFT"].get_trajectory()[0])
# ISO_LEFT.set_trajectory()

database = get_database()
# print(database["ISO_LEFT"])
print(dance_step.get_consecutive_trajectories(["ISO_LEFT", "ISO_LEFT"], database)[0])
