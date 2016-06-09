from tkinter import *

class Stats():
    def __init__(self):
        # self.bela = bela
        # self.boss = boss
        # self.x = 850
        # self.y = 100
        pass

    def draw_stat(self, canvas, enemy, x, y):
        self.stat = 'Hero (Level ' + str(enemy.level) + ') HP: ' + str(enemy.current_hp) + '/' + str(enemy.max_hp) + ' | DP: ' + str(enemy.defend_point) + ' | SP: ' + str(enemy.strike_point)
        canvas.create_text(x, y, text = self.stat)

    #
    # def draw_hero_stat(self, canvas):
    #     self.stat = 'Hero (Level ' + str(self.bela.level) + ') HP: ' + str(self.bela.current_hp) + '/' + str(self.bela.max_hp) + ' | DP: ' + str(self.bela.defend_point) + ' | SP: ' + str(self.bela.strike_point)
    #     canvas.create_text(self.x, self.y, text = self.stat)
    #
    # def draw_boss_stat(self, canvas):
    #     self.stat = 'Boss (Level ' + str(self.boss.level) + ') HP: ' + str(self.boss.current_hp) + '/' + str(self.boss.max_hp) + ' | DP: ' + str(self.boss.defend_point) + ' | SP: ' + str(self.boss.strike_point)
    #     canvas.create_text(self.x, self.y + 100, text = self.stat)
