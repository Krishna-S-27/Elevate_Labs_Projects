package main

import (
	"fmt"
	"os"
)

var GlobalVar = 123 // bad: global variable not recommended

func addNumbers(a int, b int) int {
    result := a + b
    return result
}

func BadFunction(x int, y int) int {
    if x > y {
        if x > 100 {
            fmt.Println("x is very big")
        } else {
            fmt.Println("x is just bigger")
        }
    } else {
        if y > 100 {
            fmt.Println("y is very big")
        } else {
            fmt.Println("y is just bigger")
        }
    }
    return x + y
}

func readFile(filename string) {
    file, _ := os.Open(filename) // bad: ignoring error
    defer file.Close()
    buffer := make([]byte, 100)
    file.Read(buffer) // bad: ignoring error
    fmt.Println(string(buffer))
}

func main() {
    x := 10
    y := 20
    unused := 50 // unused variable

    fmt.Println("Result:", addNumbers(x, y))
    fmt.Println("Bad result:", BadFunction(x, y))

    readFile("nonexistent.txt")
}
