import IMP 
IMP.show_image("./Untitled.jpg")
IMP.show_image_in_mode("./Untitled.jpg", "Invert")
IMP.show_image_in_mode("./Untitled.jpg", "FlipHorizontal")
IMP.show_image_in_mode("./Untitled.jpg", "FlipVertical")
IMP.show_image("./grey.jpg")
IMP.show_image_in_mode("./grey.jpg", "GrayscaleToBw", threshold = 128) #the threshold is variable, if not provided the default value is 128
IMP.show_image_in_mode("./grey.jpg", "Frame", frame_width = 20) #the frame_width is variable, if not provided the default value is 10
