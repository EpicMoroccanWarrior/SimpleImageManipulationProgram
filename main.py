import IMP 
IMP.show_image("./Untitled.jpg")
IMP.show_image_in_mode("./Untitled.jpg", "Invert")
IMP.show_image_in_mode("./Untitled.jpg", "FlipHorizontal")
IMP.show_image_in_mode("./Untitled.jpg", "FlipVertical")
IMP.show_image("./grey.jpg")
IMP.show_image_in_mode("./grey.jpg", "GrayscaleToBw", 128) #the threshold is variable, the default value is 128