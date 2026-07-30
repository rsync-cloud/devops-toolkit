package main

import (
    "bufio"
    "fmt"
    "os"
    "regexp"
    "strings"
)

func main() {
    if len(os.Args) < 3 {
        fmt.Println("Usage: log-parser <logfile> <pattern>")
        os.Exit(1)
    }
    file, err := os.Open(os.Args[1])
    if err != nil {
        fmt.Printf("Error opening file: %v\n", err)
        os.Exit(1)
    }
    defer file.Close()

    re, err := regexp.Compile(os.Args[2])
    if err != nil {
        fmt.Printf("Invalid regex: %v\n", err)
        os.Exit(1)
    }

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := scanner.Text()
        if re.MatchString(line) {
            fmt.Println(strings.TrimSpace(line))
        }
    }
}
