import cv2
import numpy as np
import os

def run_optical_ingest():
    # Target index 0 for standard integrated or direct USB webcam structures
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Optical capture stream could not initialize hardware links.")
        return

    # Utilize standard high-performance matrix detector
    detector = cv2.QRCodeDetector()
    print("[READY] Sovyrun Optical Ingest Engine Live. Awaiting transmission payload...")

    received_chunks = {}
    expected_total = None
    target_filename = "reassembled_output.txt"
    desktop_path = os.path.expanduser("~/Desktop")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[WARN] Frame drop detected in camera link loop.")
            continue

        # Flip for natural orientation mirroring
        corrected_frame = cv2.flip(frame, 1)
        
        # Performance optimization: Grayscale conversion before threshold evaluation
        gray = cv2.cvtColor(corrected_frame, cv2.COLOR_BGR2GRAY)
        _, threshold_frame = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)

        # Parse the contrasting visual matrices
        raw_data, bbox, _ = detector.detectAndDecode(threshold_frame)
        
        if raw_data:
            try:
                # Structural protocol parsing: filename|chunk_idx|total_chunks|checksum|data
                parts = raw_data.split('|', 4)
                if len(parts) == 5:
                    filename, idx_str, total_str, checksum, data = parts
                    idx = int(idx_str)
                    total = int(total_str)
                    
                    if expected_total is None:
                        expected_total = total
                        target_filename = f"sovyrun_{filename}"
                        print(f"\n[INCOMING] File stream detected: {target_filename}")
                        print(f"[PROGRESS] Allocating memory structure for {total} sequential packets...")

                    if idx not in received_chunks:
                        received_chunks[idx] = data
                        print(f"[PACKET] Successfully indexed segment {idx}/{total} [SHA-S: {checksum}]")

                    # Execute automated compilation block upon total stack verification
                    if len(received_chunks) == expected_total:
                        output_path = os.path.join(desktop_path, target_filename)
                        
                        with open(output_path, "w", encoding="utf-8") as file_out:
                            for i in range(1, expected_total + 1):
                                file_out.write(received_chunks[i])
                                
                        print(f"\n[SUCCESS] Matrix transmission sequence terminated flawlessly.")
                        print(f"[STORAGE] File cleanly reassembled on desktop surface: {output_path}")
                        break
            except Exception:
                # Sandbox processing anomalies caused by partial frame distortions during motion
                pass

        # Display the real-time feedback monitors
        cv2.imshow("Sovyrun Engine - Real-Time Feed", corrected_frame)
        cv2.imshow("Sovyrun Engine - High-Contrast Filter", threshold_frame)

        # Listen for explicit manual escape sequence
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[SYSTEM] Manual escape code received. Terminating capture pipeline...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_optical_ingest()
