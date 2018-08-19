
# Go Dry
> A wifi controlled GoKart

# Hardwares Used
1. [Arduino Uno](http://img.dxcdn.com/productimages/sku_370842_1.jpg)
2. [Common Anode RGB Led](https://storage.googleapis.com/stateless-www-faranux-com/2017/02/5mm-RGB-LED-Anode.png)
3. [L239D IC and Circuit](https://www.elementzonline.com/image/cache/catalog/data/products/Interface%20Boards/Motor%20Driver/Enusn%20Board%20with%20IC/IMG_0035-500x500.JPG)
4. [ESP 01 Wifi Module](https://researchdesignlab.com/media/catalog/product/cache/1/image/512x512/9ea150a65d3ccc136116bd4ea279f951/e/s/esp8266-esp-01-serial-wifi-wireless-transceiver-module-250x250.jpg)
5. [100 Rotation DC Geared Motor](https://images-na.ssl-images-amazon.com/images/I/414ATaxpPFL.jpg)
6. [Solderless Breadboard](https://d2drzakx2pq6fl.cloudfront.net/production/products/142/large/small-breadboard.jpg?1442476912)
7. [Jump Wires](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/A_few_Jumper_Wires.jpg/1200px-A_few_Jumper_Wires.jpg)
8. [9V Battery](https://core-electronics.com.au/media/catalog/product/cache/1/image/650x650/fe1bcd18654db18f328c2faaaf3c690a/1/3/1321-00.jpg)

# Circuit Diagram


# How to use
1. Connect the circuit as shown in [Circuit Diagram Section](#circuit-diagram)
2. Upload the `wifiCar.ino` code.
**Note :** Make sure you have entered correct AP and Password in 6 & 7 line
```cpp
String AP =  "";   // your AP SSID
String Password  = "";  // your AP Password
```
3. Press CTRL+U to upload the code
4. Wait untill Green LED i.e _Ready To Use_
5. Choose any driver in `Driver/` directory
