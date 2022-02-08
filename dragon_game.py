
def main():
    health = 100
    finish = False
    while not finish:
        print('My health', health, '. Hit me!')
        damage = int(input())
        health -= damage


main()

        
