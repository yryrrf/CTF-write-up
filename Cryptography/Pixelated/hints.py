from PIL import Image
image1 = Image.open('scrambled1.png');
image2 = Image.open('scrambled2.png');

ans = Image.new('RGB', (256, 256));

def process(v):
        if(v==1):
                return 256;
        return 0;

for i in range(0,256):
        for j in range(0,256):
                x = image1.getpixel((i,j))[0] + image2.getpixel((i,j))[0];
                y = image1.getpixel((i,j))[1] + image2.getpixel((i,j))[1];
                z = image1.getpixel((i,j))[2] + image2.getpixel((i,j))[2];                x = x%256;
                y = y%256;
                z = z%256;
                ans.putpixel((i,j),(x,y,z));

ans.save("ans.png", "PNG")

# Just Stack it together and generate as a new picture
# e.g. two pixels (2,30,253) + (2,45,64) = (4,75,317)
# Then %256 to avoid overflow -> (4,75,61)
# Put that pixel to a new image
