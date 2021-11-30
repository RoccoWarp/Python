from time import sleep
from colorama import Fore


class TrafficLight:

    def start(self, red_colors, yellow_colors, green_colors):
        self.red_colors = red_colors
        sleep(5)
        print(Fore.RED + 'Red')
        self.yellow_colors = yellow_colors
        sleep(3)
        print(Fore.YELLOW + 'Yellow')
        sleep(2)
        self.green_colors = green_colors
        print(Fore.GREEN + 'Green')


my_trafficlight = TrafficLight()
my_trafficlight.start('red', 'yellow', 'green')
