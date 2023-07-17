import random
import pygame
import time
# import math
import threading
# import firebase 

pygame.init()

total_vehicle_count = 0
def currentTime():
    global timeString

    hours = 17
    minutes = 59
    seconds = 0

    while True:
        seconds = seconds + 1

        timeString = f"{seconds}"
        time.sleep(1)

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


road = pygame.image.load("road.png")
truck = pygame.image.load("truck.png")
grass = scale_image(pygame.image.load("grass.png"), 0.45)
bike = pygame.image.load("bike.png")
car = pygame.image.load("car.png")
stra = pygame.image.load("newstr.png")
stra2 = pygame.image.load("on.png")
ca = pygame.image.load("car.png")
# red = pygame.image.load("newred1.png")

width, height = 1000, 590
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Simulation")

car_positions = []
bike_positions = []
truck_positions = []
car_count = 0
truck_count = 0
bike_count = 0
fps = 160 
def swap_images():
    global stra, stra2
    while True:
        if car_count or bike_count or truck_count >= 1:
            stra = pygame.image.load("on.png")
            # stra2 = pygame.image.load("on.png")
        else:
            # stra = pygame.image.load("on.png")
            stra2 = pygame.image.load("newstr.png")
        time.sleep(0.1)
def save_DAta():
    with open("data.txt", 'a') as file:
        file.write(f"{timeString} {total_vehicle_count}\n")
        time.sleep(1)


lock = threading.Lock()

t = threading.Thread(target=swap_images)
t.daemon = True
t.start()

t2 = threading.Thread(target=currentTime)
t2.daemon = True
t2.start()



run = True
clock = pygame.time.Clock()

while run:
    screen.blit(road, (0, 70))
    screen.blit(road, (200, 70))
    screen.blit(road, (400, 70))
    screen.blit(road, (600, 70))
    screen.blit(grass, (0, 0))
    screen.blit(grass, (150, 0))
    screen.blit(grass, (300, 0))
    screen.blit(grass, (400, 0))
    screen.blit(grass, (500, 0))
    screen.blit(grass, (600, 0))
    screen.blit(grass, (700, 0))
    screen.blit(grass, (830, 0))
    screen.blit(grass, (830, 0))
    screen.blit(grass, (830, 400))
    screen.blit(grass, (700, 400))
    screen.blit(grass, (600, 400))
    screen.blit(grass, (500, 400))
    screen.blit(grass, (400, 400))
    screen.blit(grass, (300, 400))
    screen.blit(grass, (150, 400))
    screen.blit(grass, (0, 400))
    
    if random.randint(1, 500) == 1:
        car_positions.append([-50, random.randint(200, 380)])
        
    if random.randint(1, 500) == 1:
        truck_positions.append([-50, random.randint(200, 380)])
    if random.randint(1, 500) == 1:
        bike_positions.append([-50, random.randint(200, 380)])
       
    for i in range(len(car_positions)):
        car_position = car_positions[i]
        car_position[0] += 4
        # print(car_positions)
        # firebase.send_data(len(car_positions))
        screen.blit(car, car_position)

        if car_position[0] > 0 :
           car_count = 1
        
        
        if car_position[0] > width:
            car_positions.pop(i)
            car_count += 1
            break
    for i in range(len(truck_positions)):
        truck_position = truck_positions[i]
        truck_position[0] += 4
        # print(car_positions)
        # firebase.send_data(len(car_positions))
        screen.blit(truck, truck_position)

        if truck_position[0] > 0 :
           truck_count = 1
        
        
        if truck_position[0] > width:
            truck_positions.pop(i)
            truck_count += 1
            break
    for i in range(len(bike_positions)):
        bike_position = bike_positions[i]
        bike_position[0] += 4
        # print(car_positions)
        # firebase.send_data(len(car_positions))
        screen.blit(bike, bike_position)

        if bike_position[0] > 0 :
           bike_count = 1
        
        
        if bike_position[0] > width:
            bike_positions.pop(i)
            bike_count += 1
            break

    font = pygame.font.Font(None, 36)
    total_vehicle_count = len(car_positions) + len(bike_positions) + len(truck_positions)
    if total_vehicle_count >= 1 :
        screen.blit(stra, (0, 80))
        screen.blit(stra, (870, 80))
        screen.blit(stra, (260, 80))
        screen.blit(stra, (470, 80))
        screen.blit(stra, (670, 80))
        # screen.blit(red, (850, 80))
        camera_text = font.render("Camera On",True,(0, 0, 0))
    else:
        
        screen.blit(stra2, (0, 80))
        screen.blit(stra2, (870, 80))
        screen.blit(stra2, (260, 80))
        screen.blit(stra2, (470, 80))
        screen.blit(stra2, (670, 80))
        camera_text = font.render("Camera Off",True,(245,19,2))
    clock.tick(160)    
    car_count_text = font.render("Real Vehicle Count: " + str(total_vehicle_count), True, (0,0,0))

    t3 = threading.Thread(target=save_DAta)
    t3.daemon = True
    t3.start()


    screen.blit(car_count_text, (10, 10))
    screen.blit(camera_text, (850, 10))
    
    # print(car_positions)
    pygame.display.flip()  # update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check if user clicked the window
            run = False
