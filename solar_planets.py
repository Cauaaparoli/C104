import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sol",
            (80,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (28, 139, 223)
            )

cv2.putText(img,
            "Mercurio",
            (110,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (185, 185, 185)
            )

cv2.putText(img,
            "Venus",
            (192,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 95, 213)
            )

cv2.putText(img,
            "Terra",
            (283,265),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (224, 115, 31)
            )

cv2.putText(img,
            "Lua",
            (320,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (176, 175, 175)
            )

cv2.putText(img,
            "Marte",
            (380,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (181, 106, 182)
            )

cv2.putText(img,
            "Jupiter",
            (510,60),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6,
            (127, 163, 203)
            )

cv2.putText(img,
            "Saturno",
            (770,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (121, 150, 187)
            )

cv2.putText(img,
            "Urano",
            (970,135),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (237, 234, 196)
            )

cv2.putText(img,
            "Netuno",
            (1115,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (242, 111, 68)
            )

cv2.imshow("resultado", img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)