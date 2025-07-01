import cv2
from pyzbar.pyzbar import decode
import numpy as np
import sys

def scan_code_from_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Could not access the camera.")
        sys.exit(1)

    print("Scanning... Press 'q' to cancel.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("ERROR: Could not read from camera.")
            break

        codes = decode(frame)
        if codes:
            print(f"Found {len(codes)} code(s).")
        else:
            print("No code detected in this frame.")

        for code in codes:
            code_data = code.data.decode('utf-8')
            print("Detected Code:", code_data)

            # Draw box
            pts = code.polygon
            pts = [(pt.x, pt.y) for pt in pts]
            cv2.polylines(frame, [np.array(pts)], True, (0, 255, 0), 2)
            cv2.putText(frame, code_data, (pts[0][0], pts[0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            cv2.imshow("Scanner", frame)
            cv2.waitKey(1000)

            cap.release()
            cv2.destroyAllWindows()

            print(code_data)
            sys.exit(0)

        cv2.imshow("Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Scan cancelled by user.")
            break

    cap.release()
    cv2.destroyAllWindows()
    sys.exit(1)

if __name__ == "__main__":
    scan_code_from_camera()
