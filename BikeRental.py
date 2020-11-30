import datetime

class BikeRental:
    def __init__(self, stock = 0):
        self.stock = stock

    def displaystock(self): #the current stock level in the shop
        print("We have currently {} bikes available to rent!".format(self.stock))
        return self.stock
    def rentBikeOnHourlyBasis(self,n):
        if n <= 0:
            print("Please provide a positive number of bikes to rent")
            return None
        elif n > self.stock:
            print("Sorry we currently only have {} bikes to rent out".format(self.stock))

            return None
        else:
            current = datetime.datetime.now()
            print("You have rented {} bikes at {} at a rate of $5 per hour per bike".format(n,current))
            print("Enjoy your bike ride")
            self.stock -= n
            return current
    def rentBikeOnDailyBasis(self,n):
        if n <= 0:
            print("Please provide a positive number of bikes to rent")
            return None
        elif n > self.stock:
            print("Sorry we currently only have {} bikes to rent out".format(self.stock))

            return None
        else:
            current1 = datetime.datetime.now()
            print("You have rented {} bikes at {} at a rate of $20 for the day".format(n, current1.hour))
            print("Enjoy your bike ride")
            self.stock -= n
            return current1

    def rentBikeOnWeeklyBasis(self,n):
        if n <= 0:
            print("Please provide a positive number of bikes to rent")
            return None
        elif n > self.stock:
            print("Sorry we currently only have {} bikes to rent out".format(self.stock))

            return None
        else:
            current2 = datetime.datetime.now()
            print("You have rented {} bikes at {} at a rate of $60 for the week".format(n, current2.hour))
            print("Enjoy your bike ride")
            self.stock -= n
            return current2

    def returnBike(self, request):
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0
        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            currentTime = datetime.datetime.now()
            totalTime = rentalTime - currentTime

            if rentalBasis == 1:
                bill = round(totalTime.seconds / 3600) * 5 * numOfBikes
                print("Your total bill is $" + str(bill))
            elif rentalBasis == 2:
                bill = round(totalTime.days) * 20 * numOfBikes
                print("Your total bill is $" + str(bill))
            else:
                bill = round(totalTime.days / 7) * 60 * numOfBikes
                print("Your total bill is $" + str(bill))
        return bill



class Customer:
    def __init__(self): #Constructor class for the customers renting the bike
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        bikes = int(input("How many bikes would you like to rent? "))


        try:
            int(bikes)
        except ValueError:
            print("That is not a valid selection")
            return -1

        if bikes < 1:
            print("Cannot hire less than 1 bike")
            return -1
        else:
            self.bikes = bikes
            return self.bikes

    def returnBike(self):
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0,0,0










