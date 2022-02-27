PLAYER1 = 1
PLAYER2 = -1

AREA = {
    PLAYER1: {
        'next': {
            'axis': {'x1': 180, 'x2': 196, 'y1': 56, 'y2': 71},
            'child': {'x1': 180, 'x2': 196, 'y1': 41, 'y2': 56},
        },
        'next_next': {
            'axis': {'x1': 194, 'x2': 206, 'y1': 86, 'y2': 97},
            'child': {'x1': 194, 'x2': 206, 'y1': 74, 'y2': 85},
        }
    },
    PLAYER2: {
        'next': {
            'axis': {'x1': 284, 'x2': 300, 'y1': 56, 'y2': 71},
            'child': {'x1': 284, 'x2': 300, 'y1': 41, 'y2': 56},
        },
        'next_next': {
            'axis': {'x1': 274, 'x2': 286, 'y1': 86, 'y2': 97},
            'child': {'x1': 274, 'x2': 286, 'y1': 74, 'y2': 85},
        }
    }
}

COLOR_RANGE = {
    'r': {
        'blue': {'lower': 96, 'upper': 133},
        'green': {'lower': 90, 'upper': 132},
        'red': {'lower': 160, 'upper': 210},
    },
    'g': {
        'blue': {'lower': 92, 'upper': 123},
        'green': {'lower': 193, 'upper': 217},
        'red': {'lower': 111, 'upper': 143},
    },
    'b': {
        'blue': {'lower': 192, 'upper': 220},
        'green': {'lower': 133, 'upper': 156},
        'red': {'lower': 86, 'upper': 115},
    },
    'y': {
        'blue': {'lower': 118, 'upper': 143},
        'green': {'lower': 180, 'upper': 203},
        'red': {'lower': 194, 'upper': 239},
    },
    'p': {
        'blue': {'lower': 190, 'upper': 218},
        'green': {'lower': 93, 'upper': 126},
        'red': {'lower': 145, 'upper': 181},
    },
    'n': {
        'blue': {'lower': 192, 'upper': 194},
        'green': {'lower': 189, 'upper': 191},
        'red': {'lower': 189, 'upper': 191},
    },
}
