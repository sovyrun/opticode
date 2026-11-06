package main

import (
	"crypto/sha256"
	"fmt"
	"io"
	"os"
	"path/filepath"
)

const ChunkSize = 250

func main() {
	if len(os.Args) < 2 {
		fmt.Println("[ERROR] Usage: go run splitter.go <filename>")
		return
	}

	filePath := os.Args[1]
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Printf("[ERROR] Failed to open source file: %v\n", err)
		return
	}
	defer file.Close()

	fileName := filepath.Base(filePath)
	buffer := make([]byte, ChunkSize)
	var chunks [][]byte

	for {
		bytesRead, err := file.Read(buffer)
		if bytesRead > 0 {
			chunkCopy := make([]byte, bytesRead)
			copy(chunkCopy, buffer[:bytesRead])
			chunks = append(chunks, chunkCopy)
		}
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Printf("[ERROR] Failure during stream read: %v\n", err)
			return
		}
	}

	totalChunks := len(chunks)
	fmt.Printf("[SOVYRUN] File '%s' successfully split into %d transmission payloads.\n\n", fileName, totalChunks)

	for i, chunk := range chunks {
		hasher := sha256.New()
		hasher.Write(chunk)
		checksum := fmt.Sprintf("%x", hasher.Sum(nil))[:8]

		// Format: filename|chunk_index|total_chunks|checksum|data
		fmt.Printf("=== START PAYLOAD %d/%d (%d Bytes) ===\n", i+1, totalChunks, len(chunk))
		fmt.Printf("%s|%d|%d|%s|%s\n", fileName, i+1, totalChunks, checksum, string(chunk))
		fmt.Printf("=== END PAYLOAD %d/%d ===\n\n", i+1, totalChunks)
	}
}
