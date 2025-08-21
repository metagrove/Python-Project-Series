// .add()
// .delete()
// .has()


const my_set = new Set([1,2,3] ) 
console.log(my_set) // Set(3) { 1, 2, 3 }

my_set.add(4) // Set(4) { 1, 2, 3, 4 }
console.log(my_set)

my_set.delete(4) // Set(4) { 1, 2, 3, 4 } // no duplicates allowed

my_set.clear() // Set(0) {}
console.log(my_set) // Set(0) {}