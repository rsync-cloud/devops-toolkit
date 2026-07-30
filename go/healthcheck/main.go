package main

import (
    "fmt"
    "net/http"
    "os"
    "time"
)

func main() {
    url := "http://localhost:8080/health"
    if len(os.Args) > 1 {
        url = os.Args[1]
    }
    client := http.Client{Timeout: 5 * time.Second}
    resp, err := client.Get(url)
    if err != nil {
        fmt.Printf("FAIL: %s unreachable: %v\n", url, err)
        os.Exit(1)
    }
    defer resp.Body.Close()
    if resp.StatusCode >= 200 && resp.StatusCode < 400 {
        fmt.Printf("OK: %s returned %d\n", url, resp.StatusCode)
    } else {
        fmt.Printf("FAIL: %s returned %d\n", url, resp.StatusCode)
        os.Exit(1)
    }
}
