# Sovyrun: Opticode (v1.0.0)
### Out-of-Band Ocular Data Ingestion Framework for Isolated Compute Nodes

An ultra-lean, air-gapped transmission protocol designed to facilitate unidirectional data ingestion between disparate hardware architectures via pure optical parsing, bypassing physical media contact (USB) or network dependency bridge constraints entirely.

Opticode utilizes a standard camera lens as an artificial QR code retina translator. The isolated target machine reads incoming transmission matrix arrays exactly like a human operator, enforcing an un-hackable, out-of-band boundary for sandboxed script execution testing.

## Protocol Mechanics
- **Frame Density Restriction:** Payloads are strictly limited to a maximum of 250 bytes per packet. This enforces low pixel matrix density, ensuring crisp edge-contrast translation and error-free parsing over variable frame rates or legacy camera optics.
- **Data Integrity Engine:** Each individual packet segment carries an isolated 8-character hardware-accelerated SHA256 checksum string. The receiving node drops duplicate reads, validates the data matrix packet-by-packet, and automatically reassembles the sequential stream back to disk upon array completion.

## Single-Step Execution

### 1. Transmit Payload (From Main Workstation)
```bash
go run opticode_splitter.go target_script.sh
```
*(Render the resulting output strings as standard sequential visual matrix blocks on your display monitor).*

### 2. Ingest Payload (On Air-Gapped Target Node)
```bash
pip3 install opencv-python numpy pillow && python3 opticode_ingest.py
```
*Point your hardware sensor at the transmission screen. The protocol will automatically compile and reassemble the target payload file directly onto the local desktop surface.*
