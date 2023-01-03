const arr1 = [ 1, 2, 3]
const arr2 = [4, 5, 6]


// usando o concat
const arr = arr1.concat(arr2)
console.log(arr)


// usando o spread operactor
const arr0 = [...arr1, ...arr2,'Guilherme', ...arr]
console.log(arr0)