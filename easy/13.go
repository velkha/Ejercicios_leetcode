// Queria revisar sintaxis de go
func romanToInt(s string) int {
    romanValues := map[byte]int{
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total := 0
    length := len(s)

    for i := 0; i < length; i++ {
        if i+1 < length && romanValues[s[i]] < romanValues[s[i+1]] {
            total -= romanValues[s[i]]
        } else {
            total += romanValues[s[i]]
        }
    }

    return total
}