def straight(t=None): 

    v_left = 0.2
    v_right = 0.2

    return v_left, v_right


def turning(t=None):
    v_left = 0.1
    v_right = 0.2

    return v_left, v_right


def spinning(t=None):
    v_left = -0.15
    v_right = 0.15

    return v_left, v_right

def stop(t=None):
    v_left = 0
    v_right = 0

    return v_left, v_right

