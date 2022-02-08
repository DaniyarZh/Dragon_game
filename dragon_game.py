class Dragon:
    def create(self):
        self.health = 100
        
    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def talk(self):
        print('My health', self.health, '. Hit me!')

    
def main():
    dragon = Dragon()
    dragon.create()
    finish = False
    while not finish:
        dragon.talk()
        damage = int(input())
        dragon.get_damage(damage)
        if not dragon.is_alive():
            finish = True

    print('YOu win')


main()

        
