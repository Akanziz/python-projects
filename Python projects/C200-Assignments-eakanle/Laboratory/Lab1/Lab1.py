def computeShippingPrice(height, width, depth, weight):
    return 5 * height * width * depth * weight

if __name__=="__main__":
    x= computeShippingPrice(10,10,10,10)
    print ("Compute ShippingPrice:",x)
    