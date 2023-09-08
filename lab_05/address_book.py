def get_formatted_address_string(address, city, country, name=("Undisclosed Recipient"), postal_code=0):
    if postal_code==int(0):
        return(name+"\n"+address+"\n"+city+","+country)
    return(name+"\n"+address+"\n"+city+","+country+"\n"+str(postal_code))

def main():
    """
    Just some sample behavior. Feel free to try your own!
    """
    test_name = "Herodotos of Halicarnassus"
    test_address = "Dionysiou Areopagitou 15"
    test_city = "Athens"
    test_country = "Greece"
    test_postal_code = 0

    address_string = get_formatted_address_string(address=test_address, city=test_city, country=test_country,
                                                  name=test_name, postal_code=test_postal_code)

    print(address_string)


# DO NOT WRITE CODE BELOW THIS LINE

if __name__ == '__main__':
    main()
