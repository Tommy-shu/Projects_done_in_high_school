#Chinese Zodiac Bot
#Author: Tommy Shu          
#Date: Feb 04, 2019
#Description:

#Ask what year you are born between 1948-2007?
print ("what year you are born between 1948 and 2007?")

#get the user's reply
reply= int(input())

# Check to make sure they gave an appropriate year
if reply<1948:
 print ("sorry, you have to give me a number between 1948 and 2007")
elif reply>2007:
 print ("sorry, you have to give me a number between 1948 and 2007")
else:
 
 reply = str(reply)
 #If they said 1996,1984,1972,1960,1948, then reply rat
 if reply=="1996" or reply=="1984" or reply=="1972" or reply=="1960" or reply=="1948":
    print("your Chinese Zodiac is Rat")
 #If they said 1997,1985,1973,1961,1949, then reply ox
 elif reply=="1997" or reply=="1985" or reply=="1973" or reply=="1961" or reply=="1949":
   print("your Chinese Zodiac is ox")
 #If they said 1998,1986,1974,1962,1950, then reply tiger
 elif reply=="1998" or reply=="1986" or reply=="1974" or reply=="1962" or reply=="1950":
   print("your Chinese Zodiac is tiger") 
 #If they said 1999, 1987,1975,1963,1951, then reply rabbit
 elif reply=="1999" or reply=="1987" or reply=="1975" or reply=="1963" or reply=="1951":
   print("your Chinese Zodiac is rabbit") 
 #If they said 2000,1988,1976,1964,1952, then reply dragon
 elif reply=="2000" or reply=="1988" or reply=="1976" or reply=="1964" or reply=="1952":
   print("your Chinese Zodiac is dragon")
 #If they said 2001,1989,1977,1965,1953, then reply snake
 elif reply=="2001" or reply=="1989" or reply=="1977" or reply=="1965" or reply=="1953":
   print("your Chinese Zodiac is snake")
 #If they said 2002,1990,1978,1966,1954, then reply horse
 elif reply=="2002" or reply=="1990" or reply=="1978" or reply=="1966" or reply=="1954":
   print("your Chinese Zodiac is horse") 
 #If they said 2003,1991,1979,1967,1955, then reply goat
 elif reply=="2003" or reply=="1991" or reply=="1979" or reply=="1967" or reply=="1955":
   print("your Chinese Zodiac is goat")
 #If they said 2004,1992,1980,1968,1956, then reply monkey 
 elif reply=="2004" or reply=="1992" or reply=="1980" or reply=="1968" or reply=="1956":
   print("your Chinese Zodiac is monkey")
 #If they said 2005,1993,1981,1969,1957, then reply rooster
 elif reply=="2005" or reply=="1993" or reply=="1981" or reply=="1969" or reply=="1957":
   print("your Chinese Zodiac is rooster")
 #If they said 2006,1994,1982,1970,1958, then reply dog
 elif reply=="2006" or reply=="1994" or reply=="1982" or reply=="1970" or reply=="1958":
   print("your Chinese Zodiac is dog")
 #If they said 2007,1995,1983,1971,1959, then reply pig
 else: 
  print("your Chinese Zodiac is pig")