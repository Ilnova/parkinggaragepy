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
        occupied= system.check_occupancy(system.INFRARED_PIN1)
        self.assertTrue(occupied)
        #Testing the case where is occupied
        #Now we have to control the indirect input


    def test_check_raises_errors(self):
        system= ParkingGarage()
        self.assertRaises(ParkingGarageError, system.check_occupancy, -1)


    def test_occupied_spots(self, mock_distance_sensor: Mock):
        mock_distance_sensor.side_effect=[True,False,True]
        system= ParkingGarage()
        number= system.get_number_occupied_spots()
        self.assertEqual(number,True)
        #Verificare perché da errore su mock_distance_sensor nel momento del test
    @patch.object(SDL_DS3231, 'read_datatime')
    def test_calculate_parking_fee(self, mock_exit_time: Mock):
        #tempo exit, ci conviene test ad orario spaccato senza minuti
        mock_exit_time.return_value= datetime(2024,11,6,12,00,00)
        system = ParkingGarage()
        #qui gli verrà passato l'entry time
        fee= system.calculate_parking_fee(datetime(2024,11,6,10,00,00))
        self.assertEqual(5,fee) #Sono due ore quindi 2.50x2 ci aspettiamo 5 euro
        #ragioniamo sugli input, ora gli indirect input (aggiunti sopra col nome di mock)