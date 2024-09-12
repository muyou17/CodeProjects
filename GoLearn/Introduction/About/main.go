package main

import "fmt"

func main() {
	var a, b int
	var operator string

	fmt.Print("Enter a: ")
	fmt.Scanf("%d", &a)
	fmt.Printf("Type a: %T. Value a: %v\n", a, a)
	fmt.Print("Enter b: ")
	fmt.Scanf("%d", &b)
	fmt.Printf("Type b: %T. Value b: %v\n", b, b)
	fmt.Print("Enter operator: ")
	fmt.Scanf("%s", &operator)
	fmt.Printf("Type operator: %T. Value operator: %v\n", operator, operator)

	switch operator {
	case "+":
		fmt.Println("a + b =", a+b)
	case "-":
		fmt.Println("a - b =", a-b)
	case "*":
		fmt.Println("a * b =", a*b)
	case "/":
		fmt.Println("a / b =", a/b)
	default:
		fmt.Println("Unknown operator")
	}
}
