from datetime import datetime
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock


from mock import GPIO
from mock.SDL_DS3231 import SDL_DS3231
from src.parking_garage import ParkingGarage
from src.parking_garage import ParkingGarageError

class TestParkingGarage(TestCase):
#Test sul sensore di parking garage
    @patch.object(GPIO, "input")
    def test_check_occupancy(self, mock_distance_sensor: Mock):
        # This is an example of test where I want to mock the GPIO.input() function
        mock_distance_sensor.return_value=True
        system= ParkingGarage()
        occupied= system.check_occupancy()
        self.assertTrue(occupied)
        #Testing the case where is occupied
        #Now we have to control the indirect input


    def test_check_raises_errors(self, mock_distance_sensor: Mock):
     system= ParkingGarage()
        self.assertRaises(ParkingGarageError, system.check_occupancy, -1)

    def test_occupied_spots(self, mock_distance_sensors: Mock):
        mock_distance_sensors.side_effect=[True,False,True]
        system= ParkingGarage()
        number= system.get_number_occupied_spots()
        self.assertEqual(number,True)
