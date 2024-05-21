package main

import (
    "fmt"
    "log"
    "net/http"

    utils "github.com/octopart/interview-octo-backend/go-app/utils"
)

// Helper function for mocked data
func generateJson() []byte {
    return utils.PartOffers()
}

func healthCheck(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "OK")
}

func main() {
    http.HandleFunc("/health", healthCheck)
    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatalf("Failed to start server: %v", err)
    }
}
