import os

jpg0 = 0xFF
jpg1 = 0xD8
gif0 = 0x47
gif1 = 0x49
png0 = 0x89
png1 = 0x50


def dat_to_image(input_dat_path, output_img_path):
    try:
        with open(input_dat_path, 'rb') as f:
            b = bytearray(f.read())
    except Exception as e:
        return "", str(e)

    if len(b) < 2:
        return "", "image size error"

    j0 = b[0] ^ jpg0
    j1 = b[1] ^ jpg1
    g0 = b[0] ^ gif0
    g1 = b[1] ^ gif1
    p0 = b[0] ^ png0
    p1 = b[1] ^ png1

    v = None
    ext = ""

    if j0 == j1:
        v = j0
        ext = "jpg"
    elif g0 == g1:
        v = g0
        ext = "gif"
    elif p0 == p1:
        v = p0
        ext = "png"
    else:
        return "", "unknown image format"

    for i in range(len(b)):
        b[i] ^= v

    filename = os.path.basename(input_dat_path)
    imgpath = os.path.join(output_img_path, os.path.splitext(filename)[0] + '.' + ext)  # Save with detected extension
    try:
        with open(imgpath, 'wb') as f:
            f.write(b)
    except Exception as e:
        return "", str(e)

    return imgpath, None


def main():
    dat_folder = os.path.join(os.getcwd(), 'dat')
    img_folder = os.path.join(os.getcwd(), 'img')

    # Create img directory if it doesn't exist
    os.makedirs(img_folder, exist_ok=True)

    # Process all .dat files in the dat directory
    for filename in os.listdir(dat_folder):
        if filename.endswith('.dat'):
            input_dat_path = os.path.join(dat_folder, filename)
            imgpath, error = dat_to_image(input_dat_path, img_folder)

            if error:
                print(f"Error processing {filename}: {error}")
            else:
                print(f"Processed {filename} to {imgpath}")

if __name__ == '__main__':
    main()
