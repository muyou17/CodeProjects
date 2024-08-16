package main

import (
	"fmt"
	"math"
)

func add(x, y int, a, b float32) float32 {
	return a + b + float32(x+y)
}

func main() {
	fmt.Println(add(42, 13, 4.5, math.Pi))
}
