while True:   
    import cv2
    import numpy as np
    rasm_nomi = input("Rasm nomini kiriting: ")
    if rasm_nomi != "0":
        rasm = input("Saqlash uchun rasm nomini kiriting: ")

                        #rasmnomi
        img = cv2.imread(f"{rasm_nomi}")

        #cv2.rectangle(img, (409,127), (858,760), (0, 255, 0), 3)

        cut_img = img[127:760, 409:858]

                        #nom
        cv2.imwrite(f'{rasm}', cut_img)

        #cv2.imshow("cut_img", cut_img)
        cv2.waitKey(0)
    else:
        break