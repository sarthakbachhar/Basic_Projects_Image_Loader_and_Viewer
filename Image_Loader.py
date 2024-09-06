import cv2

# Load the image  
img = cv2.imread("C:\\Users\\Acer\\Desktop\\nobi.jpg")

# Check if the image was successfully loaded 
if img is None:
  print("Unable to load image.")
else:
  # Display the image 
  cv2.imshow("Cartoon", img)

# To display until a key is pressed
cv2.waitKey(0)

# To close all windows opened by opencv
cv2.destroyAllWindows()
