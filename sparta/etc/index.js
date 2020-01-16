// Remainder calculation with % 
// let <variable> = <data type> (javascript) = "a <- 10" (R)
// let <variable> = <data type>  --> 동적 O
// const <variable> = <data type> --> enforced data type

//Conventions in javascript 
let my_first_name = 'CW' //snake case  --> 관례
let myFirstName= 'CW' //camel case 

// let a = 10
// a
// console.log("AAA")

// for (let <var> = data; cond ; function)

for (let i = 1; i<= 10; i++) {
  console.log(i)
}
console.log(3==4 + 'print')
console.log('print' + 7)

age = 20
if (age> 19){
  console.log('성인입니다')
} else if (age>50){
  console.log('노인입니다')
} //else {}

let birth = '19911201'
typeof(birth)

// Data structure: numerics, string, boolean, and the collections like array and map (dict)
//Array 
a = [1,2,3,4,5,6,7,8,9,10]
console.log(a[0])
a.push(103)
//Insert data into such end to array example 

// map (Json)
a = {
  'a': 1, 'b' : 2
}
console.log(a)
a['This is array'] = [1,2,3]
console.log(a)

// Function 함수
function hey(a1, a2){
  console.log("시작")
  console.log(a1)
  console.log(a2)
}


