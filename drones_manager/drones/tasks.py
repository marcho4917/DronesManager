from celery import shared_task
from .models import Drone
import random
from faker import Faker


@shared_task
def update_drone_data():
    drones = Drone.objects.all()

    for drone in drones:
        status = random.choice(['Active', 'Inactive', 'Service', 'Battery charge'])
        if status == 'Service':
            drone.current_location = 'Home'
        else:
            faker = Faker()
            latitude = faker.latitude()
            longitude = faker.longitude()
            drone.current_location = f"{latitude}, {longitude}"
        drone.battery_level = drone.battery_level = random.randint(0, 101)
        drone.save()
