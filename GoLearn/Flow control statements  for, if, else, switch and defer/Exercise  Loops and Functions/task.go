package main

import (
	"fmt"
)

func Sqrt(x float64) float64 {
	var z float64 = x
	for i := 0; i < 10; i++ {
		z -= (z*z - x) / (2 * z)
	}
	return z
}

func main() {
	fmt.Printf("%.16f ", Sqrt(2))
	fmt.Printf("%.16f ", Sqrt(2))
	fmt.Println(0)
}
