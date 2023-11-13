print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
keyboard.row_pins = (board.GP14, board.GP15, board.GP16, board.GP17, board.GP18)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [ #qwerty
        KC.ESC,  KC.N1, KC.N2,   KC.N3,   KC.N4, KC.N5, KC.N6,  KC.N7,  KC.N8,   KC.N9,   KC.N0,    KC.MINS, KC.EQL,  KC.BSPC,
        KC.GRV,  KC.Q,  KC.W,    KC.E,    KC.R,  KC.T,  KC.Z,   KC.U,   KC.I,    KC.O,    KC.P,     KC.LBRC, KC.RBRC, KC.BSLS,
        KC.TAB,  KC.A,  KC.S,    KC.D,    KC.F,  KC.G,  KC.H,   KC.J,   KC.K,    KC.L,    KC.SCLN,  KC.QUOT, KC.NO,   KC.ENT,
        KC.LSFT, KC.Y,  KC.X,    KC.C,    KC.V,  KC.B,  KC.N,   KC.M,   KC.COMM, KC.DOT,  KC.SLASH, KC.NO,   KC.UP,   KC.RSFT,
        KC.LCTL, KC.NO, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.SPC, KC.NO,   KC.RALT, KC.RCTL,  KC.LEFT, KC.DOWN, KC.RIGHT
        ]
]

if __name__ == '__main__':
    keyboard.go()