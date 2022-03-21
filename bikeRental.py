import datetime

class BikeRental:
    
    def __init__(self,stock=0):
        """
        Our constructor class that instantiates bike rental shop.
        """

        self.stock = stock

    def displaystock(self):
        #Displays the bikes currently available for rent in the shop.
        
        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock

    def rentBikeOnMinutesBasis(self, n):
        #Rents a bike on Minutes basis to a customer.
        
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} bike(s) on Minutes basis today at {} hours.".format(n,now.hour))
            print("You will be charged Rs 50 for each hour per bike.")
            

            self.stock -= n
            return now      
     
    def rentBikeOnHourlyBasis(self, n):
        #Rents a bike on Hourly basis to a customer.
      
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("You have rented {} bike(s) on Hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged Rs 100 for each day per bike.")
            
            self.stock -= n
            return now
        
    def rentBikeOnDaysBasis(self, n):
        #Rents a bike on Days basis to a customer.
       
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None        
        
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on Days basis today at {} hours.".format(n, now.hour))
            print("You will be charged Rs 200 for each week per bike.")
           
            self.stock -= n

            return now
    

    
    def returnBike(self, request):
       
        # Return a bill
    
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
        
            # Minutes bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 60) * 50 * numOfBikes
                
            # Hourly bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.seconds / 3600) * 100 * numOfBikes
                
            # Days bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days) * 200 * numOfBikes
            

            print("That would be Rs {}".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None



class Customer:

    def __init__(self):
        # Our constructor method which instantiates various customer objects.
       
        
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    
    def requestBike(self):
        #Takes a request from the customer for the number of bikes.
      
                      
        bikes = input("How many bikes would you like to rent? ")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):
      #Allows customers to return their bikes to the rental shop.
    
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0